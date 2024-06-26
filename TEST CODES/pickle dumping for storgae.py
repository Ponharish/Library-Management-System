import pickle
f=open('../STORAGE/bannerssource.txt','wb')
imagelist = [("./IMAGES/banners/banner.png",'24 Hours Digital Service Available...'),
             ('./IMAGES/banners/banner2.png','EVENTS: Wire Bending Flower Kit and First Aid Class'),
             ('./IMAGES/banners/banner3.png','EVENTS: Using Microsoft Windows 10 and Time Management')]
pickle.dump(imagelist,f)
f.close()
