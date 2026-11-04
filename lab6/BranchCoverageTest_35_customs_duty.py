import pytest
from customs_duty import duty_rate, total_duty, clearance_channel

def test_prohibited_weapons():
    with pytest.raises(ValueError):
        duty_rate("weapons", "FTA")

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

def test_unknown_category():
    assert duty_rate("furniture", "US") == 0.15

def test_negative_value():
    with pytest.raises(ValueError):
        total_duty("books", -100, "US", False)

def test_gift_within_limit():
    assert total_duty("electronics", 5000, "US", True) == 0

def test_gift_above_limit():
    assert total_duty("electronics", 10000, "US", True) == 1000

def test_non_gift_within_limit():
    assert total_duty("electronics", 1000, "US", False) == 0

def test_non_gift_above_limit():
    assert total_duty("electronics", 2000, "US", False) == 400

def test_minimum_duty_applied():
    assert total_duty("clothing", 2000, "FTA", False) == 100.0

def test_minimum_duty_not_applied_for_zero():
    assert total_duty("books", 2000, "US", False) == 0

def test_minimum_duty_not_applied_for_high_duty():
    assert total_duty("electronics", 2000, "US", False) == 400

def test_prohibited_clearance():
    assert clearance_channel(1000, "weapons", True) == "refuse"

def test_high_value_inspection():
    assert clearance_channel(100001, "electronics", True) == "inspect"

def test_value_at_inspection_limit():
    assert clearance_channel(100000, "electronics", True) == "green"

def test_missing_documents_inspection():
    assert clearance_channel(30000, "electronics", False) == "inspect"

def test_documents_present():
    assert clearance_channel(30000, "electronics", True) == "green"

def test_low_value_green():
    assert clearance_channel(20000, "electronics", False) == "green"


