import json

def get_nested_value(data, keys):
    keys = keys.split("/")
    for key in keys:
        data = data.get(key)
    return data

# object = {"a":{"b":{"c":"d"}}}
# key = "a/b/c"

# object = {"x":{"y":{"z":"a"}}}
# key = "x/y/z"

object = {"a":{"b":{"c":"d"}}}
key = "a/b/c"
print(get_nested_value(object, key))

object = {"x":{"y":{"z":"a"}}}
key = "x/y/z"
print(get_nested_value(object, key))
