from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

listm=[["101A","Brown rice",50,45.50,41.25],["102B","Whole wheat",30,27.45,21.50],
       ["102C","Tomato sauce",25.50,20.25,18.70],["103D","Mustard",40,39.45,37],
       ["104E","Barbecue sauce",45,43,41.50],["105F","Red-wine vinegar",4000,3800,3750],
       ["106G"	,"Salsa",200,189.50,170],["107H","Extra virgin olive oil",500,478.50,455.70],
       ["108I","canola oil"	,200,180,118],["109J","Hot pepper sauce",100,98.50,91.25],
       ["110K","Bananas",60,55,50],["111L","Apples",300,250,120],["112M","Orange",200,140,110],["113N","Mangoes",100,80,50],["114O","Strawberries",100,90	,80],["115P","Blueberries",95,80,75],["116Q","Green teas",250,225,200],
       ["117R","Sparkling water",20,14.50,11],["118S","Dried apricots",270,250,230],
       ["119T","Dried figs",100,95,90],["120U","Dried prunes",90,85,80],["121V","Almonds"	,900,870,850],["122W","Cashews",1000,950,910],["123X","Walnuts",800,770,	720],["124Y","Peanuts",400,380,360],["125Z","Pecans",350,320,300],
       ["201A","Pistachios",1200,1180,1160],["202B","Sunflower seeds",150,112.50,103.45],
       ["203C","Sesame seeds",120.50,110.25,101.40],["204D","Whole flaxseeds",95.20,90.45,89.20]]


global count
global discp
global tprice
tprice=0
discp=0
count=0
def add_product():
    add_id=options1.get()
    add_quality=int(options2.get())
    add_quantity=float(quantity.get())
    add_user=str(options3.get())
    s1=slice(4)
    for i in range (len(listm)):
        if add_id[s1]==listm[i][0]:
            list_add=listm[i]


    if add_quality==1:
        rate=list_add[2]
    elif add_quality==2:
        rate=list_add[3]
    elif add_quality==3:
        rate=list_add[4]
    amount=round(rate*add_quantity,3)

    global count
    mytable.insert(parent='',index='end',iid = count,text='',values=((count+1),list_add[0],list_add[1],add_quality,add_quantity,rate,amount))
    count += 1
    global discp
    global tprice
    tprice+=amount
    discp=tprice
    if tprice>=10000:
        if add_user=="Guest User":
            discp=(0.99*tprice)
            label3=Label(root,text="Discount Applied = 1%",bg="#e0da84",font=("Bahnschrift Condensed", 16)).place(x=1200,y=900)
        else :
            discp=(0.988*tprice)
            label4=Label(root,text="Discount Applied = 1.2%",bg="#e0da84",font=("Bahnschrift Condensed", 16)).place(x=1200,y=900)
    discps="Total Price ₹"+str(discp)
    total.set(discps)
    return None
def quit1():
    root.destroy()

root=ThemedTk(theme="adapta")
#root.get_themes()
#root.set_theme("adapta")
#root.attributes('-fullscreen',True)
root.title("Grocery Shop")
root.geometry("1920x1000")
root.iconbitmap('icon.ico')
bg = PhotoImage(file="background2.png")
background_image = Label(root,image=bg)
background_image.place(x = 0, y = 0)

#Title

title=ttk.Label(root,text="Billing Software",font=("Blackadder ITC", 35),borderwidth='5', relief="raised").place(x=830,y=5)
#title= Label(root,text="Billing Software",font=("Blackadder ITC", 35),fg="#c91c48",borderwidth='5', relief="raised").place(x=830,y=5)
#menu for Registerd User

user_name=["Guest User","Surian - AAA1001","Nila - AAA1002","Arivazhagan - AAA1003","Nithin Kumar - AAA1004","Aravind - AAA1005"]
options3= StringVar()
options3.set("Select Your User ID")
drop3= OptionMenu(root,options3,*user_name)
drop3.configure(width=60,height=2,bg="#b8e0e0")
drop3["menu"].config(bg="RED")
drop3.place(x=130,y=170)

