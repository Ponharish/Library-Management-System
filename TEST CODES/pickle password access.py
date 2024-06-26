import pickle
f=open('../STORAGE/encrypteduserdetails.txt','rb')
l=pickle.load(f)
print(l)
f.close()
