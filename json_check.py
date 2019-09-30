import json
import sys

def check_keys_list(data):
  for item in data:
    if type(item) is dict:
      check_keys_dict(item)
    elif type(item) is list:
      check_keys_list(item)

def check_keys_dict(data):
  keys = []
  for (key, val) in data.items():
    if key in keys:
      print("duplicate key {}".format(key))
    else:
      keys.append(key)

    if type(val) is dict:
      check_keys_dict(val)
    elif type(val) is list:
      check_keys_list(val)


if __name__ == "__main__":
  with open(sys.argv[1]) as json_file:
      data = json.load(json_file)
      if type(data) is dict:
        check_keys_dict(data)
        print("done..")