#Menu for Product code
product_id = ["101A - Brown rice","102B - Whole wheat","102C - Tomato sauce","103D - Mustard",
              "104E - Barbecue sauce","105F - Red-wine vinegar","106G - Salsa",
              "107H - Extra virgin olive oil","108I - canola oil","109J - Hot pepper sauce",
              "110K - Bananas","111L - Apples","112M - Oranges","113N - Mangoes","114O - Strawberries",
              "115P - Blueberries","116Q - Green teas","117R - Sparkling water","118S - Dried apricots",
              "119T - Dried figs","120U	- Dried prunes","121V - Almonds","122W - Cashews","123X	- Walnuts",
              "124Y - Peanuts","125Z - Pecans","201A - Pistachios","202B - Sunflower seeds","203C - Sesame seeds",
              "204D - Whole flaxseeds"]
options1= StringVar()
options1.set("Select Your Product Code")
drop1= OptionMenu(root,options1,*product_id)
drop1.configure(width=60,height=2,bg="#b8e0e0")
drop1.place(x=620,y=170)

#menu for Quality

quality=["1","2","3"]
options2= StringVar()
options2.set("Select Your Prefered Quality")
drop2= OptionMenu(root,options2,*quality)
drop2.configure(width=60,height=2,bg="#b8e0e0")
drop2.place(x=1100,y=170)

#quantity Entry box

label1=ttk.Label(root,text="Enter your Quantity in KG",font=("Algerian",9)).place(x=1630,y=170)
quantity=StringVar()
quantity_entry=ttk.Entry(root,textvariable = quantity,width=35).place(x=1600,y=192)
#label1=Label(root,text="Enter your Quantity in KG",bg="#b8e0e0",font=("Algerian",9)).place(x=1630,y=170)
#quantity_entry=Entry(root,textvariable = quantity,width=35,bg="#b8e0e0").place(x=1600,y=192)
#table

table_frame=Frame(root)
table_frame.config(bg="white",height=5)
table_frame.place(x=320,y=450)
table_scroll = Scrollbar(table_frame)
table_scroll.pack(side=RIGHT, fill=Y)
mytable=ttk.Treeview(table_frame,yscrollcommand=table_scroll.set)
s = ttk.Style()
s.configure('Treeview', rowheight=34, height=0 ,bg="#0d0d07",fg="#fafa50")
mytable.pack()
table_scroll.config(command=mytable.yview)

mytable['columns']=('sno','productid','name','quality','quantity','rate','amount')
mytable.column("#0", width=0,  stretch=NO)
mytable.column("sno",anchor=CENTER, width=100)
mytable.column("productid",anchor=CENTER,width=190)
mytable.column("name",anchor=CENTER,width=190)
mytable.column("quality",anchor=CENTER,width=190)
mytable.column("quantity",anchor=CENTER,width=190)
mytable.column("rate",anchor=CENTER,width=190)
mytable.column("amount",anchor=CENTER,width=190)

mytable.heading("#0",text="",anchor=CENTER)
mytable.heading("sno",text="S No.",anchor=CENTER)
mytable.heading("productid",text="Product ID",anchor=CENTER)
mytable.heading("name",text="Product Name",anchor=CENTER)
mytable.heading("quality",text="Quality",anchor=CENTER)
mytable.heading("quantity",text="Quantity",anchor=CENTER)
mytable.heading("rate",text="Rate",anchor=CENTER)
mytable.heading("amount",text="Amount",anchor=CENTER)



#add product button

total = StringVar()
total.set("Total Price ₹0")
#button1=ttk.Button(root, text="Add Product",command=add_product).place(x=940,y=300)
button1=Button(root, text="Add Product",bg="#25c225",command=add_product,height=2).place(x=940,y=300)
#total price label

label2= Label(root,textvariable=total,bg="#e0da84",font=("Bahnschrift Condensed", 16)).place(x=1450,y=900)

#Exit button
button_exit= Button(root, text="Exit Program",command=quit1).place(x=1841,y=0)

root.mainloop()
