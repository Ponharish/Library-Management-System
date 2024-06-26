from tkinter import *
import random

def captcha():
    global errorstreams
    def go():
        global errorstreams
        errorstreams. pack_forget()#This command deletes the frame
        errorstreams=Frame(root)#This creates the frame again
        errorstreams.pack(side=BOTTOM)
        captcha=captchaentry.get()#get the value enetered by the user
        if listoffilesofcaptcha[captchanumber][1]!=captchaentry.get():#Ecvaluates the captcha
            lblcaptchastats=Label(errorstreams,text='Wrong Captcha Please Retry', fg='red')
            lblcaptchastats.pack()
        else:
            lblcaptchastats=Label(errorstreams,text='Success', fg='green')
            lblcaptchastats.pack()
        
    captchaframe = Frame(root,width=1000, height= 1000)# A frame created
    captchaframe.pack()
    captchanumber= random.randint(1,5)-1 #picks a random captcha
    photo=PhotoImage(file=listoffilesofcaptcha[captchanumber][0])#loads its image path
    captchaphoto=Label(captchaframe,image=photo)
    captchaentry = Entry(captchaframe, width=20)#asking for the value
    captchaentry.pack(side=BOTTOM)
    captchaphoto.pack()

    btn=Button(captchaframe,text='sumbit',command=go)#submit the value for evaluation
    btn.pack()
    
    errorstreams=Frame(root)#This frame is just to give status of the enetered captcha
    errorstreams.pack(side=BOTTOM)
    root.mainloop()
    
root =Tk()
listoffilesofcaptcha=[('captcha 1.png','28ivw'),('captcha 2.png','k4ez'),('captcha 3.png','4D7YS'),
                      ('captcha 4.png','6ne3'),('captcha 5.png','e5hb')]
#list of Paths of captcha image and their respective value
captcha()

# pwd is the password entered by the user
countforpasswordcaptletter,countforpasswordsmallletter, countforpasswordnumber=0,0,0 #PASSWORD EVALUATION
for varia in pwd:
        if ord(varia) in range(65,91):
            countforpasswordcaptletter+=1
        elif ord(varia) in range(97,123):
            countforpasswordsmallletter+=1
        elif ord(varia) in range(48,58):
            countforpasswordnumber+=1
if countforpasswordcaptletter==0 or countforpasswordsmallletter == 0 or countforpasswordnumber ==0 or len(pwd)<8:
    passwordinvalidlabel=Label(errorstreams,text='Your Password is weak', fg='red')#EVALUATION FOR STRONG PASSWORD
    passwordinvalidlabel.pack()
            
if pwd != pwdconf:#                         #IF PASSWORD ENTERED MATCHEES WITH THE CONFIRMED ONE
    passdoesnotmatchlabel=Label(errorstreams,text='Passwords Entered does not match', fg='red')
    passdoesnotmatchlabel.pack()
            
''''''
