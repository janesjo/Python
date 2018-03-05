import json

fo = open('json.txt', "w")
#x = json.dumps([1, 'simple', 'list'])
json.dump(fo, fo)
fo.close()