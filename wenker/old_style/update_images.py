import psycopg2
import config


IMG_NAMES = '/Users/encima/.CMVolumes/Nextcloud/Documents/uzh/wenker_CH_kurrent.txt'
DB_STRING = 'postgresql://pybossa:tester@wenker.citizenscience.ch/cs'

UPDATE_STRING = "UPDATE tasks SET info = info || '{{\"old_style\": 1}}' WHERE id = '{}';"
SELECT_STRING = "SELECT * FROM tasks WHERE info ->> 'path'::text like '%{}%'::text"

class OldStyleUpdate:

    def __init__(self):
        self.conn = psycopg2.connect(host=config.DB_HOST,database=config.DB_NAME, user=config.DB_USER, password=config.DB_PWD)

    def process(self):
        with open(IMG_NAMES) as images:
            for image in images:
                img = image.replace('.jpg', '').rstrip()
                sel = SELECT_STRING.format(img)
                print(sel)
                cursor = self.conn.cursor()
                cursor.execute(sel)
                res = cursor.fetchone()
                if res is not None:
                  print(res[0])
                  print(UPDATE_STRING.format(res[0]))
                  cursor.execute(UPDATE_STRING.format(res[0]))
                else:
                  print("{} not updated".format(img))



if __name__ == "__main__":
    i = OldStyleUpdate()
    i.process()


