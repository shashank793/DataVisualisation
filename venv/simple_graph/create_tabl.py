import dash_html_components as html
import dash
from dash.dependencies import Input, Output
import dash_table
import pandas as pd
import dash_core_components as dcc


df = pd.read_csv('GraphVisualizationLearning\/data.csv')
# print(df['seed'][2])
# print(df['seed'])
del df['seed']
# df = df.dropna()
dff = df[["Config","time_stamp","testcase","fail_count"]]

# print(dff)
# print(df.columns[0])

available_project = df['project'].unique()
available_date = df['date'].unique()
available_config = df['Config'].unique()
print(available_project)

app = dash.Dash(__name__)

PAGE_SIZE = 20

# app.layout = dash_table.DataTable(
#     id='datatable-paging',
#     columns=[
#         {"name": i, "id": i} for i in df.columns
#     ],
#     page_current=0,
#     page_size=PAGE_SIZE,
#     page_action='custom'
# )
#
#
# @app.callback(
#     Output('datatable-paging', 'data'),
#     [Input('datatable-paging', "page_current"),
#      Input('datatable-paging', "page_size")])
# def update_table(page_current,page_size):
#     return df.iloc[
#         page_current*page_size:(page_current+ 1)*page_size
#     ].to_dict('records')
#
# app.layout = dash_table.DataTable(
#     id='table-multicol-sorting',
#     columns=[
#         {"name": i, "id": i} for i in df.columns
#     ],
#     page_current=0,
#     page_size=PAGE_SIZE,
#     page_action='custom',
#
#     sort_action='custom',
#     sort_mode='multi',
#     sort_by=[]
# )
#
# @app.callback(
#     Output('table-multicol-sorting', "data"),
#     [Input('table-multicol-sorting', "page_current"),
#      Input('table-multicol-sorting', "page_size"),
#      Input('table-multicol-sorting', "sort_by")])
# def update_table(page_current, page_size, sort_by):
#     # print(sort_by)
#     if len(sort_by):
#         dff = df.sort_values(
#             [col['column_id'] for col in sort_by],
#             ascending=[
#                 col['direction'] == 'asc'
#                 for col in sort_by
#             ],
#             inplace=False
#         )
#     else:
#         # No sort is applied
#         dff = df
#
#     return dff.iloc[
#         page_current*page_size:(page_current+ 1)*page_size
#     ].to_dict('records')


app.layout = html.Div(
    # html.Div([
    #     html.H1('Post regression analysis')
    # ]),

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
                    options=[{'label': date, 'value': date} for date in available_date],
                    # value='27/09/2018'
                    value=''
                    # multi=True
                )
            ], style={'width': '30%', 'display': 'inline-block'}),
            html.Div([
                dcc.Dropdown(
                    id='Config',
                    options=[{'label': config, 'value': config} for config in available_config],
                    # value='27/09/2018'
                    value=''
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


@app.callback(
    Output('table-paging-with-graph', "data"),
    [Input('Project', "value"),
     Input('table-paging-with-graph', "page_current"),
     Input('table-paging-with-graph', "page_size"),
     Input('table-paging-with-graph', "sort_by"),
     Input('table-paging-with-graph', "filter_query")
     ])
def update_table(select_proj,page_size,page_current,sort_by, filter):
    filtering_expressions = filter.split(' && ')

    dff_proj = df[df['project'] == select_proj]

    for filter_part in filtering_expressions:
        col_name, operator, filter_value = split_filter_part(filter_part)

        if operator in ('eq', 'ne', 'lt', 'le', 'gt', 'ge'):
            # these operators match pandas series operator method names
            dff_proj = dff_proj.loc[getattr(dff_proj[col_name], operator)(filter_value)]
        elif operator == 'contains':
            dff_proj = dff_proj.loc[dff_proj[col_name].str.contains(filter_value)]
        elif operator == 'datestartswith':
            # this is a simplification of the front-end filtering logic,
            # only works with complete fields in standard format
            dff_proj = dff_proj.loc[dff_proj[col_name].str.startswith(filter_value)]

    if len(sort_by):
        dff_proj = dff_proj.sort_values(
            [col['column_id'] for col in sort_by],
            ascending=[
                col['direction'] == 'asc'
                for col in sort_by
            ],
            inplace=False
        )
    return dff_proj.iloc[
           page_current * page_size: (page_current + 1) * page_size
           ].to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)