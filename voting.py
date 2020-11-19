from tkinter import *
from tkinter.ttk import *
class vote():
    bjp=0
    cong=0
    aap=0

    tk=Tk()
    tk.title("Voting app")
    tk.configure(background="Black")
    tk.geometry("1366x768")
    tk.maxsize(1366,768)

    title=Label(tk,text="Voting App",font=("Joker",50),fg="red",bg='black')
    title.place(x=500,y=5)

    rad1=Radiobutton(tk,text="BJP",width=10,value=1).place(x=150,y=200)
    rad2=Radiobutton(tk,text="CONG",width=10,value=2).place(x=600,y=200)
    rad3=Radiobutton(tk,text="AAP",width=10,value=3).place(x=1050,y=200)



    def click():
        
        if (vote.rad1==True):
            vote.bjp+=1
            party="BJP"
        elif(vote.rad2==True):
            vote.cong+=1
            party="CONG"
        elif(vote.rad3==True):
            vote.aap+=1
            party="AAP"
        l1=Label(vote.tk,text="You have voted for "+party+"\n Thank you!!"+"\n Total no. of votes: \n BJP:"+bjp+"\n CONG:"+cong+"\n AAP:"+aap,font=("Joker",50),fg="red",bg='black').place(x=620,y=300)    

    b=Button(tk,text="CONTINUE",fg="blue",command=click).place(x=620,y=400)

