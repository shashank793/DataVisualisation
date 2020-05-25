import dash_core_components as dcc
import dash_html_components as html
import dash_table
from components import Header, print_button
from datetime import datetime as dt
from dash.dependencies import Input, Output
# from datetime import date, timedelta
import pandas as pd


# Read in Failure Report Data
df = pd.read_csv('data/ConfigData.csv')

available_project = df['project'].unique()
available_config = df['config'].unique()

df.rename(columns={
  'threads': 'Threads',
  'flow_name' : 'Flow Name',
  'diag' : 'Diag',
	'num_of_clones' : 'Fail Count'
  }, inplace=True)

# df['date'] = pd.to_datetime(df['date'])
df['date'] = pd.to_datetime(df['date'])
# print(df['date'])
current_year = df['date'].dt.year
df['month'] = df['date'].dt.month
# print(current_year)

dt_columns = ['Threads', 'Flow Name','Diag','Fail Count']


######################## START First Category Layout ########################
layout_conf_fail_category =  html.Div([

#    print_button(),
 
    html.Div([
        # CC Header
        Header(),
        # Drop Down menu
        # Date Picker
        html.Div([
            html.Div([
                dcc.Dropdown(
                    id='my-project-picker-list',
                    options=[{'label': proj, 'value': proj} for proj in available_project],
                    value='INSB',
                    placeholder="Select a project"
                    # value='TimbuktuMPNX',
                    # multi=True
                )
            ], style={'width': '30%', 'display': 'inline-block'}),
            html.Div([
                dcc.Dropdown(
                    id='my-config-picker-list',
                    options=[{'label': conf, 'value': conf} for conf in available_config],
                    value='Hulk_iDMA_CMED_ROB',
                    placeholder="Select a config"
                    # value='TimbuktuMPNX',
                    # multi=True
                )
            ], style={'width': '30%', 'display': 'inline-block'}),
            html.Br([]),
            dcc.DatePickerRange(
              id='my-date-picker-range-birst-category',
              # with_portal=True,
              min_date_allowed=dt(2019, 1, 1),
              max_date_allowed=df['date'].max().to_pydatetime(),
              # initial_visible_month=dt(current_year,df['date'].max().to_pydatetime().month, 1),
              initial_visible_month=dt(2019,1,1),
              start_date=(df['date'].min()),
              end_date=df['date'].max()
              # initial_visible_month=dt(current_year,df['date'].max().to_pydatetime().month, 1),
              # start_date=(df['date'].max() - timedelta(6)).to_pydatetime(),
              # end_date=df['date'].max().to_pydatetime(),
            ),
            html.Div(id='output-container-date-picker-range-birst-category'),

            ], className="row ", style={'marginTop': 30, 'marginBottom': 15}),
        # Header Bar
        html.Div([
          html.H6(["Config Level Failure Report"], className="gs-header gs-text-header padded",style={'marginTop': 15})
          ]),

        # First Data Table
        html.Div([
            dash_table.DataTable(
                id='datatable-birst-category',
                columns=[{"name": i, "id": i, 'deletable': True} for i in dt_columns],
                editable=True,
                # n_fixed_columns=2,
                style_table={'maxWidth': '1500px'},
                # row_selectable="multi",
                # selected_rows=[0],
                style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                css=[{'selector': '.dash-cell div.dash-cell-value', 'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'}]
                ),
            ], className=" twelve columns"),

        # GRAPHS
        html.Div([
            html.Div(
            id='update_graph_1'
            ),
            html.Div([
                dcc.Graph(id='birst-category'),
            ], className=" twelve columns"
            ),
            html.Div([
                dcc.Graph(id='line-graph'),
            ], className=" twelve columns"
            ),
            html.Div([
                dcc.Graph(id='diag-graph'),
            ], className=" twelve columns"
            ),
        #     html.Div(
        #         id='table-paging-with-graph-container',
        #     className="five columns"
        # )
        ], className="row "
        ),
        ], className="subpage")
    ], className="page")

######################## END First Category Layout ########################

######################## Start Second Category Layout ########################

