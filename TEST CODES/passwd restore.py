import pickle
f=open('../STORAGE/encrypteduserdetails.txt','wb')
l=[(2, 'LIBRARIAN', 'wemindlibrary'),
   (6442, 'Jacky', 'asdf786'),
   (7948, 'subu', '1Ponharish'),
   (2017, 'prema', 'Prema1981'),
   (1198, 'satish', 'Abcdefg1'),
   (3876, 'Jackson', 'Jacky101')]
pickle.dump(l,f)
f.close()
