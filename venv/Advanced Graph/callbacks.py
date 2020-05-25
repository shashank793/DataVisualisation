from dash.dependencies import Input, Output
from app import app

from datetime import datetime as dt
from datetime import date, timedelta
from datetime import datetime
import plotly.graph_objs as go
import dash_html_components as html
import dash_core_components as dcc
import numpy as np
import pandas as pd

from components import update_first_datatable, update_graph


pd.options.mode.chained_assignment = None


df = pd.read_csv('data/ConfigData.csv')
# dff = df.groupby(['project','date','config','threads','num_of_clones']).sum()
dff = df
# dfff = df

del dff['threads']
del dff['flow_name']
del dff['diag']

dff['Fail Count'] = dff.groupby(['project','date','config'])['num_of_clones'].transform(np.sum)
del dff['num_of_clones']

# print(dff)

dff = dff.drop_duplicates(subset=['date','config'])

# print(dff)

# dff.groupby()
# dff.assign(Total=dff.groupby(['project','date','config']).num_of_clones.transform('sum'))


#[['INSB', '24/05/2019', 'Hulk_iDMA_CMED_ROB', 1],
#['INSB', '24/05/2019', 'Hulk_iDMA_CMED_ROB', 1],
#['INSB', '24/05/2019', 'Hulk_iDMA_CMED_ROB', 1], ['INSB', '24/05/2019', 'Hulk_iDMA_CMED_ROB', 1], ['INSB', '24/05/2019', 'Hulk_iDMA_CMED_ROB', 2], ['INSB', '24/05/2019', 'Hulk_iDMA_CMED_ROB', 2], ['INSB', '24/05/2019', 'Hulk_iDMA_CMED_ROB', 1], ['INSB', '24/05/2019', 'Hulk_iDMA_CMED_ROB', 2], ['INSB', '24/05/2019', 'Hulk_iDMA_CMED_ROB', 1], ['INSB', '24/05/2019', 'Hulk_iDMA_CMED_ROB', 2], ['INSB', '24/05/2019', 'Hulk_iDMA_CMED_ROB', 1], ['INSB', '24/05/2019', 'Hulk_iDMA_CMED_ROB', 1], ['INSB', '24/05/2019', 'Frodo_VisionQ7_max', 2], ['INSB', '24/05/2019', 'Frodo_VisionQ7_max', 1], ['INSB', '24/05/2019', 'Frodo_VisionQ7_max', 3], ['INSB', '24/05/2019', 'Frodo_VisionQ7_max', 2], ['INSB', '24/05/2019', 'Frodo_VisionQ7_max', 1], ['INSB', '24/05/2019', 'Elektra_1LSU', 1], ['INSB', '25/05/2019', 'Intel_VisionQ7_5Mar2019', 1], ['INSB', '25/05/2019', 'Intel_VisionQ7_5Mar2019', 3], ['INSB', '25/05/2019', 'Intel_VisionQ7_5Mar2019', 1], ['INSB', '25/05/2019', 'Intel_VisionQ7_5Mar2019', 3], ['INSB', '25/05/2019', 'Intel_VisionQ7_5Mar2019', 1], ['INSB', '25/05/2019', 'Intel_VisionQ7_5Mar2019', 1], ['INSB', '25/05/2019', 'Intel_VisionQ7_5Mar2019', 1], ['INSB', '25/05/2019', 'Intel_VisionQ7_5Mar2019', 1], ['INSB', '25/05/2019', 'Intel_VisionQ7_5Mar2019', 1], ['INSB', '25/05/2019', 'Intel_VisionQ7_5Mar2019', 1], ['INSB', '25/05/2019', 'BBN32_NX_IDMA', 1], ['INSB', '25/05/2019', 'BBN32_NX_IDMA', 1], ['INSB', '25/05/2019', 'BBN32_NX_IDMA', 1], ['INSB', '25/05/2019', 'BBN32_NX_IDMA', 1], ['INSB', '25/05/2019', 'BBN32_NX_IDMA', 1], ['INSB', '3/7/2019', 'Frodo_VisionQ7_max', 1], ['INSB', '3/7/2019', 'Frodo_VisionQ7_max', 3], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 2], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 2], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '3/7/2019', 'Hulk_iDMA_CMED_rst_pins', 13], ['INSB', '20/08/2019', 'Frodo_VisionQ7_max', 1], ['INSB', '20/08/2019', 'Frodo_VisionQ7_max', 1], ['INSB', '20/08/2019', 'Frodo_VisionQ7_max', 1], ['INSB', '20/08/2019', 'Frodo_VisionQ7_max', 3], ['INSB', '20/08/2019', 'Hulk_iDMA_CMED_rst_pins', 2], ['INSB', '20/08/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '20/08/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '20/08/2019', 'Hulk_iDMA_CMED_rst_pins', 3], ['INSB', '20/08/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '20/08/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '20/08/2019', 'Hulk_iDMA_CMED_rst_pins', 1], ['INSB', '20/08/2019', 'Hulk_iDMA_CMED_rst_pins', 2], ['INSB', '22/08/2019', 'Frodo_VisionQ7_max', 1], ['INSB', '22/08/2019', 'Frodo_VisionQ7_max', 2], ['INSB', '22/08/2019', 'Frodo_VisionQ7_max', 1], ['INSB', '22/08/2019', 'Frodo_VisionQ7_max', 2], ['INSB', '22/08/2019', 'Hulk_iDMA_CMED_rst_pins', 3], ['INSB', '22/08/2019', 'Hulk_iDMA_CMED_rst_pins', 5], ['INSB', '22/08/2019', 'Hulk_iDMA_CMED_rst_pins', 2]]


