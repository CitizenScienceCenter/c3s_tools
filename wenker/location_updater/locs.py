import psycopg2
import csv,json

BOGEN = '/home/encima/dev/uzh/c3s_tools/wenker/coords/wenkerdaten.csv'
DB_STRING = 'postgresql://pybossa:tester@wenker.citizenscience.ch/cs'

UPDATE_STRING = "UPDATE tasks SET info = info || (%s) WHERE id = %s;"
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

    def process(self):
        with open(BOGEN) as sheets:
            updated = []
            not_found = []
            incomplete = []

            for sheet in csv.reader(sheets):
                if len(sheet[0]) > 0:
                    sel = SELECT_STRING.format(sheet[0])
                    cursor = self.conn.cursor()
                    cursor.execute(sel)
                    res = cursor.fetchone()
                    if res is not None:
                        if sheet[8] != '':
                            info = {
                                'SchoolState': cantons[sheet[8]],
                                'SchoolRegion': sheet[7],
                                'SchoolDistrict': sheet[2]
                            }
                            if len(info['SchoolState']) == 0 or len(info['SchoolRegion']) == 0 or len(info['SchoolDistrict']) == 0:
                                # print("Updating {} with:".format(sheet[0]))
                                # print(info)
                                # print(sheet)
                                # input("Press Enter to continue...")
                                incomplete.append(sheet)
                            # update_query = UPDATE_STRING.format(district, region, state, res[0])
                            cursor.execute(UPDATE_STRING, (json.dumps(info), res[0]))
                            updated.append(sheet[0])
                        else:
                            # print('{}: canton not set'.format(sheet[0]))
                            incomplete.append(sheet)
                            
                    else:
                        # print("{} not updated".format(sheet[0]))
                        not_found.append(sheet)
            print(len(updated))
            print(len(not_found))
        with open('./not_found.csv', 'w') as nf:
            csv_writer = csv.writer(nf)
            for row in not_found:
                csv_writer.writerow(row)
        with open('./incomplete.csv', 'w') as ic:
            csv_writer = csv.writer(ic)
            for row in incomplete:
                csv_writer.writerow(row)
        
                
        




if __name__ == "__main__":
    i = LocationUpdate()
    i.process()


