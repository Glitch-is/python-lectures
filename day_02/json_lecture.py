import json

d = [
    {
        "name": "konni",
        "language" : {
            "name": "python",
            "version": 3.6
        },
        "favorite_food": [
            "Steak",
            "Hamburgers"
        ],
        "count":[]
    },
    {
        "name": "hlynur",
        "language" : {
            "name": "python",
            "version": 2.7
        },
        "favorite_food": [
            "Pizza"
        ],
        "count":[]
    },
]

with open("json_test.json", "w") as json_file:
    json_file.write(json.dumps(d))

with open("json_test.json", "r") as json_file:
    original_d = json.loads(json_file.read())


print(original_d[0]["language"]["version"] + original_d[1]["language"]["version"])
