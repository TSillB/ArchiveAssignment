import string

# Counts the number of manuscripts made (strictly) before the provided year
def count_before(records:list[dict], year:int) -> int:
    result = 0

    # Iterates through each of the records checking counting the ones made before the specified year
    for record in records:
        if int(record["year"]) < year:
            result += 1
    return result

# Returns a list of the records from the provided city
def find_by_city(records:list[dict], city:string) -> list[dict]:
    city_records = []

    # Iterates through each of the records checking adding the ones whose names match the given one to a list
    for record in records:
        if record["city"].lower() == city.lower():
            city_records.append(record)
    return city_records

# Return the oldest found manuscript (the first found in case of a tie)
def oldest(records:list[dict]) -> dict:
    # This keeps track of the smallest year found so far (as the smaller the year the older the manuscript)
    oldest_found_year = 100000000

    # This keeps track of the first record found with the current year found above
    oldest_found_record = None

    # Iterates through the record updating oldest_found_year and oldest_found_record as above
    for record in records:
        if int(record["year"]) < oldest_found_year:
            oldest_found_record = record
            oldest_found_year = int(record["year"])
    
    # This will return none if there are no records
    return oldest_found_record

# Returns a dictionary which has key, value pairs where the key is a city and the value is the number of records from that city
# If there are no records for a city, it is not in the dictionary
def cities_summary(records:list[dict]) -> dict:
    city_record_count = {}

    # Iterates through each record adding 1 to the count in the city_record_count dictionary for the corresponding city
    for record in records:
        if record["city"].lower() in city_record_count:
            city_record_count[record["city"].lower()] += 1
        else:
            # Creates the key if it does not exist
            city_record_count[record["city"].lower()] = 1
    return city_record_count