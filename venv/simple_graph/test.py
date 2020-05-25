# standard library
# import os

# dash libs
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.figure_factory as ff
import plotly.graph_objs as go
import pandas as pd

# from sqlalchemy import create_engine
#
# # set params
# conn = create_engine(os.environ['DB_URI'])

df = pd.read_csv('GraphVisualisationLearning\/sub_demo_data.csv')

# data = []
#
# for i in range(min(len(df), 10)):
#     if (i == 0) or (i == 1):
#         continue
#     else:
#         for col in df.columns:
#             if (col == "project") or (col == "date"):
#                 continue
#             else:
#                 data.append(df.iloc[i][col])

# print(data)
# for i in range(min(len(df), 5)):
#     print("Here")
#     print(i)
#     for col in df.columns:
#         print(col[i])

# print(cols)

    # columns = [i[2]]
# print(columns)

# project
# date
# time_stamp
# sequence
# seed
# seed_count

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__,external_stylesheets = external_stylesheets)


###########################
# Data Manipulation / Model
###########################

# def fetch_data(q):
#     result = pd.read_sql(
#         sql=q,
#         con=conn
#     )
#     return result
#
#
# def get_divisions():
#     '''Returns the list of divisions that are stored in the database'''
#
#     division_query = (
#         f'''
#         SELECT DISTINCT division
#         FROM results
#         '''
#     )
#     divisions = fetch_data(division_query)
#     divisions = list(divisions['division'].sort_values(ascending=True))
#     return divisions
#
#
# def get_seasons(division):
#     '''Returns the seasons of the datbase store'''
#
#     seasons_query = (
#         f'''
#         SELECT DISTINCT season
#         FROM results
#         WHERE division='{division}'
#         '''
#     )
#     seasons = fetch_data(seasons_query)
#     seasons = list(seasons['season'].sort_values(ascending=False))
#     return seasons
#
#
# def get_teams(division, season):
#     '''Returns all teams playing in the division in the season'''
#
#     teams_query = (
#         f'''
#         SELECT DISTINCT team
#         FROM results
#         WHERE division='{division}'
#         AND season='{season}'
#         '''
#     )
#     teams = fetch_data(teams_query)
#     teams = list(teams['team'].sort_values(ascending=True))
#     return teams
#
#
# def get_match_results(division, season, team):
#     '''Returns match results for the selected prompts'''
#
#     results_query = (
#         f'''
#         SELECT date, team, opponent, goals, goals_opp, result, points
#         FROM results
#         WHERE division='{division}'
#         AND season='{season}'
#         AND team='{team}'
#         ORDER BY date ASC
#         '''
#     )
#     match_results = fetch_data(results_query)
#     return match_results
#
#
# def calculate_season_summary(results):
#     record = results.groupby(by=['result'])['team'].count()
#     summary = pd.DataFrame(
#         data={
#             'W': record['W'],
#             'L': record['L'],
#             'D': record['D'],
#             'Points': results['points'].sum()
#         },
#         columns=['W', 'D', 'L', 'Points'],
#         index=results['team'].unique(),
#     )
#     return summary
#

def draw_season_points_graph(df):
    sequence = df['testcase']
    seed_count = df['fail_count']

    figure = go.Figure(
        data=[
            go.Scatter(x=sequence, y=seed_count, mode='markers')
        ],
        layout=go.Layout(
            title='',
            showlegend=False
        )
    )

    return figure


#########################
# Dashboard Layout / View
#########################

