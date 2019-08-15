import os
import glob
import csv
import config
import json
from pathlib import Path
from utils import Utils
from subprocess import call
from pyswagger import App, Security
from pyswagger.contrib.client.requests import Client
from pyswagger.utils import jp_compose
import requests


class Ingestor():

    def __init__(self, url = config.API_URL, key = config.API_KEY):
        self.app, self.client = Utils.generate_client(url, key)

    def ingest(self):
        rows = Utils.read_csv(os.path.join(config.ROOT_DIR,config.CSV_PATH), ',', 'utf8')
        for row in rows:
            tasks = [
                dict(activity_id='09a565c4-73f8-483d-b59a-c3e5791f9a16', sequence=0, required=True, allow_multiple=True,
                     title='Is there a mustelid?', content={'items': 'none'}),
            ]
            response = self.client.request(
                self.app.op['create_tasks'](  # access the Operation
                    tasks = tasks  # provide the parameter
                ))
            if response.status == 201:
                task = response.data[0]
                for video in row:
                    self.create_media(task, video)

    def create_media(self, task, video):
            if video:
                video = video.replace('AVI', 'mp4')
                if (os.path.exists(video)):
                    media = {
                        "source_id": task.id,
                        "path": video,
                        "name": video,
                        "info": {
                            "thumb": video.replace('mp4', 'jpg')
                        }
                    }
                    response = self.client.request(self.app.op['create_medium'](media=media))
                    print(response.data)

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
    i.ingest()
    # TODO create project here (or provide ID)
    # i.create_media()
    # i.delete_media()
    # i.delete_tasks()


