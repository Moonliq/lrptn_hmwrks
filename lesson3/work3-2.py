import json

path = 'data-397-2020-08-25.json'

with open(path, 'r', encoding='windows-1251') as f:
    reader = json.loads(f.read())
    escal_total = []
    for row in reader:
        if row["RepairOfEscalators"] == []:
            pass
        else:
            print(row['NameOfStation'], row["RepairOfEscalators"])
