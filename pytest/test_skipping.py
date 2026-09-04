# ==============================================================================
#  Organization : TINITIATE TECHNOLOGIES PVT LTD
#  Website      : tinitiate.com
#  Script Title : Python Tutorial
#  Description  : Skipping Test
#  Author       : Team Tinitiate
# ==============================================================================



import pytest
from calculator import multiply, add, subtract

# Test multiply function
def test_multiply():
    result = multiply(2, 3)
    assert result == 6

# Test add function
def test_add():
    result = add(5, 7)
    assert result == 12

# Test subtract function (skipped intentionally)
@pytest.mark.skip(reason="Not implemented yet")
def test_subtract():
    result = subtract(10, 3)
    assert result == 7

# Run pytest
if __name__ == "__main__":
    pytest.main()
