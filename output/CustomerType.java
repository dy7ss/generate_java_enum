public enum CustomerType {
    CORPORATE("01"),
    PERSONAL("02");

    private final String code;

    CustomerType(String code) {
        this.code = code;
    }

    public static CustomerType fromCode(String code) {
        for (CustomerType customertype : CustomerType.values()) {
            if (customertype.code.equals(code)) {
                return customertype;
            }
        }

        throw new IllegalArgumentException("No such enum code: " + code);
    }
}