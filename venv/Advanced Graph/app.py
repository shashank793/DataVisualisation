import dash


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
# external_stylesheets = [
#     'https://codepen.io/chriddyp/pen/bWLwgP.css',
#     {
#         'href': 'https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css',
#         'rel': 'stylesheet',
#         'integrity': 'sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO',
#         'crossorigin': 'anonymous'
#     }
# ]

# external_scripts = [
#     'https://www.google-analytics.com/analytics.js',
#     {'src': 'https://cdn.polyfill.io/v2/polyfill.min.js'},
#     {
#         'src': 'https://cdnjs.cloudflare.com/ajax/libs/lodash.js/4.17.10/lodash.core.js',
#         'integrity': 'sha256-Qqd/EfdABZUcAxjOkMi8eGEivtdTkh3b65xCZL4qAQA=',
#         'crossorigin': 'anonymous'
#     }
# ]
#external_scripts=external_scripts,

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, url_base_pathname='/report/conf-failure/')
server = app.server
app.config.suppress_callback_exceptions = True

# import dash_auth

# VALID_USERNAME_PASSWORD_PAIRS = [
#     ['', '']
# ]

# auth = dash_auth.BasicAuth(
#     app,
#     VALID_USERNAME_PASSWORD_PAIRS
# )
