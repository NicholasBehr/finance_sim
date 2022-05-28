import pytest
from simulation.credit import Credit as Credit

@pytest.mark.parametrize("yearly_interest, monthly_interest", [
    (1, 0.08295),
    (2, 0.16516),
    (0, 0),
    (-1, -0.08372),
])
def test_monthly_interest(yearly_interest: float, monthly_interest: float):
    test_credit = Credit(0, yearly_interest, 0)
    assert test_credit.get_monthly_interest() == pytest.approx(monthly_interest, abs=1e-5)

@pytest.mark.parametrize("monthly_rate, balance_due_afer_25_years", [
    (42.3, -1.02),
    (10, 12527.32),
    (100, -22381.37),
    (0, 16406.06),
])
def test_balance_due(monthly_rate: float, balance_due_afer_25_years: float):
    test_credit = Credit(10000, 2, monthly_rate)
    assert test_credit.get_balance_due(25*12) == pytest.approx(balance_due_afer_25_years, rel=1e-2)
