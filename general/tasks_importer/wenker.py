import config
from utils import Utils

class Wenker:

    @staticmethod
    def create_transcribe_media(app, client):
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

    @staticmethod
    def create_translate_tasks(app, client, rows):
        t = "<TEXT>"
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

    @staticmethod
    def create_transcribe_tasks(app, client, rows):
        tasks = []
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
                task_answers.append(
                    {"type": "text", "placeholder": "{}".format(i), "choices": []})
            task['content']['answers'] = task_answers
            img_name = r['SheetNumber'] + '*a.jp2'
            img = Utils.list_images(config.ROOT_DIR, img_name)
            if img is not None:
                r['path'] = './static/upload/' + img.replace(config.ROOT_DIR, '')
                task['info'] = r
                tasks.append(task)
        print(len(tasks))

        req, resp = app.op['create_tasks'](tasks=tasks)
        task_save = client.request((req, resp)).data
        print(task_save)