import json
import csv

with open('covid_cases.json', 'r') as covid_data:
    data = json.loads(covid_data.read())

fields = ['dateRep', 'countriesAndTerritories', 'cases', 'deaths']

with open('parsed_data.csv', 'w', newline='') as json_parsed:
    csv_file = csv.writer(json_parsed)
    csv_file.writerow(fields)
    for i in data["records"]:
        csv_file.writerow([i["dateRep"], i["countriesAndTerritories"], i["cases"], i["deaths"]])