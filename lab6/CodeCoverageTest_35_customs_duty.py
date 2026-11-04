import pytest
from customs_duty import duty_rate, total_duty, clearance_channel

def test_prohibited_weapons():
    with pytest.raises(ValueError):
        duty_rate("weapons", "US")

def test_prohibited_narcotics():
    with pytest.raises(ValueError):
        duty_rate("narcotics", "US")

def test_electronics_fta():
    assert duty_rate("electronics", "FTA") == 0.10

def test_electronics_non_fta():
    assert duty_rate("electronics", "US") == 0.20

def test_clothing_fta():
    assert duty_rate("clothing", "FTA") == 0.05

def test_clothing_non_fta():
    assert duty_rate("clothing", "US") == 0.12

def test_books():
    assert duty_rate("books", "US") == 0

def test_other_category():
    assert duty_rate("furniture", "US") == 0.15

def test_negative_value():
    with pytest.raises(ValueError):
        total_duty("books", -100, "US", False)

def test_gift_below_limit():
    assert total_duty("electronics", 3000, "US", True) == 0

def test_gift_above_limit():
    assert total_duty("electronics", 10000, "US", True) == 1000

def test_non_gift_below_limit():
    assert total_duty("electronics", 500, "US", False) == 0

def test_minimum_duty():
    assert total_duty("clothing", 1001, "FTA", False) == pytest.approx(50.05)

def test_normal_duty():
    assert total_duty("electronics", 2000, "US", False) == 400

def test_prohibited_clearance():
    assert clearance_channel(1000, "weapons", True) == "refuse"

def test_high_value_inspection():
    assert clearance_channel(150000, "electronics", True) == "inspect"

def test_missing_documents_inspection():
    assert clearance_channel(30000, "electronics", False) == "inspect"

def test_green_clearance():
    assert clearance_channel(10000, "electronics", True) == "green"


