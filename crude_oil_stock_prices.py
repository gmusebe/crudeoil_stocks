# set environment
import pandas as pd
import datetime as dt
from datetime import date
import plotly.express as px
import plotly.graph_objects as go
from datawrapper import Datawrapper
import pandas_datareader.data as web
from pandas_datareader import data as pdr

# Data
# data from a date to today:
# date today:
today = date.today()

cl_f = pdr.get_data_yahoo("CL=F", start="2018-01-01", end=today)


# visualize Data:
candlestick = go.Figure(data = [go.Candlestick(x = cl_f.index, 
                                               open = cl_f['Open'], 
                                               high = cl_f['High'], 
                                               low = cl_f['Low'], 
                                               close = cl_f['Close']
                                              )])

candlestick.update_layout(xaxis_rangeslider_visible = False, title = 'CRUDE OIL SHARE PRICE (2018- TO DATE)')
candlestick.update_xaxes(title_text = 'Date')
candlestick.update_yaxes(title_text = 'CL=F Close Price', tickprefix = '$')

candlestick.show()


# Visualize using data wrapper
ACCESS_TOKEN = "rO55d4knYpI8dAB0iWKNSsAROImURi0NuK0NDf9YmHCkMsNuRCPB8hAI5L35eFmH" # Datawrapper API token
dw = Datawrapper(access_token = ACCESS_TOKEN)

chart_info = dw.create_chart(
  title = 'Crude Oil Stock PrIces',
  chart_type = 'd3-lines',
  data = cl_f)


# Display & Publish
dw.publish_chart(chart_id = chart_info['id'])

# View in Datawrapper dashboard