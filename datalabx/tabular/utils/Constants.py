## List of Supported file types

SUPPORTED_FILE_TYPES = ['txt','csv', 'xlsx', 'xls', 'parquet', 'json']

## List of default Missingness Placeholders
_DEFAULT_MISSINGNESS_PLACEHOLDERS = ['N/A', '?', '-','—', # dashes used as placeholders
    # --- empty / whitespace ---
    "", " ", "  ", "   ", "\t", "\n", "\r", "\r\n",

    # --- null-like ---
    "null", "Null", "NULL",
    "none", "None", "NONE",
    "nil", "NIL",
    "nan", "NaN", "NAN",
    "na", "NA", "n/a", "N/A", "n.a.", "N.A.",'<NA>',
    "n.a", "N.a", "not available", "Not Available", "NOT AVAILABLE",
    "not applicable", "Not Applicable", "NOT APPLICABLE",
    "not known", "Not Known", "NOT KNOWN",
    "unknown", "Unknown", "UNKNOWN",
    "undefined", "Undefined", "UNDEFINED",
    "missing", "Missing", "MISSING",

    # --- empty words ---
    "blank", "Blank", "BLANK",
    "empty", "Empty", "EMPTY",
    "no data", "No Data", "NO DATA",
    "no value", "No Value", "NO VALUE",
    "no info", "No Info", "NO INFO",
    "no information", "No Information",

    # --- punctuation placeholders ---
    "-", "--", "---", "----",
    "_", "__", "___",
    ".", "..", "...",
    "*", "**", "***",
    "?", "??", "???",

    # --- bracketed nulls ---
    "<null>", "<NULL>", "<nil>",
    "(null)", "(NULL)", "(nil)",
    "[null]", "[NULL]", "[nil]",
    "{null}", "{NULL}", "{nil}",

    # --- excel / system errors ---
    "#N/A", "#NA", "#N/A N/A",
    "#NULL!", "#VALUE!", "#DIV/0!", "#REF!", "#NAME?", "#NUM!",
    "NULL_VALUE", "N/A VALUE",

    # --- ui / form placeholders ---
    "select", "Select", "SELECT",
    "select option", "Select Option",
    "choose", "Choose", "CHOOSE",
    "choose option", "Choose Option",
    "-- select --", "--Select--",
    "please select", "Please Select",
    "enter value", "Enter value", "enter text",
    "type here", "Type here",
    "click here", "Click here",
    "your name", "your name here",
    "enter name", "enter email",

    # --- dummy / fake data ---
    "test", "Test", "TEST",
    "dummy", "Dummy", "DUMMY",
    "sample", "Sample", "SAMPLE",
    "example", "Example", "EXAMPLE",
    "demo", "Demo", "DEMO",
    "lorem ipsum", "Lorem Ipsum",
    "asdf", "ASDF", "qwerty", "QWERTY",
    "xxx", "XXX", "xxxx", "XXXXX",

    # --- fake structured values ---
    "0000-00-00",
    "1900-01-01", "1970-01-01",
    "9999-12-31",
    "00/00/0000",
    "01/01/1900",
    "01/01/1970",

    # --- fake contact info ---
    "0000000000", "000-000-0000",
    "1234567890", "1111111111",
    "test@test.com", "example@example.com",
    "user@domain.com", "email@email.com",

    # --- booleans misused ---
    "false", "False", "FALSE",
    "true", "True", "TRUE",

    # --- misc junk ---
    "nill", "Nill", "NILL",
    "nil.", "null.", "none.",
    "tbd", "TBD",
    "to be decided", "To Be Decided",
    "to be determined", "To Be Determined",
    "pending", "Pending",
    "incomplete", "Incomplete",

    # --- scraped missingness artifacts ---
    "&nbsp;", "nbsp",
    "|", "||",
    "/", "//",
]