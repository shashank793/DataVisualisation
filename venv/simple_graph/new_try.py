import dash_html_components as html
import dash
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import dash_core_components as dcc
import logging


df = pd.read_csv('GraphVisualisationLearning\/data.csv')

del df['seed']

dff = df[["config","time_stamp","testcase","fail_count"]]

available_project = df['project'].unique()
available_date = df['date'].unique()
available_config = df['config'].unique()
# print(available_project)

app = dash.Dash(__name__)

PAGE_SIZE = 20

# def onLoad_date_options():



app.layout = html.Div(
    className="row",
    children=[
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='Project',
                    options=[{'label': proj, 'value': proj} for proj in available_project],
                    value=''
                    # value='TimbuktuMPNX',
                    # multi=True
                )
            ], style={'width': '30%', 'display': 'inline-block'}),
            html.Div([
                dcc.Dropdown(
                    id='Date',
                    # options=onLoad_date_options(),
                    # options=[{'label': date, 'value': date} for date in available_date],
                    # value='27/09/2018'
                    # value=''
                    # multi=True
                )
            ], style={'width': '30%', 'display': 'inline-block'}),
            html.Div([
                dcc.Dropdown(
                    id='Config',
                    # options=[{'label': config, 'value': config} for config in available_config],
                    # value='27/09/2018'
                    # value=''
                    # multi=True
                )
            ], style={'width': '30%', 'display': 'inline-block'})
        ]),
        html.Div(
            dash_table.DataTable(
                id='table-paging-with-graph',
                columns=[

                    {"name" : i, "id":i} for i in dff.columns
                ],
                page_current=0,
                page_size=20,
                page_action='custom',

                filter_action='custom',
                filter_query='',

                sort_action='custom',
                sort_mode='multi',
                sort_by=[]
            ),
            style={'height': 300, 'overflowY': 'scroll'},
            className='six columns'
        ),
        html.Div(
            id='table-paging-with-graph-container',
            className="five columns"
        )
    ]
)

operators = [['ge ', '>='],
             ['le ', '<='],
             ['lt ', '<'],
             ['gt ', '>'],
             ['ne ', '!='],
             ['eq ', '='],
             ['contains '],
             ['datestartswith ']]


def split_filter_part(filter_part):
    for operator_type in operators:
        for operator in operator_type:
            if operator in filter_part:
                name_part, value_part = filter_part.split(operator, 1)
                name = name_part[name_part.find('{') + 1: name_part.rfind('}')]

                value_part = value_part.strip()
                v0 = value_part[0]
                if (v0 == value_part[-1] and v0 in ("'", '"', '`')):
                    value = value_part[1: -1].replace('\\' + v0, v0)
                else:
                    try:
                        value = float(value_part)
                    except ValueError:
                        value = value_part

                # word operators need spaces after them in the filter string,
                # but we don't want these later
                return name, operator_type[0].strip(), value

    return [None] * 3

# Output('Date',component_property = 'options'),

@app.callback(
    Output('Date',component_property = 'options'),
    [Input('Project','value')]
)
def populate_date(proj):
    dff_proj_selected = df[df['project'] == proj]
    df_by_date = []
    # dff_date_selected = df[df['date'] == ]
    # return []

    for proj_sel in dff_proj_selected.project.unique():
        df_by_proj = dff_proj_selected[dff_proj_selected['project'] == proj_sel]
        for date_sel in df_by_proj.date.unique():
            df_by_date = dff_proj_selected['date']
            # df_by_date.append(dff_proj_selected['date'])
    # print(df_by_date)
    # return df_by_date
    return [
        {'label' : date, 'value':date}
        for date in df_by_date
    ]

@app.callback(
    Output('Config',component_property = 'options'),
    # [Input('Project','value'),
     [Input('Date','value')
     ])
