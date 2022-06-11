from math import nan
import numpy as np
from multiprocessing import Pool
from dataclasses import dataclass
from itertools import repeat


@dataclass
class Stock:
    def __init__(self, initial_amount: float, annual_growth_rate: float, annual_standard_deviation: float):
        self.initial_amount = initial_amount
        self.annual_growth_rate = annual_growth_rate / 100
        self.monthly_growth_rate = (1+self.annual_growth_rate)**(1/12)-1
        self.annual_standard_deviation = annual_standard_deviation / 100
        self.monthly_standard_deviation = (self.annual_standard_deviation / (1+self.annual_growth_rate)) / (12 ** (1/2))


def simulate_stocks_minibatch(stockData: Stock, batchId: int, batchSize: int, simulationDuration: int, monthlyPayment: float) -> np.array:
    final_value = np.empty([batchSize], dtype=float)
    batchDigits = np.ceil(np.log10(batchSize))
    for individualId in range(batchSize):
        value = stockData.initial_amount

        # rng with unique seed value
        rng = np.random.default_rng(seed=int(batchId * (10**batchDigits) + individualId))

        # generate random return data
        randomReturn = rng.normal(stockData.monthly_growth_rate, stockData.monthly_standard_deviation, simulationDuration)

        # simulate simulationDuration months
        for monthlyReturn in randomReturn:
            value = value * (1 + monthlyReturn) + monthlyPayment

        final_value[individualId] = value

    return final_value


def simulate_stocks(stockData: Stock, simulationSize: int, numberOfWorkrers: int, simulationDuration: int, monthlyPayment: float) -> np.array:
    # split up simulationSize equally to numberOfWorkrers
    batchSize = np.full(shape=numberOfWorkrers,
                        fill_value=np.floor(simulationSize/numberOfWorkrers),
                        dtype=int)
    for index in range(simulationSize-sum(batchSize)):
        batchSize[index] += 1

    # launch pool of workers
    processes_pool = Pool(numberOfWorkrers)
    dataZip = zip(repeat(stockData), range(numberOfWorkrers), batchSize, repeat(simulationDuration), repeat(monthlyPayment))
    data = processes_pool.starmap(simulate_stocks_minibatch, dataZip)

    # collect and return data
    processes_pool.close()
    return np.concatenate(data, axis=0)


if __name__ == '__main__':
    stocks = Stock(200000, 11.05, 14.88)
    data = simulate_stocks(stocks, 2000000, 8, 300)
    print(len(data))
    if (len(data) == len(set(data))):
        print("unique")
    else:
        print("not unique")
