import os, glob, csv
import codecs
from pyswagger import App, Security
from pyswagger.contrib.client.requests import Client
from pyswagger.utils import jp_compose

class Utils:

    @staticmethod
    def generate_client(URL, KEY=None):
        app = App._create_(URL)
        auth = Security(app)
        auth.update_with('apiKeyHeader', KEY)  # api key
        client = Client(auth)
        return app, client


    @staticmethod
    def jp2_convert(direc, fname):
        img = Utils.list_images(direc, fname)
        for i in img:
            print(i.replace(' a', '\ a'))
            os.system("convert {} {}".format(i.replace(" a", '\ a'),
                                            i.replace(" a", 'a').replace('jp2', 'jpg')))
            print('-----')

    @staticmethod
    def list_images(path, pattern):
        all_img = glob.iglob(path + pattern, recursive=False)
        return all_img

    @staticmethod
    def read_csv(path, delim, enc='utf8'):
        with open(path, 'r', encoding=enc) as f:
            reader = csv.DictReader(f, delimiter=delim)
            rows = [row for row in reader]
        return rows

    @staticmethod
    def find_img(img, id):
        for i in img:
            if id in i:
                return i
        print(id, "Not found")
        return None
