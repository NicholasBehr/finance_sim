

class Credit:
    def __init__(self, credit_amount: float, effective_interest: float, monthly_rate: float):
        """Generic constructor of credit class

        Args:
            credit_amount (float): initial amout of money loaned
            effective_interest (float): yearly effective interest in PERCENT!
            monthly_rate (float): amount of money returned to creditor every month
        """
        self.credit_amount = credit_amount
        self.q_yearly = 1 + (effective_interest/100)
        self.q_monthly = self.q_yearly ** (1/12)
        self.monthly_rate = monthly_rate

    def get_monthly_interest(self) -> float:
        return (self.q_monthly-1) * 100


if __name__ == '__main__':
    credit = Credit(10, 1, 2)
