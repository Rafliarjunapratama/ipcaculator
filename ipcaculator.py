from tkinter import *
from tkinter.font import Font
root = Tk()
root.geometry("930x800")
root.title("Caculator ip")
def on_enter6(e):
		subnetmask_engtry.delete(0,'end')


def subnetmask():
	home_subnetmask = Frame(option_border,bg="#FFFFFF")
	
	subnetmask_label= Label(home_subnetmask,text="Subnet Mask",fg="Black",bg="#FFFFFF",font=("Arial",7,"bold"))
	subnetmask_label.pack(pady=20)
	
	global subnetmask_engtry
	subnetmask_engtry = Entry(home_subnetmask,width=30,font=("default", 5 ),bg="#FFFFFF",highlightthickness=2,highlightbackground="black")
	subnetmask_engtry.pack(ipady=10,padx=10)
	subnetmask_engtry.insert(0,"                Masukan Subnetmask ")
	subnetmask_engtry.bind("<FocusIn>",on_enter6)
	
	
	#lambda 
	
	wedget= Frame(home_subnetmask,bg="#FFFFFF")
	
	subnetmask_button = Button(wedget,text="Subnet Matching",bd=0, font=("Bold",4),bg="#FFFFFF",fg="#1b1b1b",highlightthickness=2,highlightbackground="#1b1b1b",activebackground="#1b1b1b",activeforeground="#FFFFFF",width=7,command=subnetmask_proses)
	subnetmask_button.pack(side=LEFT,padx=10)
	
	
	
	wedget.pack(pady=40)
	home_subnetmask.pack()
def subnetmask_proses():
	home_subnetmask_proses= Frame(option_border,bg="#FFFFFF")
	 
	ntah = ["255.0.0.0","255.128.0.0","255.192.0.0","255.224.0.0","255.240.0.0","255.248.0.0","255.252.0.0","255.254.0.0","255.255.0.0","255.255.128.0","255.255.192.0.","255.255.224.0","255.255.240.0","255.255.248.0","255.255.252.0","255.255.254.0","255.255.255.0","255.255.255.128","255.255.255.192","255.255.255.224","255.255.255.240","255.255.255.248","255.255.255.252","255.255.255.254","255.255.255.255.255"]
	entry_int = int(subnetmask_engtry.get())
	
	if 8 <= entry_int and 33 > entry_int :
		hasil = entry_int - 8
		hasil1 = ntah[hasil].replace('"',"")
		
	elif 8 > entry_int:
		hasil1 = " Tidak Ada Subnetmask Di Bawah 8"
	elif  33 <=entry_int:
			hasil1 = " Tidak Ada Subnetmask Di Atas 32"
	
	ucupoutput = Label(home_subnetmask_proses,text=hasil1,font=("'Consolas",6,"bold"),bg="#FFFFFF",highlightthickness=2,highlightbackground="#1b1b1b",width=30)
	ucupoutput.pack(ipady=3,pady=10)
	home_subnetmask_proses.pack()
	

def apan():
	home_apan = Frame(option_border,bg="white")
	
	subnetmask_label= Label(home_apan,text="Host id",fg="Black",bg="#FFFFFF",font=("Arial",7,"bold"))
	subnetmask_label.pack(pady=20)
	
	global subnetmask_engtry
	subnetmask_engtry = Entry(home_apan,width=30,font=("default", 5 ),bg="#FFFFFF",highlightthickness=2,highlightbackground="black")
	subnetmask_engtry.pack(ipady=10,padx=10)
	subnetmask_engtry.insert(0,"                Masukan Host ID ")
	subnetmask_engtry.bind("<FocusIn>",on_enter6)
	
	wedget= Frame(home_apan,bg="#FFFFFF")
	uwo = int(1)
	uwo1 = int(2)
	uwo2 = int(3)
	subnetmask_button = Button(wedget,text="Host Class A",bd=0, font=("Bold",4),bg="#FFFFFF",fg="#1b1b1b",highlightthickness=2,highlightbackground="#1b1b1b",activebackground="#1b1b1b",activeforeground="#FFFFFF",width=7,command= lambda : apan_proses(uwo))
	subnetmask_button.pack(side=LEFT,padx=10)
	
	subnetmask_button = Button(wedget,text="Host Class B",bd=0, font=("Bold",4),bg="#FFFFFF",fg="#1b1b1b",highlightthickness=2,highlightbackground="#1b1b1b",activebackground="#1b1b1b",activeforeground="#FFFFFF",width=7,command= lambda : apan_proses(uwo1))
	subnetmask_button.pack(side=LEFT,padx=10)
	
	subnetmask_button = Button(wedget,text="Host Class C",bd=0, font=("Bold",4),bg="#FFFFFF",fg="#1b1b1b",highlightthickness=2,highlightbackground="#1b1b1b",activebackground="#1b1b1b",activeforeground="#FFFFFF",width=7,command= lambda : apan_proses(uwo2))
	subnetmask_button.pack(side=LEFT,padx=10)
	
	
	
	wedget.pack(pady=40)
	home_apan.pack()
