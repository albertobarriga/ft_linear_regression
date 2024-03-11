import os, pickle
FILE = 'result.pkl'

m = 0
c = 0

if os.path.isfile(FILE):
	with open(FILE, 'rb') as f:
		results = pickle.load(f)
		assert len(results) == 2
		m = results[0]
		c = results[1]

milleage = input('Introduce milleage: ')
try:
    result = round(float(milleage) * m + c, 2)
    if result < 0:
        result = 0
    print(result)
except:
	print('ERROR: You should introduce a number')