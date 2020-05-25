import dash_html_components as html
import dash_core_components as dcc

def Header():
    return html.Div([
        # get_logo(),
        get_header(),
        html.Br([]),
        get_menu(),
        html.Br([])
    ])

#html.Img(src='assets/dv6y2019415962019-09-183102169Bee Cube Logo.jpg',  height='150', width='300'

def get_logo():
    logo = html.Div([

        html.Div([
            html.Img(src='assets/logo.jpg', style={'height' : '30%','width' : '30%', 'float': 'left'})
        ], className="ten columns padded"),

    ], className="row gs-header")
    return logo


def get_header():
    header = html.Div([

        html.Div([
            html.H5(
                'Tenscilica Failure Reporting System')
        ], className="twelve columns padded")

    ], className="row gs-header gs-text-header")
    return header

# gs-header gs-text-header

def get_menu():
    menu = html.Div([
        dcc.Link('Overview - Config   ', href='/report/conf-failure/', className="tab first"),

        dcc.Link('Overview - Diag   ', href='/report/diag-failure/', className="tab"),

    ], className="row ")
    return menu
