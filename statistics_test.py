import sample_data


def test_parse_json():
    got = parse_json("sample.json")
    assert got == sample_data.sample
