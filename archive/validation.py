from archive.errors import MalformedRecordError  # noqa: F401  (you may not need it here)

KNOWN_CITIES = ["timbuktu", "djenne", "gao", "walata", "chinguetti"]

VALID_CONDITIONS = ["fragile", "fair", "good"]

MIN_YEAR = 600
MAX_YEAR = 1900


def validate_id(value):
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
    if value is None or str(value).strip() == "":
        return False, "Title not found"

    if len(value.strip())<3:
        return False, "Title too short"

    return (True, "")


def validate_city(value):
    if value is None or str(value).strip() == "":
        return False, "City not found"

    if value.lower() not in KNOWN_CITIES: # I updated KNOWN_CITIES for all elements to be lowercase for easier comparison
        return False, "Invalid city"

    return (True, "")


def validate_year(value):
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
    if value is None or str(value).strip() == "":
        return False, "Condition not found"
    
    if value.lower() not in VALID_CONDITIONS:
        return False, "Invalid condition"

    return (True, "")


def validate_record(record):
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
