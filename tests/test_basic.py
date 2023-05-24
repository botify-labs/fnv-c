import json
import os

import fnv_c

DIR = os.path.dirname(os.path.realpath(__file__))

JSON_FILE = os.path.join(DIR, "data.json")

with open(JSON_FILE) as f:
    data = json.loads(f.read())


def test_fnv0_32():
    for d in data:
        dta = d["data"].encode("utf8")
        assert fnv_c.fnv0_32(dta) == d["fnv0_32"]


def test_fnv0_64():
    for d in data:
        dta = d["data"].encode("utf8")
        assert fnv_c.fnv0_64(dta) == d["fnv0_64"]
