import string
from errors import MalformedRecordError
from validation import validate_record

FIELD_NAMES = ["id", "title", "city", "year", "condition"]


def parse_line(line:string) -> dict:
    line_array = line.strip().split(",")
    if len(line_array) != 5:
        raise MalformedRecordError
    for i in range(len(line_array)):
        line_array[i] = line_array[i].strip()
    line_dict = {
        "id": line_array[0], 
        "title": line_array[1], 
        "city": line_array[2], 
        "year":line_array[3], 
        "condition":line_array[4],
    }
    return line_dict


def load_archive(path:string) -> tuple[list]:
    valid_records = []; rejected_records = []
    try:
        with open(path, "r") as file:
            for line in file:
                try:
                    ldict = parse_line(line)
                    if not validate_record(ldict):
                        rejected_records.append(line)
                    else:
                        valid_records.append(ldict)
                except MalformedRecordError:
                    rejected_records.append(line)
    except FileNotFoundError:
        return ([],[]);
    return (valid_records, rejected_records)


def save_archive(path:string, records:list[dict]):
    path += "/archive.csv"
    with open(path, "a") as file:
        for record in records:
            record_list:list[string] = []
            for field in FIELD_NAMES:
                record_list.append(record[field])
                record_list.append(",")
            if (len(record_list) > 0):
                record_list.pop()
                record_list.append("\n")
                file.writelines(record_list)