def generate_table(dataframe, max_rows=10):
    '''Given dataframe, return template generated using Dash components
    '''
    # dataframe

    print(((df.iloc[i][col[2], col[3], col[5], col[4]]) for col in dataframe.columns) for i in range(min(len(df), max_rows)))

    data = []

    for i in range(min(len(df), max_rows)):
        if (i == 0) or (i == 1):
            continue
        else:
            for col in df.columns:
                if (col == "project") or (col == "date"):
                    continue
                else:
                    data.append(df.iloc[i][col])
    return html.Table(
        # Header
        #[html.Tr([html.Th(col) for col in dataframe.columns])]
        [html.Tr([html.Th(col[2],col[3],col[5],col[4]) for col in dataframe.columns])] +

        # Body
        # [html.Tr([
        #     html.Td(data)
        # ])]
        [html.Tr([
            html.Td(dataframe.iloc[i][col[2],col[3],col[5],col[4]]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
        # [html.Tr([
        #     html.Td(i) for i in data
        # ])]

    )


def onLoad_release_options():
    '''Actions to perform upon initial page load'''

    release_options = (
        [{'label': release, 'value': release}
         for release in df['project']]
    )
    return release_options


# Set up Dashboard and create layout
# app = dash.Dash()
# app.css.append_css({
#     "external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"
# })

app.layout = html.Div([

    # Page Header
    html.Div([
        html.H1('Post regression analysis')
    ]),

    # Dropdown Grid
    html.Div([
        html.Div([
            # Select Division Dropdown
            html.Div([
                html.Div('Select Release', className='three columns'),
                html.Div(dcc.Dropdown(id='release-selector',
                                      options=onLoad_release_options()),
                         className='nine columns')
            ]),

            # Select Season Dropdown
            html.Div([
                html.Div('Select Date', className='three columns'),
                html.Div(dcc.Dropdown(id='date-selector'),
                         className='nine columns')
            ]),

            # Select Team Dropdown
            # html.Div([
            #     html.Div('Select seed', className='three columns'),
            #     html.Div(dcc.Dropdown(id='team-selector'),
            #              className='nine columns')
            # ]),
        ], className='six columns'),

        # Empty
        html.Div(className='six columns'),
    ], className='twleve columns'),

    # Match Results Grid
    html.Div([

        # Match Results Table
        html.Div(
            html.Table(id='regression-results'),
            className='six columns'
        ),

        # Season Summary Table and Graph
        html.Div([
            # summary table
            dcc.Graph(id='date-summary'),

            # graph
            dcc.Graph(id='date-graph')
            # style={},

        ], className='six columns')
    ]),
])


#############################################
# Interaction Between Components / Controller
#############################################

# Load Seasons in Dropdown
@app.callback(
    Output(component_id='date-selector', component_property='options'),
    [
        Input(component_id='release-selector', component_property='value')
    ]
)
def populate_season_selector(release):
    dates = df['date']
    return [
        {'label': date, 'value': date}
        for date in dates
    ]


# Load Teams into dropdown
# @app.callback(
#     Output(component_id='team-selector', component_property='options'),
#     [
#         Input(component_id='division-selector', component_property='value'),
#         Input(component_id='season-selector', component_property='value')
#     ]
# )
# def populate_team_selector(division, season):
#     teams = get_teams(division, season)
#     return [
#         {'label': team, 'value': team}
#         for team in teams
#     ]
#

# Load Match results
@app.callback(
    Output(component_id='regression-results', component_property='children'),
    [
        Input(component_id='release-selector', component_property='value'),
        Input(component_id='date-selector', component_property='value')
        # Input(component_id='team-selector', component_property='value')
    ]
)
def load_regress_results(release, date):
    # results = get_match_results(division, season, team)
    return generate_table(df, max_rows=50)


# Update Season Summary Table
# @app.callback(
#     Output(component_id='date-summary', component_property='figure'),
#     [
#         Input(component_id='release-selector', component_property='value'),
#         Input(component_id='date-selector', component_property='value')
#         # Input(component_id='team-selector', component_property='value')
#     ]
# )
# def load_date_summary(release, date):
#     # results = get_match_results(division, season, team)
#     results = df
#     table = []
#     if len(results) > 0:
#         summary = calculate_season_summary(results)
#         table = ff.create_table(summary)
#
#     return table


# Update Season Point Graph
@app.callback(
    Output(component_id='date-graph', component_property='figure'),
    [
        Input(component_id='release-selector', component_property='value'),
        Input(component_id='date-selector', component_property='value')
        # Input(component_id='team-selector', component_property='value')
    ]
)
def load_season_points_graph(release, date):
    # results = get_match_results(division, season, team)
    results = df

    figure = []
    if len(results) > 0:
        figure = draw_season_points_graph(results)

    return figure


# start Flask server
if __name__ == '__main__':
    app.run_server( debug=True , port= '8081')