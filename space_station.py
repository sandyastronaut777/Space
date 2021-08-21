import pandas as pd
import plotly.express as px
url='http://api.open-notify.org/iss-now.json'
df = pd.read_json(url)
df
df['latitude'] = df.loc['latitude','iss_position']
df['longitude'] = df.loc['longitude','iss_position']
df.reset_index(inplace=True)
df
df = df.drop(['index','message'], axis = 1)
df
fig = px.scatter_geo(df,lat='latitude',lon='longitude')
fig.show()
