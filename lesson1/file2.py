import csv
clients = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]
with open("table.csv", "w", encoding="utf-8") as test_table:
    fields = ["name", "age", "job"]
    writer = csv.DictWriter(test_table, fields, delimiter = ";")
    writer.writeheader()
    for rows in clients:
        writer.writerow(rows)
