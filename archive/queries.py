import string

def count_before(records:list[dict], year:int) -> int:
    result = 0
    for record in records:
        if int(record["year"]) < year:
            result += 1
    return result


def find_by_city(records:list[dict], city:string) -> list[dict]:
    city_records = []
    for record in records:
        if record["city"].lower() == city.lower():
            city_records.append(record)
    return city_records


def oldest(records:list[dict]) -> dict:
    oldest_found_year = 100000000
    oldest_found_record = None
    for record in records:
        if int(record["year"]) < oldest_found_year:
            oldest_found_record = record
            oldest_found_year = int(record["year"])
    return oldest_found_record


def cities_summary(records:list[dict]) -> dict:
    city_record_count = {}
    for record in records:
        if record["city"].lower() in city_record_count:
            city_record_count[record["city"].lower()] += 1
        else:
            city_record_count[record["city"].lower()] = 1
    return city_record_count