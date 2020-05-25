from datetime import datetime as dt
from datetime import date, timedelta
from datetime import datetime
import plotly.graph_objs as go
from plotly import tools
import numpy as np
import pandas as pd

# pd.options.mode.chained_assignment = None

df = pd.read_csv('data/ConfigData.csv')
# df = df.dropna()
# del df['seed']


df.rename(columns={
  'threads': 'Threads',
  'flow_name' : 'Flow Name',
  'diag' : 'Diag',
	'num_of_clones' : 'Fail Count'
  }, inplace=True)



df['date'] = pd.to_datetime(df['date'])
current_year = df['date'].dt.year.max()
df['year'] = df['date'].dt.year

now = datetime.now()
datestamp = now.strftime("%Y%m%d")

columns = ['Threads', 'Flow Name','Diag','Fail Count']


# First Data Table Update Function

def update_first_datatable(proj,conf,start_date, end_date):
	if start_date is not None:
		start_date = dt.strptime(start_date, '%Y-%m-%d')
		start_date_string = start_date.strftime('%Y-%m-%d')
	if end_date is not None:
		end_date = dt.strptime(end_date, '%Y-%m-%d')
		end_date_string = end_date.strftime('%Y-%m-%d')
	days_selected = (end_date - start_date).days

	prior_start_date = start_date - timedelta(days_selected + 1)
	prior_start_date_string = datetime.strftime(prior_start_date, '%Y-%m-%d')
	prior_end_date = end_date - timedelta(days_selected + 1)
	prior_end_date_string = datetime.strftime(prior_end_date, '%Y-%m-%d')
	dff_date_selected = df[(df['date'] >= start_date) & (df['date'] <= end_date)]

	dff_proj_selected = df[(df['project'] == proj)]
	dff_conf_selected = df[(df['config'] == conf)]

	for sel_proj in dff_proj_selected.project.unique():
		df_by_proj = dff_proj_selected[dff_proj_selected['project'] == sel_proj]
		for sel_conf in df_by_proj.config.unique():
			df_by_conf = dff_conf_selected[(dff_conf_selected['config'] == sel_conf) & (df_by_proj['project'] == sel_proj) & (dff_date_selected['config'] == sel_conf)]
			# print("\n\nIn Printing config\n\n",df_by_conf)
			if df_by_conf.empty == True:
				pass
			else:
				df_by_date_combined_dt = df_by_conf[[
					'Threads',
					'Flow Name',
					'Diag',
					'Fail Count'
				]]

				data_df = df_by_date_combined_dt.to_dict("rows")
				return data_df


		# dff_proj_selected = df_proj_selected[(df_proj_selected['project'] == sel_proj) & (df_date_selected['project'] == sel_proj)]
	# print("\nHey Hey Shashank\n",df_by_conf)
	# Rearrange the columns
	# df_by_date_combined_dt = df_by_conf[[
	# 	'Threads',
	# 	'Flow Name',
	# 	'Diag',
	# 	'Fail Count'
	# 	 ]]

	# print(df_by_date_combined_dt)
	# df_by_date_combined_dt = df_by_conf[[
	# 	'Threads',
	# 	'Flow Name',
	# 	'Diag',
	# 	'Fail Count'
	# ]]
	# data_df = df_by_date_combined_dt.to_dict("rows")
	# return data_df

######################## FOR GRAPHS  ########################

# def update_graph(proj,start_date, end_date):
# 	traces = []
# 	if start_date is not None:
# 		start_date = dt.strptime(start_date, '%Y-%m-%d')
# 		start_date_string = start_date.strftime('%Y-%m-%d')
# 	if end_date is not None:
# 		end_date = dt.strptime(end_date, '%Y-%m-%d')
# 		end_date_string = end_date.strftime('%Y-%m-%d')
# 	days_selected = (end_date - start_date).days
#
# 	prior_start_date = start_date - timedelta(days_selected + 1)
# 	prior_start_date_string = datetime.strftime(prior_start_date, '%Y-%m-%d')
# 	prior_end_date = end_date - timedelta(days_selected + 1)
# 	prior_end_date_string = datetime.strftime(prior_end_date, '%Y-%m-%d')
# 	df_date_selected = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
# 	# print("\n\nDate Selected",dff_date_selected)
# 	df_proj_selected = df[(df['project'] == proj)]
#
# 	for i in df_proj_selected.project:
# 		dff_proj_selected = df_proj_selected[(df_proj_selected['project'] == i) & (df_date_selected['project'] == i)]
# 		if dff_proj_selected.empty == True:
# 			pass
# 		else:
# 			traces.append(go.Scatter(
# 				x = dff_proj_selected['date'],
# 				y = dff_proj_selected['fail_count'],
# 				text = dff_proj_selected['project'],
# 				mode = 'lines',
# 				opacity=0.5,
# 				marker={'size': 10, 'line': {'width': 0.5, 'color': 'white'}},
# 				name = i
# 			))
# 			return {
# 				'data' : traces,
# 				'layout' : go.Layout(
# 					title=f"Regression Status",
# 					xaxis={"title": "Date"}, yaxis={"title": f"Failure Count"},
# 					colorway=["#C7037A", "#E20048", "#FFCB00", "#FF7C00", "#2F9609",
# 							  "#0E4770", "#A8AE0B"]
# 				)
# 			}
def update_graph(proj,conf,start_date,end_date):
	# print("\ndf_shashank\n", df)
	traces = []
	if start_date is not None:
		start_date = dt.strptime(start_date, '%Y-%m-%d')
		start_date_string = start_date.strftime('%Y-%m-%d')
	if end_date is not None:
		end_date = dt.strptime(end_date, '%Y-%m-%d')
		end_date_string = end_date.strftime('%Y-%m-%d')
	# df_date_selected = df[(df['date'] >= start_date_string) & (df['date'] <= end_date_string)]
	df_date_selected = df[(df['date'] >= start_date_string) & (df['date'] <= end_date_string)]
	# print("\ndf_date_selected\n", df_date_selected)
	df_proj_selected = df[(df['project'] == proj)]
	# print("\ndf_proj_selected\n", df_proj_selected)

	df_conf_selected = df[df['config'] == conf]

	# print("df_conf_selected\n", df_conf_selected)

	for sel_proj in df_proj_selected.project.unique():
		df_by_proj = df_proj_selected[df_proj_selected['project'] == sel_proj]
		for sel_conf in df_by_proj.config.unique():
			df_by_conf = df_conf_selected[
				(df_conf_selected['config'] == sel_conf) & (df_by_proj['project'] == sel_proj) & (
							df_date_selected['config'] == sel_conf)]
			if df_by_conf.empty == True:
				pass
			else:
				# print("\n\nHere Shashank\n\n", df_by_conf)
				traces.append(go.Scatter(
					x=df_by_conf['Diag'],
					y=df_by_conf['Fail Count'],
					text=df_by_conf['config'],
					mode='markers',
					opacity=0.5,
					marker={'size': 10, 'line': {'width': 0.5, 'color': 'white'}},
					name=sel_conf
				))
				return {
					'data': traces,
					'layout': go.Layout(
						title=f"Per Diag Fail Count",
						xaxis={"title": "Date"}, yaxis={"title": f"Failure Count"},
						colorway=["#C7037A", "#E20048", "#FFCB00", "#FF7C00", "#2F9609",
								  "#0E4770", "#A8AE0B"]
					)
				}


    # updated_fig = fig
    # return updated_fig


