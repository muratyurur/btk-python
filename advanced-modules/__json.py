# dict
import json

person_string = '{"name": "Murat", "languages": ["python", "php"]}'
person_dict = {"name": "Murat", "languages": ["python", "php"]}

# JSON string to Dict
# result = json.loads(person_string)
# result = result["name"]
# result = result["languages"]
# result = result["languages"][0]

# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])

# Dict to JSON string


# result = json.dumps(person_dict)
#
# with open("person.json", "w") as f:
#     json.dump(person_dict, f)

person_dict = json.loads(person_string)

result = json.dumps(person_dict, indent=4, sort_keys=True)
print(person_dict)
print(result)
