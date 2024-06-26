import pickle
f=open('databaseaccounts.txt','wb')
l=[('localhost','root','12345678','12345678')]
pickle.dump(l,f)
f.close()
