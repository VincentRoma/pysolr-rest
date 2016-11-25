from views import DataAPI, SuggestionAPI

'''
    Routes definition, defaults are:
        /data/                  return first page unfiltered
        /data/<field>/<params>  return first page filter by <params> on <field>
                                <field> is required
                                <params> e.g: UR
                                e.g: /data/name/UR return FAURECIA if exist.

'''

def load_routes(app=None):
    data_view = DataAPI.as_view('data_api')
    suggest_api = SuggestionAPI.as_view('suggest_api')

    app.add_url_rule('/data/', defaults={'field': None, 'params': None},view_func=data_view, methods=['GET',])
    app.add_url_rule('/data/<field>/<params>',view_func=data_view, methods=['GET',])

    app.add_url_rule('/suggestions/<field>/<params>',view_func=suggest_api, methods=['GET',])
