import pytest
from DAL.Entities.Field import Field
from DAL.Entities.Name import Name
from DAL.Entities.Phone import Phone

def test_field_equality():
    assert Field("abc") == Field("abc")
    assert Field("123") == "123"
    assert Field("abc") != Field("xyz")

def test_name_validation():
    with pytest.raises(ValueError):
        Name(None)
    with pytest.raises(TypeError):
        Name(123)
    name = Name("Roman")
    assert str(name) == "Roman"

def test_phone_validation():
    valid = Phone("1234567890")
    assert valid.value == "1234567890"
    with pytest.raises(ValueError):
        Phone("abc")
    with pytest.raises(ValueError):
        Phone("12345")