def show_conf_list (date):
    # proj,
    # dff_proj_selected = df[df['project'] == proj]
    dff_date_selected = df[df['date'] == date]
    df_by_conf = []

    # for proj_sel in dff_proj_selected.project.unique():
    #     df_by_proj = dff_proj_selected[dff_proj_selected['project'] == proj_sel]
    #     for date_sel in df_by_proj.date.unique():
    #         df_by_date = dff_date_selected[dff_date_selected['date'] == date_sel]
    #         for conf_sel in df_by_date.config.unique():
    #             df_by_conf = dff_date_selected['config']
    for date_sel in dff_date_selected.date.unique():
        df_by_date = dff_date_selected[dff_date_selected['date'] == date_sel]
        for conf_sel in df_by_date.config.unique():
            df_by_conf = dff_date_selected['config']

    # print(df_by_conf)
    return [
        {'label' : conf, 'value' : conf}
        for conf in df_by_conf
    ]

@app.callback(
    Output('table-paging-with-graph', 'data'),
    [Input('Project','value'),
     Input('Date','value'),
     Input('Config','value')
])
     # Input('table-paging-with-graph', "page_current"),
     # Input('table-paging-with-graph', "page_size"),
     # Input('table-paging-with-graph', "sort_by"),
     # Input('table-paging-with-graph', "filter_query")

def update_table(proj,date,config,page_current,page_size,sort_by,filter_query):



# @app.callback(
#     Output('table-paging-with-graph', 'data'),
#     [Input('Project','value'),
#      Input('Date','value'),
#      Input('Config','value')
#     ])
# def show_date_list(proj,date,conf):
#     dff_proj_selected = df[df['project'] == proj]
#     dff_date_selected = df[df['date'] == date]
#     dff_conf_selected = df[df['config'] == conf]
#
#     print("\nDate selected : ",dff_date_selected)
#
#     for sel_project in dff_proj_selected.project.unique():
#         df_by_proj = dff_proj_selected[dff_proj_selected['project'] == sel_project]
#         print("\nHere")
#         # print(df_by_proj)
#         for sel_date in df_by_proj.date.unique():
#             # print("\nhey printing date list : ",dff_date_selected['date'])
#             # if dff_date_selected['date'] == sel_date:
#             #     print("\nTrue")
#             df_by_date = dff_date_selected[(df_by_proj['date'] == sel_date) & (df_by_proj['project'] == sel_project)]
#             # print("Printing Seleced date : ", sel_date)
#             # df_by_date = dff_date_selected[dff_date_selected['date'] == sel_date]
#             print(df_by_date)
#             for sel_config in df_by_proj.config.unique():
#                 df_by_conf = dff_conf_selected[(dff_conf_selected['config'] == sel_config) & (dff_date_selected[dff_date_selected['date']] == sel_date) & (df_by_proj['project'] == sel_project)]
#                 print(df_by_conf)
#

# @app.callback(
#     Output('table-paging-with-graph', "data"),
#     [Input('Project', "value"),
#      Input('table-paging-with-graph', "page_current"),
#      Input('table-paging-with-graph', "page_size"),
#      Input('table-paging-with-graph', "sort_by"),
#      Input('table-paging-with-graph', "filter_query")
#      ])
# def update_table(select_proj,page_size,page_current,sort_by, filter):
#     filtering_expressions = filter.split(' && ')
#
#     dff_proj = df[df['project'] == select_proj]
#
#     for filter_part in filtering_expressions:
#         col_name, operator, filter_value = split_filter_part(filter_part)
#
#         if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
#             # these operators match pandas series operator method names
#             dff_proj = dff_proj.loc[getattr(dff_proj[col_name], operator)(filter_value)]
#         elif operator == 'contains':
#             dff_proj = dff_proj.loc[dff_proj[col_name].str.contains(filter_value)]
#         elif operator == 'datestartswith':
#             # this is a simplification of the front-end filtering logic,
#             # only works with complete fields in standard format
#             dff_proj = dff_proj.loc[dff_proj[col_name].str.startswith(filter_value)]
#
#     if len(sort_by):
#         dff_proj = dff_proj.sort_values(
#             [col['column_id'] for col in sort_by],
#             ascending=[
#                 col['direction'] == 'asc'
#                 for col in sort_by
#             ],
#             inplace=False
#         )
#     return dff_proj.iloc[
#            page_current * page_size: (page_current + 1) * page_size
#            ].to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)