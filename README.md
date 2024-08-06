Black Scholes

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
  
Configuring:
use 'pip install' to get dependencies in files

dependencies:
```
pip install numpy
pip install scipy
pip install matplotlib
pip install pyqt6
```

Run blackScholesGUI.py
