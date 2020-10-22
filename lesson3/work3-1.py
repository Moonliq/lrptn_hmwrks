import csv
import collections
from collections import Counter

with open('data-398-2020-09-18.csv', 'r', encoding='windows-1251') as f:
    fields = ["ID", "Name", "Longitude_WGS84", "Latitude_WGS84", "Street", "AdmArea", "District", "RouteNumbers", "StationName", "Direction", "Pavilion", "OperatingOrgName", "EntryState", "global_id", "geoData"]
    reader = csv.DictReader(f, fields, delimiter=';')
    streets_total = []
    for row in reader:
        streets_total.append(row["Street"])
    counter = Counter(streets_total)
print(counter.most_common(10))