def apan_proses(uwo):
	home_subnetmask_proses= Frame(option_border,bg="#FFFFFF")
	kokok = int(subnetmask_engtry.get())
	lahkok = [8,7,6,5,4,3,2,1,0]
	lahkok2 = [16,15,14,13,12,10,9,8,7,6,5,4,3,2,1,0]
	lahkok3 = [24,23,22,21,20,19,18,17,16,15,14,13,12,10,9,8,7,6,5,4,3,2,1,0]
	
	if uwo == 3 and kokok <= 32:
		lahiya = kokok-24
		if lahiya >-1:
				hasil1 = lahkok[lahiya]
				hasil2 = 2**hasil1
				hasil3 = hasil2-2
	elif uwo == 2 and kokok <= 32:
		lahiya = kokok-16
		if lahiya >-1:
				hasil1 = lahkok[lahiya]
				hasil2 = 2**hasil1
				hasil3 = hasil2-2
	elif uwo == 1 and kokok <= 32:
		lahiya = kokok-8
		if lahiya >-1:
				hasil1 = lahkok[lahiya]
				hasil2 = 2**hasil1
				hasil3 = hasil2-2
		
	ucupoutput = Label(home_subnetmask_proses,text=hasil3,font=("'Consolas",6,"bold"),bg="#FFFFFF",highlightthickness=2,highlightbackground="#1b1b1b",width=30)
	ucupoutput.pack(ipady=3,pady=10)
	home_subnetmask_proses.pack()
	
	
	
	
def network():
	home_apan = Frame(option_border,bg="white")
	
	subnetmask_label= Label(home_apan,text="Network ID",fg="Black",bg="#FFFFFF",font=("Arial",7,"bold"))
	subnetmask_label.pack(pady=20)
	
	global subnetmask_engtry
	subnetmask_engtry = Entry(home_apan,width=30,font=("default", 5 ),bg="#FFFFFF",highlightthickness=2,highlightbackground="black")
	subnetmask_engtry.pack(ipady=10,padx=10)
	subnetmask_engtry.insert(0,"                Masukan Network ID ")
	subnetmask_engtry.bind("<FocusIn>",on_enter6)
	
	wedget= Frame(home_apan,bg="#FFFFFF")
	uwo = int(1)
	uwo1 = int(2)
	uwo2 = int(3)
	subnetmask_button = Button(wedget,text="Network Class A",bd=0, font=("Bold",4),bg="#FFFFFF",fg="#1b1b1b",highlightthickness=2,highlightbackground="#1b1b1b",activebackground="#1b1b1b",activeforeground="#FFFFFF",width=7,command= lambda : network_proses(uwo))
	subnetmask_button.pack(side=LEFT,padx=10)
	
	subnetmask_button = Button(wedget,text="Network Class B",bd=0, font=("Bold",4),bg="#FFFFFF",fg="#1b1b1b",highlightthickness=2,highlightbackground="#1b1b1b",activebackground="#1b1b1b",activeforeground="#FFFFFF",width=7,command= lambda : network_proses(uwo1))
	subnetmask_button.pack(side=LEFT,padx=10)
	
	subnetmask_button = Button(wedget,text="Network Class C",bd=0, font=("Bold",4),bg="#FFFFFF",fg="#1b1b1b",highlightthickness=2,highlightbackground="#1b1b1b",activebackground="#1b1b1b",activeforeground="#FFFFFF",width=7,command= lambda : network_proses(uwo2))
	subnetmask_button.pack(side=LEFT,padx=10)
	
	
	
	wedget.pack(pady=40)
	home_apan.pack()
def network_proses(uwo):
	home_subnetmask_proses= Frame(option_border,bg="#FFFFFF")
	kokok = int(subnetmask_engtry.get())
	
	
	if uwo == 3 and kokok <= 32:
		lahiya = kokok-24
		if lahiya>-1:
			hasil2 = 2**lahiya
		
	elif uwo == 2 and kokok <= 32:
		lahiya = kokok-16
		if lahiya>-1:
			hasil2 = 2**lahiya
		
		
	elif uwo == 1 and kokok <= 32:
		lahiya = kokok-8
		
		if lahiya>-1:
			hasil2 = 2**lahiya
		
		
		
	ucupoutput = Label(home_subnetmask_proses,text=hasil2,font=("'Consolas",6,"bold"),bg="#FFFFFF",highlightthickness=2,highlightbackground="#1b1b1b",width=30)
	ucupoutput.pack(ipady=3,pady=10)
	home_subnetmask_proses.pack()
	
def delet_page():
	for frame in option_border.winfo_children():
		frame.destroy()
def utama(bronya):
	delet_page()
	bronya()
	
	
option_frame = Frame(root,bg="black")

btn5 = Button(option_frame,text="Subnetmask",bd=0, font=("Bold",4),bg="#1b1b1b",fg="#E4E4E4",command=lambda : utama(subnetmask))
btn5.place(x=20, y=50)

btn5 = Button(option_frame,text="    Host ID      ",bd=0, font=("Bold",4),bg="#1b1b1b",fg="#E4E4E4",command=lambda : utama(apan))
btn5.place(x=20, y=150)

btn5 = Button(option_frame,text="  Network ID",bd=0, font=("Bold",4),bg="#1b1b1b",fg="#E4E4E4",command=lambda : utama(network))
btn5.place(x=20, y=250)

btn5 = Button(option_frame,text="   Dashboard",bd=0, font=("Bold",4),bg="#1b1b1b",fg="#E4E4E4")
btn5.place(x=20, y=350)

option_frame.pack(side=LEFT)
option_frame.pack_propagate(False)
option_frame.configure(width=250,height=800)

option_border = Frame(root,highlightbackground="black",highlightthickness=2,bg="#FFFFFF")

option_border.pack(side=LEFT)
option_border.pack_propagate(False)
option_border.configure(width=700,height=800)
network()
root.mainloop()
