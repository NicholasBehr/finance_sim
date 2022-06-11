import pytest
from simulation.stock import Stock as Stock


@pytest.mark.parametrize("annual_growth_rate, balance_afer_25_years", [
    (-2, 29608.67),
    (0, 40000),
    (4, 77549.66),
    (10, 231772.62),
])
def test_growth(annual_growth_rate: float, balance_afer_25_years: float):
    test_credit = Stock(10000, annual_growth_rate, 0)
    out = test_credit.simulate(1, 25*12, 100)
    assert out[0] == pytest.approx(balance_afer_25_years, rel=1e-3)
