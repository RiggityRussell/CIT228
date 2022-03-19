from matplotlib.pyplot import legend, title
import plotly.graph_objects as go
from plotly import offline

men = [37.9,46.5,37.6,25.6]
women = [35.4,43.3,37.8,22.7]
total=[36.6,44.9,37.7,24.1]
age_range=["Over 20","20-39","40-59","Over 60"]


colors=['purple', 'green', 'black', 'yellow']

fig = go.Figure()
fig.add_trace(go.Bar(
    x =age_range,
    y=men,
    name = "Men",
    marker_color="yellow"
))
fig.add_trace(go.Bar(
    x=age_range,
    y=women,
    name="Women",
    marker_color = "purple"
))

layout=fig.update_layout(
    title="Amount of humans who eat fast food eaten every day",
    title_font_color="darkblue",
    title_font_size=40,
    xaxis_tickfont_size=14,
    yaxis= dict(
        title='Age Range',
        titlefont_size=16,
        tickfont_size=14,
    ),
    legend =dict(
        x=0,
        y=1.0,
        bgcolor='black',
        bordercolor='gray'
    ),
    barmode='group',
    bargap=0.25,
    bargroupgap=0.1
)

#fig.show()
offline.plot({'data': fig, 'layout':layout}, filename='bar.html')
# Pie Chart Example:

# labels = 'Freshwater Fish', 'Cats', 'Dogs', 'Birds'
# numPets = [142, 88.3, 74.8, 16]
# colors=['lightgreen','lightblue','lavender','lemonchiffon']
# fig = go.Figure(data=[go.Pie(labels=labels, values=numPets)])

