import datetime

import sample_data
from statistics import parse_json


def test_parse_json():
    got = parse_json("sample.json")
    assert got == sample_data.sample


def test_get_statistics_for_delete_events():
    got = get_statistics("sample.json")
    assert got == datetime.timedelta(6, 28, 0, 0, 49, 4)
