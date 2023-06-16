# *-* coding:utf8 *-*
import random
import time
import json


prefix = []
suffix = []
random.seed(time.time_ns())

with open ("prefix.json", "r") as f:
    prefix = json.loads(f.read())

with open ("suffix.json", "r") as f:
    suffix = json.loads(f.read())

insChars = "abcdehilmnorstuvwxz"
noRepeatRecord = {}

def makeRandomName():
    chars = ""
    for i in range(random.randint(0, 3)):
        chars += insChars[random.randint(0, len(insChars) - 1)]

    rp = random.randint(0, len(prefix) - 1)
    rs = random.randint(0, len(suffix) - 1)
    name = prefix[rp] + chars + suffix[rs]

    if name in noRepeatRecord:
        return makeRandomName()

    noRepeatRecord[name] = 1
    return name

 
# test:
if __name__ == "__main__":
    for i in range(1000000):
        print(makeRandomName())