layout_diag_fail_category = html.Div([

#    print_button(),

    html.Div([
        # CC Header
        Header(),
        # Drop Down menu
        # Date Picker
        # html.Div([
        #     html.Div([
        #         dcc.Dropdown(
        #             id='my-project-picker-list',
        #             options=[{'label': proj, 'value': proj} for proj in available_project],
        #             value='INSB',
        #             placeholder="Select a project"
        #             # value='TimbuktuMPNX',
        #             # multi=True
        #         )
        #     ], style={'width': '30%', 'display': 'inline-block'}),
        #     html.Div([
        #         dcc.Dropdown(
        #             id='my-config-picker-list',
        #             options=[{'label': conf, 'value': conf} for conf in available_config],
        #             value='Hulk_iDMA_CMED_ROB',
        #             placeholder="Select a config"
        #             # value='TimbuktuMPNX',
        #             # multi=True
        #         )
        #     ], style={'width': '30%', 'display': 'inline-block'}),
        #     html.Br([]),
        #     dcc.DatePickerRange(
        #       id='my-date-picker-range-birst-category',
        #       # with_portal=True,
        #       min_date_allowed=dt(2019, 1, 1),
        #       max_date_allowed=df['date'].max().to_pydatetime(),
        #       # initial_visible_month=dt(current_year,df['date'].max().to_pydatetime().month, 1),
        #       initial_visible_month=dt(2019,1,1),
        #       start_date=(df['date'].min()),
        #       end_date=df['date'].max()
        #       # initial_visible_month=dt(current_year,df['date'].max().to_pydatetime().month, 1),
        #       # start_date=(df['date'].max() - timedelta(6)).to_pydatetime(),
        #       # end_date=df['date'].max().to_pydatetime(),
        #     ),
        #     html.Div(id='output-container-date-picker-range-birst-category'),
        #
        #     ], className="row ", style={'marginTop': 30, 'marginBottom': 15}),
        # Header Bar
        html.Div([
          html.H6(["Config Level Failure Report"], className="gs-header gs-text-header padded",style={'marginTop': 15})
          ]),

        # First Data Table
        html.Div([
            # dash_table.DataTable(
            #     id='datatable-birst-category',
            #     columns=[{"name": i, "id": i, 'deletable': True} for i in dt_columns],
            #     editable=True,
            #     n_fixed_columns=2,
            #     style_table={'maxWidth': '1500px'},
            #     # row_selectable="multi",
            #     # selected_rows=[0],
            #     style_cell = {"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
            #     css=[{'selector': '.dash-cell div.dash-cell-value', 'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'}]
            #     ),
            dash_table.DataTable(
                id='table-paging-with-graph',
                columns=[{"name": i, "id": i, 'deletable': True} for i in dt_columns],
                page_current=0,
                page_size=20,
                page_action='custom',

                filter_action='custom',
                filter_query='',
                sort_action='custom',
                sort_mode='multi',
                sort_by=[],
                style_cell={"fontFamily": "Arial", "size": 10, 'textAlign': 'left'},
                css=[{'selector': '.dash-cell div.dash-cell-value', 'rule': 'display: inline; white-space: inherit; overflow: inherit; text-overflow: inherit;'}]
            ),
            ], className=" twelve columns"),

        # GRAPHS
        # html.Div([
        #     html.Div(
        #     id='update_graph_1'
        #     ),
        #     html.Div([
        #         dcc.Graph(id='birst-category'),
        #     ], className=" twelve columns"
        #     ),
        #     html.Div([
        #         dcc.Graph(id='line-graph'),
        #     ], className=" twelve columns"
        #     ),
        #     html.Div([
        #         dcc.Graph(id='diag-graph'),
        #     ], className=" twelve columns"
        #     ),
        # #     html.Div(
        # #         id='table-paging-with-graph-container',
        # #     className="five columns"
        # # )
        # ], className="row "
        # ),
        ], className="subpage")
    ], className="page")


######################## 404 Page ########################
noPage = html.Div([ 
    # CC Header
    Header(),
    html.P(["404 Page not found"])
    ], className="no-page")
