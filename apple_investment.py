import yfinance as yf
import matplotlib.pyplot as plt

tickers = ['AAPL', 'KO', 'AXP']

data = yf.download(tickers, period='1y')
data_close = data['Close']  # Prend la partie "Close"

data_close.plot(figsize=(10,5))
plt.title("Cours des actions principales Berkshire Hathaway (1 an)")
plt.show()
