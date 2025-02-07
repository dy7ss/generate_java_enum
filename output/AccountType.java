public enum AccountType {
    FUTU("01"),
    TOZA("02");

    private final String code;

    AccountType(String code) {
        this.code = code;
    }

    public static AccountType fromCode(String code) {
        for (AccountType accounttype : AccountType.values()) {
            if (accounttype.code.equals(code)) {
                return accounttype;
            }
        }

        throw new IllegalArgumentException("No such enum code: " + code);
    }
}