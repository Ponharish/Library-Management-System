import pickle

f=open('../STORAGE/bannerssource.txt','rb')
l=pickle.load(f)

print(l)
l=pickle.load(f)
f.close()
