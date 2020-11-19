from tkinter import *
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

    def click():
        vote.bjp+=1
        l1=Label(vote.tk,text="You have voted for BJP     \n Thank you!!",font=("Joker",20),fg="red",bg='black').place(x=500,y=300)
    def click1():
        vote.cong+=1
        l1=Label(vote.tk,text="You have voted for CONG   \n Thank you!!",font=("Joker",20),fg="red",bg='black').place(x=500,y=300)
    def click2():
        vote.aap+=1
        l1=Label(vote.tk,text="You have voted for AAP     \n Thank you!!",font=("Joker",20),fg="red",bg='black').place(x=500,y=300)

    b1=Button(tk,text="BJP",font=("Arial",20),width=20,fg="blue",command=click).place(x=50,y=200)
    b2=Button(tk,text="CONG",font=("Arial",20),width=20,fg="blue",command=click1).place(x=500,y=200)
    b3=Button(tk,text="AAP",font=("Arial",20),width=20,fg="blue",command=click2).place(x=950,y=200)

    def click3():
        l2=Label(vote.tk,text="Total no. of votes: \n BJP:"+str(vote.bjp)+"\n CONG:"+str(vote.cong)+"\n AAP:"+str(vote.aap),font=("Joker",20),fg="red",bg='black').place(x=555,y=550)

    b4=Button(tk,text="See results",font=("Arial",20),width=10,command=click3).place(x=600,y=450)
    
