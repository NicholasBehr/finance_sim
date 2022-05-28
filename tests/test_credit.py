import pytest
from simulation.credit import Credit as Credit

@pytest.mark.parametrize("yearly_interest,monthly_interest", [
    (1, 0.08295),
    (2, 0.16516),
    (0, 0),
    (-1, -0.08372),
])
def test_monthly_interest(yearly_interest: float, monthly_interest: float):
    test_credit = Credit(0, yearly_interest, 0)
    assert test_credit.get_monthly_interest() == pytest.approx(monthly_interest, abs=1e-5)
