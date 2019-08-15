import csv, json, re
from dinsort import normalize, sort_func

BOGEN = '/home/encima/dev/wenker_cantons.csv'

cantons = []

def din5007(input):
	""" This function implements sort keys for the german language according to 
	DIN 5007."""
	
	# key1: compare words lowercase and replace umlauts according to DIN 5007
	key1=input.lower()
	key1=key1.replace(u"ä", u"a")
	key1=key1.replace(u"ö", u"o")
	key1=key1.replace(u"ü", u"u")
	key1=key1.replace(u"ß", u"ss")
	
	# key2: sort the lowercase word before the uppercase word and sort
	# the word with umlaut after the word without umlaut
	key2=input.swapcase()
	
	# in case two words are the same according to key1, sort the words
	# according to key2. 
	return (key1, key2)

with open(BOGEN) as canton_csv:
    for row in csv.reader(canton_csv):
        found = False
        for c in cantons:
            if c['label'] == row[0]:
                c['towns'].append(row[1])
                found = True
        if not found:
            cantons.append({
                'label': row[0],
                'lang': 'DE',
                'towns': [row[1]]
            })

    for r in cantons:
        if r['label'] == 'Zürich':
            print(r['towns'])
            print('------------------------')
            print(sorted(r['towns'], key=sort_func(case_sensitive=True)))
        # decoded = r['towns'].copy()
        # for d in decoded:
        #     d = d.encode('utf-8')
        # d = sorted(d)
        # for d in decoded:
        #     d = d.decode('utf-8')
        r['towns'] = sorted(r['towns'], key=sort_func(case_sensitive=True))
    with open('cantons.json', 'w', encoding='utf8') as output:
        json.dump(cantons, output, ensure_ascii=False)

