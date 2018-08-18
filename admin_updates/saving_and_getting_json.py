import os
import json
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder

class Saving_And_Getting_Json:
    def __init__(self):
        self.base_dir = settings.BASE_DIR

    def get_json_file(self, get_json):
        main_json_file = self.base_dir + '/static/json/'+ get_json +'.json'
        try:
            main_json_file_size = os.path.getsize(main_json_file)
            if main_json_file_size > 0:
                 with open(main_json_file) as json_file:
                     get_main_json = json.load(json_file)
        except FileNotFoundError as e:
            print(e)
        return get_main_json

    def save_json(self, save_file_to_json, get_json):
        json_file = json.dumps(save_file_to_json, ensure_ascii=False, indent=4, cls=DjangoJSONEncoder)
        with open(self.base_dir + '/static/json/'+ get_json +'.json', 'w') as f:
            f.write(json_file)