available_project = df['project'].unique()
# available_date = df['date'].unique()
available_config = df['config'].unique()

df.rename(columns={
  'threads': 'Threads',
  'flow_name' : 'Flow Name',
  'diag' : 'Diag',
  'num_of_clones' : 'Fail Count'
  }, inplace=True)


df['date'] = pd.to_datetime(df['date'])
dff['date'] = pd.to_datetime(dff['date'])
# current_year = df['date'].dt.year
# df['month'] = df['date'].dt.month
# current_week = df[df['year'] == current_year]['Week'].max()

now = datetime.now()
datestamp = now.strftime("%Y%m%d")


#### Date Picker Callback
@app.callback(Output('output-container-date-picker-range-birst-category', 'children'),
	[Input('my-date-picker-range-birst-category', 'start_date'),
	 Input('my-date-picker-range-birst-category', 'end_date')])
def update_output(start_date, end_date):
	string_prefix = 'You have selected '
	if start_date is not None:
		start_date = dt.strptime(start_date, '%Y-%m-%d')
		start_date_string = start_date.strftime('%B %d, %Y')
		string_prefix = string_prefix + 'a Start Date of ' + start_date_string + ' | '
	if end_date is not None:
		end_date = dt.strptime(end_date, '%Y-%m-%d')
		end_date_string = end_date.strftime('%B %d, %Y')
		days_selected = (end_date - start_date).days
		prior_start_date = start_date - timedelta(days_selected + 1)
		prior_start_date_string = datetime.strftime(prior_start_date, '%B %d, %Y')
		prior_end_date = end_date - timedelta(days_selected + 1)
		prior_end_date_string = datetime.strftime(prior_end_date, '%B %d, %Y')
		string_prefix = string_prefix + 'End Date of ' + end_date_string + ', for a total of ' + str(days_selected + 1) + ' Days. The prior period Start Date was ' + \
		prior_start_date_string + ' | End Date: ' + prior_end_date_string + '.'
	if len(string_prefix) == len('You have selected: '):
		return 'Select a date to see it displayed here'
	else:
		return string_prefix

# Callback and update first data table
@app.callback(Output('datatable-birst-category', 'data'),
	[Input('my-project-picker-list','value'),
	 Input('my-config-picker-list','value'),
	 Input('my-date-picker-range-birst-category', 'start_date'),
	 Input('my-date-picker-range-birst-category', 'end_date')])
def update_data_1(proj,conf,start_date, end_date):
	data_1 = update_first_datatable(proj,conf,start_date, end_date)
	return data_1


