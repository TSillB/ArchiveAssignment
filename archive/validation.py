"""Validation rules for manuscript records.

YOU IMPLEMENT THIS FILE.

Every validate_* function takes a raw string (exactly as it came out of the
CSV file) and returns a tuple:

    (True, "")              the value is trustworthy
    (False, "reason here")  the value is not, and here is why

The reason is a short human-readable string. The autograder checks the
boolean, not your exact wording — but a teammate reading your rejection log
should understand it, so write it for them.

READ THIS BEFORE YOU START
--------------------------
The year range is INCLUSIVE at both ends: 1100 and 1900 are VALID.
1099 and 1901 are not. Most marks lost in Part A are lost on that line.
"""

from archive.errors import MalformedRecordError  # noqa: F401  (you may not need it here)

KNOWN_CITIES = ["Timbuktu", "Djenne", "Gao", "Walata", "Chinguetti"]

VALID_CONDITIONS = ["fragile", "fair", "good"]

MIN_YEAR = 600
MAX_YEAR = 1900


def validate_id(value):
    """An ID is the letters 'MS' followed by exactly three digits.

    Valid:   "MS001", "MS742"
    Invalid: "MS1", "MS0012", "ms001", "XX001", "", "MS00A"

    Returns (bool, str).
    """
    Id = bool()
    message_Id = ""

    if value.strip() == "":
        Id = False
        message_Id = "Id not found"
    
    if len(value)!= 5:
        Id = False
        message_Id = "Id not 5 characters"

    try:
        int(value[3:])
        Id = True
    except ValueError:
        Id = False
        message_Id = "Invalid Id number" 

    if value[:2] != "MS" or (int(value[3:])<=0 or int(value[3:])>999):
        Id = False
        message_Id = "Invalid Id"
    else:
        Id = True
    
    return Id, message_Id
    # raise NotImplementedError("validate_id")


def validate_title(value):
    """A title must be present and at least 3 characters once stripped.

    Valid:   "Tarikh al-Sudan"
    Invalid: "", "   ", "Ab"

    Returns (bool, str).
    """
    title = bool()
    message_title = ""

    # if value.strip() == "":
    #     title = False
    #     message_title = "Title not found"

    if value.strip() and len(value.strip()>=3):
        title = True
    else:
        title = False
        message_title = "Title too short"


    return title, message_title
    # raise NotImplementedError("validate_title")


def validate_city(value):
    """A city must be present and appear in KNOWN_CITIES.

    Comparison is case-insensitive: "timbuktu" is acceptable.
    "Kano" is not in our list, so it is rejected — and that is a real
    decision with a cost. Write about it in your README.

    Returns (bool, str).
    """
    city = bool()
    message_city = ""

    if value.strip() == "":
        city = False
        message_city = "No city found"

    if value not in KNOWN_CITIES:
        city = False
        message_city = "Invalid city"
    else:
        city = True

    return city, message_city
    # raise NotImplementedError("validate_city")


def validate_year(value):
    """A year must be present, numeric, and between MIN_YEAR and MAX_YEAR
    INCLUSIVE.

    Valid:   "1655", "1100", "1900"
    Invalid: "", "   ", "c.1590", "sixteen fifty", "1099", "1901", "2087"

    Note that "2087" parses perfectly well as a number. It is still wrong.
    That is the whole point of a range check.

    Returns (bool, str).
    """
    year = bool()
    message_year = ""

    if value == "":
        year = False
        message_year = "Year is absent"

    try:
        int(value)
        year = True
    except ValueError:
        year = False
        message_year  = "Invalid year"

    if int(value) < MIN_YEAR and int(value) > MAX_YEAR:
        year = False
        message_year = "Year outside range"
    else:
        year = True
     
    return year, message_year
    # raise NotImplementedError("validate_year")


def validate_condition(value):
    """A condition must be one of VALID_CONDITIONS, case-insensitively.

    Valid:   "fragile", "GOOD", "Fair"
    Invalid: "excellent", "", "ok"

    Returns (bool, str).
    """
    condition = bool()
    message_condition = ""

    if value == "":
        condition = False
        message_condition = "Condition absent"
    
    if value.lower() not in VALID_CONDITIONS:
        condition = False
        message_condition = "Invalid condition"
    else:
        condition = True

    return condition, message_condition
    # raise NotImplementedError("validate_condition")


def validate_record(record):
    """Validate a whole record dictionary.

    record is a dict with the keys: id, title, city, year, condition.

    Returns a LIST of reasons the record is invalid — one string per broken
    rule, in this field order: id, title, city, year, condition.
    An empty list means the record is valid.

    Do not re-write the rules here. Call the five functions above.
    """
    raise NotImplementedError("validate_record")
