"""
  What is it?
  - a math method used to calculate the theoretical value of an option contract
  Uses:
    current stock prices
    the option's strike price
    expected interest rates
    time to expiration
    expected dividends
    expected volatility

  Assumptions:
    No dividends are paid out during the life of the option.
    Markets are random because market movements can't be predicted.
    There are no transaction costs in buying the option.
    The risk-free rate and volatility of the underlying asset are known and constant.
    The returns of the underlying asset are normally distributed.
    The option is European and can only be exercised at expiration.
"""
import math
from scipy.stats import norm


class BlackScholesCalculator:
    def __init__(self, s: float = 0, k: float = 0, t: float = 0, r: float = 0, vol: float = 0):
        self.s = s
        self.k = k
        self.t = t
        self.r = r
        self.vol = vol

        self.d1 = (math.log(self.s / self.k) + (self.r + 0.5 * self.vol ** 2) * self.t) / (self.vol * math.sqrt(self.t))
        self.d2 = self.d1 - (self.vol * math.sqrt(self.t))

    def call_option_price(self):
        return self.s * norm.cdf(self.d1) - self.k * math.exp(-self.r * self.t) * norm.cdf(self.d2)

    def put_option_price(self):
        return self.k * math.exp(-self.r * self.t) * norm.cdf(-self.d2) - self.s * norm.cdf(-self.d1)

# S = 45  # Underlying Price
# K = 40  # Strike Price
# T = 2   # Time to Expiration
# r = 0.1 # Risk-Free Rate
# vol = 0.1 # Volatility (σ)
