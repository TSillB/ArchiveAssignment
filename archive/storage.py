import string
from errors import MalformedRecordError
from validation import validate_record
from queries import *

FIELD_NAMES = ["id", "title", "city", "year", "condition"]

# Parses one line (for one record) and returns a record dictionary (Does not validate the fields in the record)
def parse_line(line:string) -> dict:
    # Splits the line by the commas
    line_array = line.strip().split(",")

    # Checks if five fields have been found (raises MalformedRecordError otherwise)
    if len(line_array) != 5:
        raise MalformedRecordError
    
    # Iterates through the fields removing leading and trailing whitespace
    for i in range(len(line_array)):
        line_array[i] = line_array[i].strip()
    
    # Creates the record dictionary
    line_dict = {
        "id": line_array[0], 
        "title": line_array[1], 
        "city": line_array[2], 
        "year":line_array[3], 
        "condition":line_array[4],
    }
    return line_dict

# Loads the records at the provided file
def load_archive(path:string) -> tuple[list]:
    valid_records = []; rejected_records = []

    # Checks if the file at the path exists
    try:
        with open(path, "r") as file:
            for line in file:
                try:
                    record = parse_line(line)

                    # Checks if the record is valid using the validate_record function in validation.py
                    if len(validate_record(record)) > 0:
                        rejected_records.append(line)
                    else:
                        valid_records.append(record)
                except MalformedRecordError:
                    # Rejects the record if MalformedRecordError is raised by parse_line
                    rejected_records.append(line)

    except FileNotFoundError:
        # Returns nothing if no such file exists
        return ([],[])
    
    # Returns the rejected and valid records
    return (valid_records, rejected_records)

# Saves the provided (valid) records at the provided directory in an archive.csv file
def save_archive(path:string, records:list[dict]) -> None:
    # At the provided directory path, adds an archive.csv file
    path += "/archive.csv"

    # Checks if the provided file path is valid
    try:
        with open(path, "a") as file:

            # Adds each record in records line by line
            for record in records:
                # Validates the record
                if (len(validate_record(record) > 0)):
                    continue

                # Adds each element in the record to a list to be added to the file using file.writelines
                record_list = []
                for field in FIELD_NAMES:
                    record_list.append(record[field])
                    record_list.append(",")
                record_list.pop()
                record_list.append("\n")
                file.writelines(record_list)
    except FileNotFoundError:
        # Prints when the file is not found
        print("Invalid Folder Path")
