import os
import pickle
path = "/Users/localds/AV/"
pkl_file = path + ".data.pkl"
with open(pkl_file, 'rb') as f:
    data = pickle.load(f)
    lst = data['todown']


for i in lst:
    os.system(
        "jav -s {fh} -x http://127.0.0.1:8123".format(fh=i))
