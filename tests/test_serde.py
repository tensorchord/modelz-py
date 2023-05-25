import pytest

from modelz.serde import SerdeEnum


@pytest.mark.parametrize(
    "serde_name, data, encoded",
    [
        ("json", {"foo": "bar"}, '{"foo": "bar"}'),
        ("msgpack", {"foo": "bar"}, b"\x81\xa3foo\xa3bar"),
        ("raw", b"foobar", b"foobar"),
        ("text", "foobar", b"foobar"),
    ],
)
def test_serde(serde_name, data, encoded):
    serde_cls = getattr(SerdeEnum, serde_name).value
    serde = serde_cls()
    assert serde.encode(data) == encoded
    assert serde.decode(encoded) == data
