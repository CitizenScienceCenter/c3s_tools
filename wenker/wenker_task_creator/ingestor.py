import os, glob, csv
from subprocess import call
from pyswagger import App, Security
from pyswagger.contrib.client.requests import Client
from pyswagger.utils import jp_compose



ROOT_DIR = '/Users/encima/drive/uzh/linguistics/data/wenkerbogen-switzerland/'
IMG_PATTERN = '*a.jpg'
CSV_PATH = 'wenkerbogen-schweiz.csv'
API_KEY = "fe3682d1-add1-40e6-b8ca-d95ebb2673af"
API_URL = "http://172.23.52.127:8080/api/v1/swagger.json"

# Must be in UZH network
def generate_client(URL, KEY = None):
    app = App._create_(URL)
    auth = Security(app)
    auth.update_with('apiKeyHeader', KEY) # api key
    client = Client(auth)
    return app, client

def read_csv(path, delim):
    with open(path, 'r') as f:
        reader = csv.DictReader(f, delimiter=delim)
        rows = [row for row in reader]
    return rows


def list_images(path, pattern):
    all_img = glob.iglob(path + pattern, recursive=False)
    return all_img
    # for a in all_img:
    #     return a

def create_translate_tasks():
    app, client = generate_client(API_URL, API_KEY)
    rows = read_csv("/Users/encima/drive/uzh/linguistics/data/questions.csv", '.')
    t = "Bitte übersetzen Sie diesen Satz in Ihren lokalen Dialekt."
    tasks = []
    for r in rows:
        task = {
            'project_id': '507b3f89-aff1-4fa3-8f28-9c8399811539',
            'sequence': 0,
            'info': {},
            'required': True,
            'title': t,
            'content': {"question": {"text": r['Sentence'], "type": "text"}, "answers": [{"type": "text", "placeholder": "", "choices": []}]}
        }
        tasks.append(task)
    req, resp = app.op['create_tasks'](tasks=tasks)
    task_save = client.request((req, resp)).data
    print(task_save)

def convert():
    img = list_images(ROOT_DIR, '*a.jp2')
    print(img)
    for i in img:
        print(i.replace(' a', '\ a'))
        os.system("convert {} {}".format(i.replace(" a", '\ a'), i.replace(" a", 'a').replace('jp2', 'jpg')))
        print('-----')



def create_transcribe_tasks():
    rows = read_csv(ROOT_DIR + CSV_PATH, '|')
    tasks = []
    app, client = generate_client(API_URL, API_KEY)
    t = "Bitte übertragen Sie jeden nummerierten Satz in das entsprechende Textfeld."
    for r in rows:
        task = {
            'project_id': 'e4b5ebc5-47a2-430b-84a9-a03b1d4dda34',
            'sequence': 0,
            'info': {},
            'required': True,
            'title': t,
            'content': {"question": {"text": t, "type": "single_file"}}
        }
        task_answers = []
        for i in range(1, 41):
            task_answers.append({"type": "text", "placeholder": "{}".format(i), "choices": []})
        task['content']['answers'] = task_answers
        img_name = r['SheetNumber'] + '*a.jp2'
        img = list_images(ROOT_DIR, img_name)
        if img is not None:
            r['path'] = './static/upload/' + img.replace(ROOT_DIR, '')
            task['info'] = r
            tasks.append(task)
    print(len(tasks))
        
    req, resp = app.op['create_tasks'](tasks=tasks)
    task_save = client.request((req, resp)).data
    print(task_save)

def find_img(img, id):
    for i in img:
        if id in i:
            return i
    print(id, "Not found")
    return None

def create_transcribe_media():
    app, client = generate_client(API_URL, API_KEY)
    req, resp = app.op['get_tasks'](limit=20000)
    tasks = client.request((req, resp)).data
    for t in tasks:
        media = {
            'source_id': '',
            'path': '',
            'name': '',
            'f_type': 'raster-image'
        }
        if('SheetNumber' in t.info):
            i = t.info['SheetNumber'] + 'a.jpg'
            media['source_id'] = t.id
            media['path'] = './static/upload/' + i
            media['name'] = i
            req, resp = app.op['create_media'](media=media)
            m_save = client.request((req, resp)).data
            print(t.id, m_save)
        else:
            continue

# create_transcribe_tasks()
create_transcribe_media()
# create_translate_tasks()
# convert()