from tkinter import*
import math,random
import os
from tkinter import messagebox
class Bill_App:
   
        
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1385x700+0+0")
        self.root.title("Billing Software")
        bg_color="#074463"
        title=Label(self.root,text="Billing Software",bd=12,relief=GROOVE,bg=bg_color,fg="white",font=("Algerian",25,"bold"),pady=2).pack(fill=X)

        


        self.c_name=StringVar()
        self.c_phn=StringVar()
        self.bill_no=StringVar()
        x=random.randint(100,999)
        self.bill_no.set(str(x))
        self.search_bill=StringVar()

        self.tea=IntVar()
        self.masala=IntVar()
        self.hotc=IntVar()
        self.coldc=IntVar()
        self.milk=IntVar()

        self.shahi=IntVar()
        self.kadhi=IntVar()
        self.tandoori=IntVar()
        self.garlic=IntVar()
        self.laccha=IntVar()

        
        self.plat=IntVar()
        self.spring=IntVar()
        self.manchu=IntVar()
        self.frank=IntVar()
        self.sweet=IntVar()

        self.tea_price=StringVar()
        self.main_price=StringVar()
        self.starter_price=StringVar()

        self.tea_tax=StringVar()
        self.starter_tax=StringVar()
        self.main_tax=StringVar()



        

        

        
        #======================customer frame===============
        
        F1=LabelFrame(self.root,bd=10,text="Customer Details",font=("Algerian",15,"bold"),fg="gold",bg=bg_color)
        F1.place(x=0,y=80,relwidth=1)
        cname_lbl=Label(F1,text="Customer Details",font=("Algerian",12,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=15,textvariable=self.c_name,font="airal 12",bd=7,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=5)

        cphn_lbl=Label(F1,text="Customer Phon no:",font=("Algerian",12,"bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=20,pady=5)
        cphn_txt=Entry(F1,width=15,textvariable=self.c_phn,font="airal 12",bd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=5)

        cbill_lbl=Label(F1,text="Bill No:",font=("Algerian",12,"bold"),bg=bg_color,fg="white").grid(row=0,column=4,padx=20,pady=5)
        cbill_txt=Entry(F1,width=15,textvariable=self.bill_no,font="airal 12",bd=7,relief=SUNKEN).grid(row=0,column=5,pady=5,padx=5)
        
        bill_btn=Button(F1,text="Search",command=self.find_bill,width=10,bd=7,font="arial 12 bold").grid(row=0,column=6,padx=30,pady=10)


        #======================TEA&COFFEE frame===============

        F2=LabelFrame(self.root,bd=10,text="TEA&COFFEE",font=("Algerian",15,"bold"),fg="gold",bg=bg_color)
        F2.place(x=5,y=170,width=290,height=320)

        tea_lbl=Label(F2,text="TEA",font=("Algerian",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        tea_txt=Entry(F2,width=5,textvariable=self.tea,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        masalat_lbl=Label(F2,text="MASALA TEA",font=("Algerian",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        masalat_txt=Entry(F2,width=5,textvariable=self.masala,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        hotc_lbl=Label(F2,text="HOT COFFEE",font=("Algerian",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        hotc_txt=Entry(F2,width=5,textvariable=self.hotc,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        coldc_lbl=Label(F2,text="COLD COFFEE",font=("Algerian",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        coldc_txt=Entry(F2,width=5,textvariable=self.coldc,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        milk_lbl=Label(F2,text="MILK",font=("Algerian",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        milk_txt=Entry(F2,width=5,textvariable=self.milk,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)



        #======================MainCourse frame===============

        F3=LabelFrame(self.root,bd=10,text="Main Cours",font=("Algerian",15,"bold"),fg="gold",bg=bg_color)
        F3.place(x=305,y=170,width=315,height=320)

        shahi_lbl=Label(F3,text="Shahi Paneer",font=("Algerian",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        shahi_txt=Entry(F3,width=5,textvariable=self.shahi,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        kadhi_lbl=Label(F3,text="Kadhi Paneer",font=("Algerian",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        kadhi_txt=Entry(F3,width=5,textvariable=self.kadhi,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        tandoori_lbl=Label(F3,text="Tandoori Roti",font=("Algerian",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        tandoori_txt=Entry(F3,width=5,textvariable=self.tandoori,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        garlic_lbl=Label(F3,text="Garlic Naan",font=("Algerian",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        garlic_txt=Entry(F3,width=5,textvariable=self.garlic,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        laccha_lbl=Label(F3,text="Laccha Paratha",font=("Algerian",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        laccha_txt=Entry(F3,width=5,textvariable=self.laccha,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)



        #======================Starter frame===============

        F4=LabelFrame(self.root,bd=10,text="STARTERS",font=("Algerian",15,"bold"),fg="gold",bg=bg_color)
        F4.place(x=625,y=170,width=335,height=320)

        plat_lbl=Label(F4,text="Platter",font=("Algerian",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        plat_txt=Entry(F4,width=5,textvariable=self.plat,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=10)

        spring_lbl=Label(F4,text="Spring Roll",font=("Algerian",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        spring_txt=Entry(F4,width=5,textvariable=self.spring,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=10)

        manchu_lbl=Label(F4,text="Manchurian",font=("Algerian",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        manchu_txt=Entry(F4,width=5,textvariable=self.manchu,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=10)

        fran_lbl=Label(F4,text="Frankie",font=("Algerian",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        fran_txt=Entry(F4,width=5,textvariable=self.frank,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10,pady=10)

        sweet_lbl=Label(F4,text="Sweet Corn",font=("Algerian",15,"bold"),bg=bg_color,fg="lightgreen").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        sweet_txt=Entry(F4,width=5,textvariable=self.sweet,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10,pady=10)


        #======================Billing frame===============

        F5=Frame(self.root,bd=10,relief=GROOVE)
        F5.place(x=965,y=170,width=395,height=315)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE).pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.textarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)

        
        #======================Footer frame===============

        F7=Frame(self.root,bd=6,relief=GROOVE,bg=bg_color)
        F7.place(x=0,y=650,relwidth=1,height=50)
        title=Label(F7,text="THANK YOU",bd=2,relief=GROOVE,bg=bg_color,fg="white",font=("Algerian",15,"bold"),pady=2).pack(fill=X)




        #=================Button frame=========================
        F6=LabelFrame(self.root,bd=10,relief=GROOVE,text="BILL MENU",font=("times new roman",15,"bold"),fg="gold",bg=bg_color)
        F6.place(x=0,y=500,relwidth=1,height=155)

        m1_lbl=Label(F6,text="Total Tea&Coffee Price:",font=("arial",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=0,padx=10,pady=1,sticky="w")
        m1_txt=Entry(F6,width=7,textvariable=self.tea_price,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10,pady=1)

        m2_lbl=Label(F6,text="Total Main cours Price:",font=("arial",14,"bold"),bg=bg_color,fg="white").grid(row=1,column=0,padx=10,pady=1,sticky="w")
        m2_txt=Entry(F6,width=7,textvariable=self.main_price,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10,pady=1)

        m3_lbl=Label(F6,text="Total Starter Price:",font=("arial",14,"bold"),bg=bg_color,fg="white").grid(row=2,column=0,padx=10,pady=1,sticky="w")
        m3_txt=Entry(F6,width=7,textvariable=self.starter_price,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

        t1_lbl=Label(F6,text="Tea&Coffee Tax:",font=("arial",14,"bold"),bg=bg_color,fg="white").grid(row=0,column=2,padx=20,pady=1,sticky="w")
        t1_txt=Entry(F6,width=7,textvariable=self.tea_tax,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=3,padx=10,pady=1)

        t2_lbl=Label(F6,text="Starter Tax:",font=("arial",14,"bold"),bg=bg_color,fg="white").grid(row=1,column=2,padx=20,pady=1,sticky="w")
        t2_txt=Entry(F6,width=7,textvariable=self.starter_tax,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=3,padx=10,pady=1)

        t3_lbl=Label(F6,text="Main Course Tax:",font=("arial",14,"bold"),bg=bg_color,fg="white").grid(row=2,column=2,padx=20,pady=1,sticky="w")
        t3_txt=Entry(F6,width=7,textvariable=self.main_tax,font=("Algerian",15,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=3,padx=10,pady=1)


        btn_F=Frame(F6,bd=7,relief=GROOVE)
        btn_F.place(x=710,width=600,height=110)

        t_btn=Button(btn_F,text="TOTAL",command=self.total,font=("arial",15,"bold"),bd=5,bg="cadetblue",fg="white",width=10,height=2).grid(row=0,column=0,padx=5,pady=13)
        gb_btn=Button(btn_F,text="Generate Bill",command=self.bill_area,font=("arial",15,"bold"),bd=5,bg="cadetblue",fg="white",width=10,height=2).grid(row=0,column=1,padx=5,pady=13)
        clear_btn=Button(btn_F,command=self.clear_data,text="Clear",font=("arial",15,"bold"),bd=5,bg="cadetblue",fg="white",width=10,height=2).grid(row=0,column=2,padx=5,pady=13)
        exit_btn=Button(btn_F,text="Exit",font=("arial",15,"bold"),bd=5,bg="cadetblue",fg="white",width=10,height=2).grid(row=0,column=3,padx=5,pady=13)
        

    def total(self):
        self.t_t_p=self.tea.get()*15
        self.t_m_p=self.masala.get()*20
        self.t_h_p=self.hotc.get()*25
        self.t_c_p=self.coldc.get()*30
        self.t_m_p=self.milk.get()*10
        self.total_tea_price=float(
                                    self.t_t_p+
                                    self.t_m_p+
                                    self.t_h_p+
                                    self.t_c_p+
                                    self.t_m_p
                                )
        self.tea_price.set("Rs:"+str(self.total_tea_price))
        self.t_tax=round((self.total_tea_price*0.05),2)
        self.tea_tax.set("Rs:"+str(self.t_tax))

        self.m_s_p=self.shahi.get()*150
        self.m_k_p=self.kadhi.get()*200
        self.m_t_p=self.tandoori.get()*16
        self.m_g_p=self.garlic.get()*36
        self.m_l_p=self.laccha.get()*50

        self.total_main_price=float(
                                    self.m_s_p+
                                    self.m_k_p+
                                    self.m_t_p+
                                    self.m_g_p+
                                    self.m_l_p
                                 )
        self.main_price.set("Rs:"+str(self.total_main_price))
        self.m_tax=round((self.total_main_price*0.10),2)
        self.main_tax.set("Rs:"+str(self.m_tax))

        self.s_p_p=self.plat.get()*120
        self.s_s_p=self.spring.get()*200
        self.s_m_p=self.manchu.get()*150
        self.s_f_p=self.frank.get()*60
        self.s_sw_p=self.sweet.get()*60

        self.total_starter_price=float(
                                        self.s_p_p+
                                        self.s_s_p+
                                        self.s_m_p+
                                        self.s_f_p+
                                        self.s_sw_p
                                    )
        self.starter_price.set("Rs:"+str(self.total_starter_price))
        self.s_tax=round((self.total_starter_price*0.5),2)
        self.starter_tax.set("Rs:"+str(self.s_tax))

        self.Total_bill=float( self.total_tea_price+
                               self.total_main_price+
                               self.total_starter_price+
                               self.t_tax+
                               self.m_tax+
                               self.s_tax
                             )

        

    def welcome_bill(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"\t Welcome A.P Restaurant\n")
        self.textarea.insert(END,f"\n Bill No: {self.bill_no.get()}")
        self.textarea.insert(END,f"\n Customer Name: {self.c_name.get()}")
        self.textarea.insert(END,f"\n Phone Number: {self.c_phn.get()}")
        self.textarea.insert(END,f"\n============================================")
        self.textarea.insert(END,f"\nOrders\t\t\tQTY\t\tRs:")
        self.textarea.insert(END,f"\n============================================")

    def bill_area(self):

        if self.c_name.get()=="":
            messagebox.showerror("ERROR","Customer Details Are Must")
        else:
             self.welcome_bill()

             if self.tea.get()!=0:
                 self.textarea.insert(END,f"\n TEA\t\t\t{self.tea.get()}\t\t{self.t_t_p}")
             if self.hotc.get()!=0:
                 self.textarea.insert(END,f"\n Hot Coffee\t\t\t{self.hotc.get()}\t\t{self.t_h_p}")
             if self.coldc.get()!=0:
                 self.textarea.insert(END,f"\n Cold Coffee\t\t\t{self.coldc.get()}\t\t{self.t_c_p}")
             if self.masala.get()!=0:
                 self.textarea.insert(END,f"\n Masala Tea\t\t\t{self.coldc.get()}\t\t{self.t_c_p}")
             if self.milk.get()!=0:
                 self.textarea.insert(END,f"\n Milk\t\t\t{self.milk.get()}\t\t{self.t_m_p}")

             if self.shahi.get()!=0:
                 self.textarea.insert(END,f"\n Shahi Pannir\t\t\t{self.shahi.get()}\t\t{self.m_s_p}")
             if self.kadhi.get()!=0:
                 self.textarea.insert(END,f"\n Kadhi Pannir\t\t\t{self.kadhi.get()}\t\t{self.m_k_p}")
             if self.tandoori.get()!=0:
                 self.textarea.insert(END,f"\n Tandoori\t\t\t{self.tandoori.get()}\t\t{self.m_t_p}")
             if self.garlic.get()!=0:
                 self.textarea.insert(END,f"\n Garlic Nan\t\t\t{self.garlic.get()}\t\t{self.m_g_p}")
             if self.laccha.get()!=0:
                 self.textarea.insert(END,f"\n Laccha Paratha\t\t\t{self.laccha.get()}\t\t{self.m_l_p}")


             if self.plat.get()!=0:
                 self.textarea.insert(END,f"\n Platter\t\t\t{self.plat.get()}\t\t{self.s_p_p}")
             if self.spring.get()!=0:
                 self.textarea.insert(END,f"\n Hot Spring Roll\t\t\t{self.spring.get()}\t\t{self.s_s_p}")
             if self.manchu.get()!=0:
                 self.textarea.insert(END,f"\n Manchurian\t\t\t{self.manchu.get()}\t\t{self.s_m_p}")
             if self.frank.get()!=0:
                 self.textarea.insert(END,f"\n Masala Tea\t\t\t{self.frank.get()}\t\t{self.s_f_p}")
             if self.sweet.get()!=0:
                 self.textarea.insert(END,f"\n Sweet Corn\t\t\t{self.sweet.get()}\t\t{self.s_sw_p}")


             self.textarea.insert(END,f"\n--------------------------------------------")
             if self.tea_tax.get()!="Rs:  0.0":
                 self.textarea.insert(END,f"\nTea Tax\t\t\t\t{self.tea_tax.get()}")

             if self.main_tax.get()!="Rs:  0.0":
                 self.textarea.insert(END,f"\nMain Course Tax\t\t\t\t{self.main_tax.get()}")

             if self.starter_tax.get()!="Rs:  0.0":
                 self.textarea.insert(END,f"\nstarter Tax\t\t\t\t{self.starter_tax.get()}")

       
             self.textarea.insert(END,f"\nTotal Bill:\t\t\t\t{str(self.Total_bill)}")
             self.textarea.insert(END,f"\n-------------------------------------------")
             self.save_bill()

      
    def save_bill(self):
         op=messagebox.askyesno("Save Bill","do you want to save the bill?")
         if op>0:
             self.bill_data=self.textarea.get('1.0',END)
             f1=open("bills/"+str(self.bill_no.get())+".txt","w")
             f1.write(self.bill_data)
             f1.close()
             messagebox.showinfo("Saved",f"Bill no.: {self.bill_no.get()}saved successfully")
         else:
              return


    def find_bill(self):
        present="no"
        for i in os.listdir("bills/"):
            if i.split('.')[0]==self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.textarea.delete('1.0',END)
                for d in f1:
                    self.textarea.insert(END,d)
                f1.close()
                present="yes"
        if present=="no":
            messagebox.showerror("Error","Invalid Bill no")


    def clear_data(self):
        self.c_name.set("")
        self.c_phn.set("")
        self.bill_no.set("")
        x=random.randint(100,999)
        self.bill_no.set(str(x))
        self.search_bill.set("")
        
        self.tea.set(0)
        self.masala.set(0)
        self.hotc.set(0)
        self.coldc.set(0)
        self.milk.set(0)

        self.shahi.set(0)
        self.kadhi.set(0)
        self.tandoori.set(0)
        self.garlic.set(0)
        self.laccha.set(0)

        
        self.plat.set(0)
        self.spring.set(0)
        self.manchu.set(0)
        self.frank.set(0)
        self.sweet.set(0)

        self.tea_price.set(0)
        self.main_price.set(0)
        self.starter_price.set(0)

        self.tea_tax.set("")
        self.starter_tax.set("")
        self.main_tax.set("")
        self.welcome_bill()

                
       

root = Tk()
obj = Bill_App(root)
root.mainloop()
