"""
An app to test how to make API services with werkzeug

How it should work:

- describe your ressources
  - fields to be displayed
  - how fields should be displayed
  - etc...

- define global settings

  - pagination
  - authorization
  - authentication
  - throttling
  - etc..

"""

from rest_api_framework.datastore import PythonListDataStore
from rest_api_framework.controllers import ApiView


ressources = [
    {"name": "bob",
     "age": a,
     "id": a
     } for a in range(100)
    ]

api_keys = [
    {"id": "azerty"},
    {"id": "querty"}
    ]


class View(ApiView):
    """
    The main views of the application
    """
    pass


class ApiApp(View):

    def __init__(self, *args, **kwargs):
        urls = [
            ('/', 'index', ["GET", "POST"]),
            ('/<int:identifier>/', 'unique_uri', ["GET", "PUT", "DELETE"]),
            ]

        options = {"paginate_by": 20,
                   }
        options["description"] = {
            "name": {
                "type": basestring, "required": True},
            "age": {
                "type": int, "required": True},
            "id": {
                "type": "autoincrement", "required": False}
            }

        self.datastore = PythonListDataStore(ressources, **options)
        super(ApiApp, self).__init__(urls, *args, **kwargs)
