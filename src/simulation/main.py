from turtle import color
import numpy as np
import matplotlib.pyplot as plt
from simulation.credit import Credit as Credit
from simulation.stock import Stock as Stock, simulate_stocks
import multiprocessing as mp


if __name__ == '__main__':
    initial = 200000
    months = 25 * 12
    monte_carlo_iter = int(1e5)
    monthly_payment = 1000

    #25 Year fixed term
    credit = Credit(initial, 3.49, 736.67)
    stocks = Stock(initial, 11.05, 14.88)

    #EM 10% EU 15% WLD 75%
    final_credit_balance = credit.get_balance_due(months)
    final_portfolios = simulate_stocks(stocks, monte_carlo_iter, mp.cpu_count(), months, monthly_payment-credit.monthly_rate)
    final_value_with_cred = final_portfolios - final_credit_balance
    print("completed sim 1")
    print(np.percentile(final_value_with_cred, 5))

    #25 Year fixed term
    stocks = Stock(0, 11.05, 14.88)

    #EM 10% EU 15% WLD 75%
    final_value_without_cred = simulate_stocks(stocks, monte_carlo_iter, mp.cpu_count(), months, monthly_payment)
    print("completed sim 2")
    print(np.percentile(final_value_with_cred, 5))


    # histogram on log scale.
    # Use non-equal bin sizes, such that they look equal on log scale.
    logbins = np.logspace(5, 8, 1000)

    plt.hist(final_value_with_cred, bins=logbins, alpha=0.5, label='credit', density=True)
    plt.hist(final_value_without_cred, bins=logbins, alpha=0.5, label='no credit', density=True)
    plt.axvline(x=np.percentile(final_value_with_cred, 5), label='credit', color='r')
    plt.axvline(x=np.percentile(final_value_without_cred, 5), label='no credit', color='g')
    plt.xscale('log')
    plt.legend(loc='upper right')
    plt.show()

    # data = np.log10(final_value)

    # mu = np.mean(data)
    # sigma = np.std(data)

    

    # fig, ax = plt.subplots()

    # # the histogram of the data
    # n, bins, patches = ax.hist(data, num_bins, density=1)

    # # add a 'best fit' line
    # y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
    #     np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
    # ax.plot(bins, y, '--')
    # ax.set_xlabel('log of return')
    # ax.set_ylabel('Probability density')
    # ax.set_title(f'$\mu={mu:.2f}$, $\sigma={sigma:.2f}$')

    # # Tweak spacing to prevent clipping of ylabel
    # fig.tight_layout()
    # plt.show()
