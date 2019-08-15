import os
import glob
import csv
import config
import json
from pathlib import Path
from utils import Utils
from snapp import Snapp
from subprocess import call
from pyswagger import App, Security
from pyswagger.contrib.client.requests import Client
from pyswagger.utils import jp_compose
import requests


class Ingestor():

    def __init__(self, url = config.API_URL, key = config.API_KEY):
        self.app, self.client = Utils.generate_client(url, key)

    def ingest(self):
        tasks =[]
        rows = Utils.read_csv(config.ROOT_DIR + config.CSV_PATH, ',', 'latin1')
        print(len(rows))
        for row in rows:
            row['difficulty'] = 0 if row['difficulty'] == 'easy' else 1
            task = {
                'activity_id': '74033a29-4346-485d-b0e3-3f263a507837',
                'sequence': 0,
                'info': row,
                'required': True,
                'title': 'What is this snake?',
                'content': {}
            }
            img = Utils.list_images(config.ROOT_DIR, row['filename'])

            if img is not None and Path('{}{}'.format(config.ROOT_DIR, row['filename'])).exists():
                task['info']['filename'] = row['filename']
                if task['info']['genus']:
                    tasks.append(task)
        print("tasks found", len(tasks))
        req, resp = self.app.op['create_tasks'](tasks=tasks)
        task_save = self.client.request((req, resp))
        # TODO copy all media here
        # print(task_save.text)

    def create_media(self):
        req, resp = self.app.op['get_tasks'](limit=1500)
        tasks = self.client.request((req, resp)).data
        print(len(tasks))
        for t in tasks:
            media = {
                "source_id": t["id"],
                "path": t["info"]["filename"],
                "name": t["info"]["binomial"],
                "filetype": "raster-image"
            }

            req, resp = self.app.op['create_medium'](media=media)
            media_save = self.client.request((req, resp))
            # headers = {'x-api-key': config.API_KEY, 'content-type': 'application/json'}
            # r = requests.post('{}/api/v2/media'.format(config.API_URL), data=json.dumps(media), headers=headers)
            # print(r.text)

    def delete_media(self):
        req, resp = self.app.op['get_media'](limit=3000)
        media = self.client.request((req, resp)).data
        for t in media:
            req, resp = self.app.op['delete_medium'](id=t['id'])
            t_del = self.client.request((req, resp))

    def delete_tasks(self):
        req, resp = self.app.op['get_tasks'](limit=3000)
        tasks = self.client.request((req, resp)).data
        for t in tasks:
            req, resp = self.app.op['delete_task'](id=t['id'])
            t_del = self.client.request((req, resp))



if __name__ == "__main__":
    i = Ingestor()
    # i.ingest()
    # TODO create project here (or provide ID)
    i.create_media()
    # i.delete_media()
    # i.delete_tasks()


