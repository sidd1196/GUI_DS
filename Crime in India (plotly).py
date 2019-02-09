import pandas as pd

import plotly.graph_objs as go
import plotly.offline as ply
import matplotlib.pyplot as plt

# Data
data = pd.read_csv('01_District_wise_crimes_committed_IPC_2001_2012.csv')

df_u = pd.DataFrame(data) # unsorted data
print(df_u.head())
df = df_u.sort_values(['MURDER'])


total = df.loc[(df.STATE_UT == 'ASSAM'),['STATE_UT','DISTRICT','YEAR','MURDER']]

I = df.loc[( df.DISTRICT == 'TOTAL') & (df.YEAR == 2011),: ]
J = df.loc[( df.DISTRICT == 'TOTAL') & (df.YEAR == 2012),: ]

print(I.head())

# 1st Plot
#         By Siddharth Pathania
## Plotly steps begin
# Create Traces - data collections

trace1 = go.Bar(x = I['STATE_UT'],
                y = I['MURDER'],
                name = 'Murder in 2011')


trace2 = go.Bar(x = J['STATE_UT'],
                y = J['MURDER'],
                name = 'Murder in 2012')
# Create information  / layout dictionary
layout = dict(
        title = 'Murder in India in 2012',
        xaxis = dict(title = 'States'),
        yaxis = dict(title = 'No. of people')
        )

# Pack the data

data = [trace1,trace2]

# Create a figure
fig = dict(data = data ,layout = layout)


#Plot 
ply.plot(fig,filename = 'Murder in India StateWise in 2012.html')



# 2 Plot

total = df_u.loc[(df_u.STATE_UT == 'PUNJAB') & ( df_u.DISTRICT == 'TOTAL'),
               ['STATE_UT','DISTRICT','YEAR','MURDER','RAPE']]

trace1 = go.Scatter(x = total['YEAR'],
                y = total['MURDER'],
                name = 'Murder in Punjab year wise'
                )

trace2 = go.Scatter(x = total['YEAR'],
                y = total['RAPE'],
                name = 'Rape in Punjab year wise')

layout = dict(
        title = 'Murder and Rape in Punjab',
        xaxis = dict(title = 'Year'),
        yaxis = dict(title = 'No. of people')
        )

data = [trace1,trace2]

fig = dict(data = data ,layout = layout)

ply.plot(fig , filename='Murder and Rape in Punjab year wise.html')

























