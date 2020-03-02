import json
# a = {"a": 3, "b": 4}
# print(a)
# print(type(a))
#
# json_string = json.dumps(a)
# print(json_string)
# print(type(json_string))
#
#
# json_dict = json.loads(json_string)
# print(json_dict)
# print(type(json_dict))


# with open('test.json', 'w') as f:
#     json.dump(a, f)

with open('test.json', 'r') as f:
    j = json.load(f)

print(j)