# Callback for the Graphs
# Shashank Come back here
# @app.callback(
#    Output('birst-category', 'figure'),
#    [Input('datatable-birst-category', "selected_rows"),
#    Input('my-date-picker-range-birst-category', 'end_date')])
# def update_birst_category(selected_rows, end_date):
# 	travel_product = []
# 	travel_product_list = sorted(df['Birst Category'].unique().tolist())
# 	for i in selected_rows:
# 		travel_product.append(travel_product_list[i])
# 		# Filter by specific product
# 	filtered_df = df[(df['Birst Category'].isin(travel_product))].groupby(['Year', 'Week']).sum()[['Spend TY', 'Spend LY', 'Sessions - TY', 'Sessions - LY', 'Bookings - TY', 'Bookings - LY', 'Revenue - TY', 'Revenue - LY']].reset_index()
# 	fig = update_graph(filtered_df, end_date)
# 	return fig


@app.callback(
   Output('birst-category', 'figure'),
	[Input('my-project-picker-list', 'value'),
	 Input('my-config-picker-list','value'),
	 Input('my-date-picker-range-birst-category', 'start_date'),
	 Input('my-date-picker-range-birst-category', 'end_date')
	])
def update_birst_category(proj,conf,start_date, end_date):

	traces = []
	if start_date is not None:
		start_date = dt.strptime(start_date,'%Y-%m-%d')
		start_date_string = start_date.strftime('%Y-%m-%d')
	if end_date is not None:
		end_date = dt.strptime(end_date,'%Y-%m-%d')
		end_date_string = end_date.strftime('%Y-%m-%d')
	# df_date_selected = df[(df['date'] >= start_date_string) & (df['date'] <= end_date_string)]
	df_date_selected = dff[(dff['date'] >= start_date_string) & (dff['date'] <= end_date_string)]
	df_proj_selected = dff[(dff['project'] == proj)]

	df_conf_selected = dff[dff['config'] == conf]

	for sel_proj in df_proj_selected.project.unique():
		df_by_proj = df_proj_selected[df_proj_selected['project'] == sel_proj]
		for sel_conf in df_by_proj.config.unique():
			df_by_conf = df_conf_selected[(df_conf_selected['config'] == sel_conf) & (df_by_proj['project'] == sel_proj) & (df_date_selected['config'] == sel_conf)]
			if df_by_conf.empty == True:
				pass
			else:
				traces.append(go.Bar(
					x=df_by_conf['date'],
					y=df_by_conf['Fail Count'],
					text=df_by_conf['config'],
					# mode='lines',
					opacity=0.5,
					# marker={'size': 10, 'line': {'width': 0.5, 'color': 'white'}},
					name=sel_conf
				))
				return {
					'data': traces,
					'layout': go.Layout(
						title=f"Per Config Total Failure",
						xaxis={"title": "Diag"}, yaxis={"title": f"Failure Count"},
						colorway=["#C7037A", "#E20048", "#FFCB00", "#FF7C00", "#2F9609",
								  "#0E4770", "#A8AE0B"]
					)
				}

@app.callback(
   Output('line-graph', 'figure'),
	[Input('my-project-picker-list', 'value'),
	 Input('my-config-picker-list','value'),
	 Input('my-date-picker-range-birst-category', 'start_date'),
	 Input('my-date-picker-range-birst-category', 'end_date')
	])
def update_line_graph(proj,conf,start_date, end_date):
	line_data = update_graph(proj,conf,start_date,end_date)
	return line_data

	# for i in df_proj_selected.project:
	# 	dff_proj_selected = df_proj_selected[(df_proj_selected['project'] == i) & (df_date_selected['project'] == i) ]
	# 	if dff_proj_selected.empty == True:
	# 		pass
	# 	else:
	# 		# print("\n\nIn graph\n\n",dff_proj_selected['date'])
	# 		traces.append(go.Scatter(
	# 			x=dff_proj_selected['date'],
	# 			y=dff_proj_selected['Failure Count'],
	# 			# text=dff_proj_selected['project'],
	# 			mode='lines',
	# 			opacity=0.5,
	# 			marker={'size': 10, 'line': {'width': 0.5, 'color': 'white'}},
	# 			name=i
	# 		))
	# 		return {
	# 			'data': traces,
	# 			'layout': go.Layout(
	# 				title=f"Regression Status",
	# 				xaxis={"title": "Date"}, yaxis={"title": f"Failure Count"},
	# 				colorway=["#C7037A", "#E20048", "#FFCB00", "#FF7C00", "#2F9609",
	# 						  "#0E4770", "#A8AE0B"]
	# 			)
	# 		}

