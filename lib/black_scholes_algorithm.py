import math
from scipy.stats import norm


# S - Underlying Price
# K - Strike Price
# T - Time to Expiration
# r - Risk-Free Rate
# vol - Volatility (σ)
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
