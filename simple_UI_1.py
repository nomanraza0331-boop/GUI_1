from tkinter import *
root=Tk()
root.title("Ragistration form !")

L1=Label(root,text="Enter username:",font=("Times New Roman",20),padx=10,pady=10)
L1.grid(row=0,column=0)
username=Entry(root,font=("Times New Roman",20,"bold"))
username.grid(row=0,column=1,padx=10,pady=10)

L2=Label(root,text="Enter Email:",font=("Times New Roman",20),padx=10,pady=10)
L2.grid(row=1,column=0)
Email=Entry(root,font=("Times New Roman",20,"bold"))
Email.grid(row=1,column=1,padx=10,pady=10)

L3=Label(root,text="Enter Mobile number:",font=("Times New Roman",20),padx=10,pady=10)
L3.grid(row=2,column=0)
Mobile_number=Entry(root,font=("Times New Roman",20,"bold"))
Mobile_number.grid(row=2,column=1,padx=10,pady=10)

L4=Label(root,text="Enter Password:",font=("Times New Roman",20),padx=10,pady=10)
L4.grid(row=3,column=0)
Password=Entry(root,font=("Times New Roman",20,"bold"),show="*")
Password.grid(row=3,column=1,padx=10,pady=10)

L5=Label(root,text="Enter verify_password:",font=("Times New Roman",20),padx=10,pady=10)
L5.grid(row=4,column=0)
verify_password=Entry(root,font=("Times New Roman",20,"bold"),show="*")
verify_password.grid(row=4,column=1,padx=10,pady=10)

B1=Button(root,text="Submit",font=("Arial",15,"bold",),bg="white",fg="green")
B1.grid(row=5,column=0)
B2=Button(root,text="Exit",font=("Arial",15,"bold"),bg="white",fg="red")
B2.grid(row=5,column=1)

print("Check again !")

root.mainloop() 