# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from reader import read_data

app = dash.Dash()

x, y, avg_x, avg_y = read_data()

my_css_url = "https://cdnjs.cloudflare.com/ajax/libs/bulma/0.6.2/css/bulma.min.css"
app.css.append_css({"external_url": my_css_url})

app.layout = html.Div(
    children=[
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [html.H1("Resting Heart Rate", className="title")],
                            className="container",
                        )
                    ],
                    className="hero-body",
                )
            ],
            className="hero is-danger",
        ),
        html.Div(
            [
                dcc.Graph(
                    id="graph",
                    figure=go.Figure(
                        data=[
                            go.Scatter(
                                x=x,
                                y=y,
                                line=dict(shape="linear", color="#FF6382"),
                                fillcolor="#FF95AA",
                                hoverinfo="x+y",
                                hoverlabel=dict(bgcolor="#333", font=dict(size=18)),
                                fill="tozeroy",
                                name="HR"
                                ),
                                go.Scatter(
                                    x=avg_x,
                                    y=avg_y,
                                    hoverinfo='y',
                                    hoverlabel=dict(bgcolor='#333',font=dict(size=18)),
                                    line=dict(shape="spline", color="#b32945"),
                                    name='Average'
                            )
                        ],
                        layout=dict(
                            autosize=True,
                            margin=go.Margin(l=35, r=20, b=0, t=20, pad=4),
                            yaxis=dict(range=[30, 60]),
                            xaxis=dict(
                                rangeslider=dict(),
                                type="date",
                                showspikes=True,
                                spikemode="toaxis",
                                spikethickness=2,
                                spikedash="solid",
                            ),
                        ),
                    ),
                    style=dict(height="78vh"),
                )
            ],
            className="section",
        ),  # ,
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
