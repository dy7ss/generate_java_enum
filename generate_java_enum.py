import os

INPUT_DIR = "input/"
OUTPUT_DIR = "output/"
OUTPUT_EXTENSION = ".java"

class Processor:
    def main(self):
        for input_file in os.listdir(INPUT_DIR):
            input_filepath = INPUT_DIR + input_file
            content = self.read_file(input_filepath)
            element_dict = self.shape_input_elements(content)
            enum_content = self.generate_enum(input_file.split(".")[0], element_dict)
            self.write_file(self.generate_outputfilepath(OUTPUT_DIR + input_file.split(".")[0]), enum_content)

    def read_file(self, filepath):
        with open(filepath, "r", encoding="UTF-8") as f:
            return f.read()

    def write_file(self, filepath, content):
        with open(filepath, "w", encoding="UTF-8") as f:
            f.write(content)
        print("generated", filepath)

    def generate_outputfilepath(self, class_name):
        return class_name + OUTPUT_EXTENSION
    
    def shape_input_elements(self, content):
        lines = content.split("\n")
        element_dict = dict()

        for line in lines:
            if line == "":
                continue

            if len(line.split(" ")) != 2:
                raise ValueError("format error")

            element_dict[line.split(" ")[1]] = line.split(" ")[0]

        return element_dict
    

    def generate_enum(self, class_name, element_dict):
        enum_values = []
        for key, value in element_dict.items():
            enum_values.append("    " + key + "(\"" + value + "\")")

        enum_values = ",\n".join(enum_values)
        enum_values = enum_values + ";\n"

        content = "public enum " + class_name + " {\n"
        content += enum_values
        content += "\n"
        content += "    private final String code;\n"
        content += "\n"
        content += "    " + class_name + "(String code) {\n"
        content += "        this.code = code;\n"
        content += "    }\n"
        content += "\n"
        content += "    public static " + class_name + " fromCode(String code) {\n"
        content += "        for (" + class_name + " " +  class_name.lower()  + " : " + class_name + ".values()) {\n"
        content += "            if (" + class_name.lower() + ".code.equals(code)) {\n"
        content += "                return " + class_name.lower() + ";\n"
        content += "            }\n"
        content += "        }\n"
        content += "\n"
        content += "        throw new IllegalArgumentException(\"No such enum code: \" + code);\n"
        content += "    }\n"
        content += "}"

        return content

if __name__ == "__main__":
    p = Processor()
    p.main()