import pandas as pd 

dict_= {"a":[11,21,31], "b":[12,22,32]}
df = pd.DataFrame(dict_)

df.head()

df.mean()

from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
bitcoin_data = cg.get_coin_market_chart_by_id(id="bitcoin", vs_currency="usd", days=30)

# data = pd.DataFrame(bitcoin_price_data, columns=["Timestamp", "Price"])
# data["Date"] = pd.to_datetime(data["Timestamp"], unit="ms")

# candlestick_data = data.groupby(date.dt.date).agg({"price": ["min", "max", "first", "last"]})

# fig = go.figure(data=[go.candlestick(x= candlestick_data.index,
#                open=candlestick_data["Price"]["first"],
#                high=candlestick_data["Price"]["max"],
#                low=candlestick_data["Price"]["min"],
#                close=candlestick_data["Price"]["last"])
#                ])

# fig.update_layout(xaxis_rangeslider_visible=False, xaxis_title="Date",
# yaxis_title="Price (USD $)", title="Bitcoin Candlestick Chart Over Past 30 Days")

# plot(fig, filename="bitcoin_candlestick_graph.html")
