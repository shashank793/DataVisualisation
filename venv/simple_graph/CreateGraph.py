import pandas as pd

import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import dash.dependencies
from dash.dependencies import Input, Output
import plotly

#load data source

file_path = 'raphVisualisationLearning\/ConfigData.csv'

df_data = pd.read_csv(file_path)

print(df_data[['project','config']])

# print(df_data)

#Create app layout

app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H2('My Regression Data'),
    dt.DataTable(
        id='my-datatable',
        data=df_data.to_dict('records'),
        editable=False,
        row_selectable="multi",
        # filterable=True,
        # sortable=True,
        selected_rows=[0]
    ),
    html.Div(id='selected-indexes'),
    dcc.Graph(
        id='datatable-subplots'
    )
    ],style={'width' : '60%'})

@app.callback(Output('my-datatable', 'selected_rows'),
              [Input('datatable-subplots', 'clickData')])

def updated_selected_row_indices(clickData, selected_rows):
    print("Here \n")
    if clickData:
        for point in clickData['points']:
            if point['pointNumber'] in selected_rows:
                selected_rows.remove(point['pointNumber'])
            else:
                selected_rows.append(point['pointNumber'])
    return selected_rows

@app.callback(Output('datatable-subplots', 'figure'),
              [Input('my-datatable', 'data'),
               Input('my-datatable', 'selected_rows')])

def update_figure(data, selected_rows):
    dff = pd.DataFrame(data)
    fig = plotly.tools.make_subplots(
        data=3, cols=1,
        subplot_titles=('project', 'config', 'diag'),
        shared_xaxes=True)
    marker = {'color': ['#0074D9']*len(dff)}
    for i in (selected_rows or []):
        marker['color'][i] = '#FF851B'
    fig.append_trace({
        'x': dff['date'],
        'y': dff['project'],
        'type': 'bar',
        'marker': marker
    }, 1, 1)
    fig.append_trace({
        'x': dff['date'],
        'y': dff['Config'],
        'type': 'bar',
        'marker': marker
    }, 2, 1)
    fig.append_trace({
        'x': dff['date'],
        'y': dff['diag'],
        'type': 'bar',
        'marker': marker
    }, 3, 1)
    fig['layout']['showlegend'] = False
    fig['layout']['height'] = 1000
    fig['layout']['width'] = 1200
    fig['layout']['margin'] = {
        'l': 40,
        'r': 10,
        't': 60,
        'b': 200
    }
    return fig

app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})


if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=8080,debug=True)


