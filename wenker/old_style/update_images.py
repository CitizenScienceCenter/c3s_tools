import psycopg2


IMG_NAMES = '/Users/encima/.CMVolumes/Nextcloud/Documents/uzh/wenker_CH_kurrent.txt'
DB_STRING = 'postgresql://pybossa:tester@wenker.citizenscience.ch/cs'

UPDATE_STRING = "UPDATE tasks SET info = info || {'old_style': 1} WHERE id = '{}'"
SELECT_STRING = "SELECT * FROM tasks WHERE info ->> 'path'::text like '%{}%'::text"

class OldStyleUpdate:

    def __init__(self):
        self.conn = psycopg2.connect(host="wenker.citizenscience.ch",database="cs", user="pybossa", password="tester")

    def process(self):
        with open(IMG_NAMES) as images:
            for image in images:
                # print(image)
                img = image.replace('.jpg', '').rstrip()
                sel = SELECT_STRING.format(img)
                print(sel)
                cursor = self.conn.cursor()
                cursor.execute(sel)
                res = cursor.fetchone()
                print(res)



if __name__ == "__main__":
    i = OldStyleUpdate()
    i.process()


