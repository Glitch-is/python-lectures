import csv

persons = [
    ["Namel", "Favorite Food", "Favorite Fruit"],
    ["Hlynur", "Pizza", "Banana"],
    ["Konni", "hamburger", "Orange"],
    ["Other", "Other", "other"],
    [1, 2, 3, 3.14]
]

with open("csv_test.csv", "w") as csv_file:
    csv_writer = csv.writer(csv_file)
    for person in persons:
        csv_writer.writerow(person)

original_people = []
with open("csv_test.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        original_people.append(line)

for o_people in original_people:
    if o_people[0].isdigit():
        print(int(o_people[0]))
    else:
        print(f"Found string: {o_people[0]}")






