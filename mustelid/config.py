ROOT_DIR = './'
MEDIA_PATTERN = '*.mp4'
CSV_PATH = 'all_files.csv'
API_KEY = "c14a4415-5a4d-46dc-a974-7f8e2d365ee2"
API_URL = "https://api.citizenscience.ch/api/v2/swagger.json"
# API_URL = "http://localhost:8080/api/v2/openapi.json"
ACTIVITY_ID = "09a565c4-73f8-483d-b59a-c3e5791f9a16"
TASK_TEMPLATE =  {
                'activity_id': "09a565c4-73f8-483d-b59a-c3e5791f9a16",
                'sequence': 0,
                'info': {},
                'required': True,
                'title': 'Is there a mustelid here?',
                'content': {
                    'items':''
                }
            }
MEDIA_TEMPLATE = {
                "source_id": "",
                "path": "",
                "name": "",
                "filetype": "",
                "info": {}
            }
