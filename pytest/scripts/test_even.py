# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Parametrized Testing
#  Author       : Team Tinitiate
# ==============================================================================



import pytest

def is_even(number):
    return number % 2 == 0

@pytest.mark.parametrize("number, expected", [(2, True), (3, False), (0, True)])
def test_is_even(number, expected):
    assert is_even(number) == expected
