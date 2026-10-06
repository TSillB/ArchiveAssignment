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

from errors import MalformedRecordError  # noqa: F401  (you may not need it here)

KNOWN_CITIES = ["timbuktu", "djenne", "gao", "walata", "chinguetti"]

VALID_CONDITIONS = ["fragile", "fair", "good"]

MIN_YEAR = 600
MAX_YEAR = 1900


def validate_id(value):
    """An ID is the letters 'MS' followed by exactly three digits.

    Valid:   "MS001", "MS742"
    Invalid: "MS1", "MS0012", "ms001", "XX001", "", "MS00A"

    Returns (bool, str).
    """
    if value is None or str(value).strip() == "":
        return False, "Id not found"
    
    if len(value)!= 5:
        return False, "Id not 5 characters"

    try:
        int(value[2:])
    except ValueError:
        return False, "Invalid Id number"

    if not value.startswith("MS"):
        return False, "Invalid Id format"
    
    if (int(value[2:])<=0 or int(value[2:])>999):
        return False, "Id number out of range"
    
    return (True, "")


def validate_title(value):
    """A title must be present and at least 3 characters once stripped.

    Valid:   "Tarikh al-Sudan"
    Invalid: "", "   ", "Ab"

    Returns (bool, str).
    """

    if value is None or str(value).strip() == "":
        return False, "Title not found"

    if len(value.strip())<3:
        return False, "Title too short"

    return (True, "")


def validate_city(value):
    """A city must be present and appear in KNOWN_CITIES.

    Comparison is case-insensitive: "timbuktu" is acceptable.
    "Kano" is not in our list, so it is rejected — and that is a real
    decision with a cost. Write about it in your README.

    Returns (bool, str).
    """

    if value is None or str(value).strip() == "":
        return False, "City not found"

    if value.lower() not in KNOWN_CITIES: # I updated KNOWN_CITIES for all elements to be lowercase for easier comparison
        return False, "Invalid city"

    return (True, "")


def validate_year(value):
    """A year must be present, numeric, and between MIN_YEAR and MAX_YEAR
    INCLUSIVE.

    Valid:   "1655", "1100", "1900"
    Invalid: "", "   ", "c.1590", "sixteen fifty", "1099", "1901", "2087"

    Note that "2087" parses perfectly well as a number. It is still wrong.
    That is the whole point of a range check.

    Returns (bool, str).
    """

    if value is None or str(value).strip() == "":
        return False, "Year not found"

    try:
        int(value)
    except ValueError:
        return False, "Invalid year"

    if int(value) < MIN_YEAR or int(value) > MAX_YEAR:
        return False, "Year outside range"
     
    return (True, "")


def validate_condition(value):
    """A condition must be one of VALID_CONDITIONS, case-insensitively.

    Valid:   "fragile", "GOOD", "Fair"
    Invalid: "excellent", "", "ok"

    Returns (bool, str).
    """
    if value is None or str(value).strip() == "":
        return False, "Condition not found"
    
    if value.lower() not in VALID_CONDITIONS:
        return False, "Invalid condition"

    return (True, "")


def validate_record(record):
    """Validate a whole record dictionary.

    record is a dict with the keys: id, title, city, year, condition.

    Returns a LIST of reasons the record is invalid — one string per broken
    rule, in this field order: id, title, city, year, condition.
    An empty list means the record is valid.

    Do not re-write the rules here. Call the five functions above.
    """
    invalid_list = []  

    result = validate_id(record["id"])
    if not result[0]:
        invalid_list.append(result[1])
    result = validate_title(record["title"])
    if not result[0]:
        invalid_list.append(result[1])
    result = validate_city(record["city"])
    if not result[0]:
        invalid_list.append(result[1])
    result = validate_year(record["year"])
    if not result[0]:
        invalid_list.append(result[1])
    result = validate_condition(record["condition"])
    if not result[0]:
        invalid_list.append(result[1])
        
    return invalid_list
