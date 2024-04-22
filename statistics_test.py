import sample_data
from statistics import parse_json


def test_parse_json():
    got = parse_json("sample.json")
    assert got == sample_data.sample
