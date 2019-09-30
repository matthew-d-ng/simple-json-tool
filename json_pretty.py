import json
import sys

if __name__ == "__main__":
  with open(sys.argv[1]) as json_file:
    data = json.load(json_file)

    new_file = open("newdata.json", "w")
    new_file.write(
      json.dumps(
        data, 
        indent=4, 
        sort_keys=True
      )
    )
    new_file.close()
