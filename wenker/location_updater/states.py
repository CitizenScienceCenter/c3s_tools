import psycopg2
import csv, json

BOGEN = '/home/encima/Nextcloud/Documents/uzh/wenkerdaten.csv'
DB_STRING = 'postgresql://pybossa:testing@localhost:5430/cs'

UPDATE_STRING = "UPDATE tasks SET info = info || '(%s)' WHERE id = %s;"
UPDATE = "UPDATE tasks SET info = info || '{}' WHERE id = '{}';"
SELECT_STRING = "SELECT * FROM tasks WHERE info ->> 'path'::text like '%{}%'::text"

cantons = {
    'BE': 'Bern',
    'TG': 'Thurgau',
    'LU': 'Luzern',
    'SO': 'Solothurn',
    'ZH': 'Zürich',
    'UR': 'Uri',
    'SZ': 'Schwyz',
    'OW': 'Obwalden',
    'NW': 'Nidwalden',
    'GL': 'Glarus',
    'ZG': 'Zug',
    'FR': 'Fribought',
    'BS': 'Basel-Stadt',
    'BL': 'Basel-Landschaft',
    'SH': 'Schaffhausen',
    'AR': 'Appenzell Ausserhoden',
    'AI': 'Appenzell Innerhoden',
    'SG': 'St. Gallen',
    'GR': 'Grisons',
    'AG': 'Aargau',
    'TI': 'Ticino',
    'VD': 'Vaud',
    'VS': 'Valais',
    'NE': 'Neuchâtel',
    'GE': 'Geneva',
    'JU': 'Jura'
}

class LocationUpdate:

    def __init__(self):
        self.conn = psycopg2.connect(DB_STRING)

    def find(self, csv_file, place):
        for row in csv.reader(csv_file):
            # print(ascii(row[2]), ascii(place))
            if ascii(place.lower()) in ascii(row[2].lower()):
                print(row[8])

    def process(self):
        cursor = self.conn.cursor()
        cursor.execute("select id, info from tasks where info->>'SchoolState' = '';")
        res = cursor.fetchall()

        count = 1
        with open(BOGEN) as sheets:

            wenker_map = []
            states = []
            places = []
            for row in csv.reader(sheets):
                wenker_map.append({'state': row[8], 'place': row[2]})
                states.append(row[8])
                places.append(ascii(row[2].lower()))

        for r in res:
            place = ascii(r[1]['title'].lower())
            if place in places:
                idx = places.index(place)
                if len(states[idx]) > 0:
                    canton = cantons[states[idx]]
                    info = {
                        'SchoolState': canton
                    }
                    # print(cursor.execute(UPDATE_STRING, (json.dumps(info), r[0])))

                    print(UPDATE.format((json.dumps(info)), r[0]))

        cursor.close()

if __name__ == "__main__":
    i = LocationUpdate()
    i.process()


