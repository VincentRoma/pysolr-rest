from views import DataAPI

def init_route(app=None):
    data_view = DataAPI.as_view('data_api')
    app.add_url_rule('/data/', defaults={'field': None, 'params': None},
                     view_func=data_view, methods=['GET',])
    app.add_url_rule('/data/<field>/<params>',
                     view_func=data_view, methods=['GET',])
