import pickle
import json

D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')
pickle.dump(D, F)
F.close()
F = open('datafile.pkl', 'rb')
E = pickle.load(F)
print(E, '\n')


name = dict (first = 'Bob', last = 'Smith')
rec = dict(name=name, job=['dev', 'mgr'], age = 40.5)
print(rec)
print(json.dumps(rec))
S = json.dumps(rec)
print(S)
O = json.loads(S)
print(O)
print(rec == O)
json.dump(rec, fp=open('testjson.txt', 'w'), indent = 4)
print(open('testjson.txt').read())
P = json.load(open('testjson.txt'))
print(P)
