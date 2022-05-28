

class Credit:
    def __init__(self, credit_amount: float, effective_interest: float, monthly_rate: float):
        """Generic constructor of credit class

        Args:
            credit_amount (float): initial amout of money loaned
            effective_interest (float): yearly EFFECTIVE INTEREST in PERCENT! 2% -> 2\n
            The effective interest rate is higher than the nominal interest rate because it takes into account that your 
            installments are not annual, but monthly. Interest is thus accrued over the course of the year. 
            The effective interest rate is the interest that you actually pay.
            monthly_rate (float): amount of money returned to creditor at the end of every month (in arrears)
        """
        self.credit_amount = credit_amount
        self.q_yearly = 1 + (effective_interest/100)
        self.q_monthly = self.q_yearly ** (1/12)
        self.monthly_rate = monthly_rate

    def get_monthly_interest(self) -> float:
        return (self.q_monthly - 1) * 100

    def get_balance_due(self, after_n_months: int) -> float:
        """ remaining balace due, after paying n months in arrears \n
        balance_due_0 \t= credit_amount \n
        balance_due_1 \t= credit_amount * q_monthly - monthly_rate \n
        balance_due_2 \t= (credit_amount * q_monthly - monthly_rate) * q_monthly - monthly_rate \n
                      \t= credit_amount * q_monthly^2 - monthly_rate * (q_monthly^2 + q_monthly^1 + q_monthly^0) \n

        Args:
            after_n_months (int): after how many months?

        Returns:
            float: remaining balance due
        """
        interest = self.credit_amount * (self.q_monthly ** after_n_months)
        paid = self.monthly_rate * (1 - (self.q_monthly ** after_n_months)) / (1 - self.q_monthly)
        return interest - paid


if __name__ == '__main__':
    credit = Credit(10000, 2, 20)
    print("remaining", credit.get_balance_due(300))
