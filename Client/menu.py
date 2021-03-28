import os, sys
import tkinter as tk
from tkinter import *
import requests
import json

productList = []
company = ""
product = []
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)
        self.geometry('500x500')
        self.title("Revelio")
        self.configure(background='red')
        self.resizable(False, False)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
        

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, background='red')
        tk.Label(self, text="Revelio", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self, text = 'Enter a company and product to find vulnerabilites', font=('Helvetica',10, 'bold')).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Enter a serial number", height=2, width=50, font=('Helvetica',10, 'bold'),
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="Enter a company and product ID", height=2, width=50, font=('Helvetica',10, 'bold'),
                  command=lambda: master.switch_frame(PageTwo)).pack()
        tk.Button(self, text="Choose a company and product ID", height=2, width=50, font=('Helvetica',10, 'bold'),
                  command=lambda: master.switch_frame(PageThree)).pack()
        
        

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Serial Number Search", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        serialNumber_var=tk.StringVar()
        
        def submit():
            serialNumber=serialNumber_var.get()
            print("The serial number is : " + serialNumber)
            serialNumber_var.set("")
            selected(serialNumber)
            

            
        def selected(serialNumber):
            global company
            company = "netgear"
            product = "http://cve.revelio.space:8080/find/netgear/%s" % (serialNumber)
            x = requests.get(product)
            product = x.text
            productURL = "http://cve.revelio.space:8080/search/%s/%s" % (company, product)
            z = requests.get(productURL)
            y = json.loads(z.text)
            
            print("Company: " + str(company) + " ProductID: " + product)
            count = 0
            for j in y:
                if count % 5 == 0:
                    print("\n")
                if count % 5 == 1:
                    print("CVSS: ",end = '')
                if count % 5 == 2:
                    print("Description: ",end = '')
                if count % 5 == 3:
                    print("Last (major) update: ",end = '')
                if count % 5 == 4:
                    print("Published: ",end = '')
                print(str(j))
                count = count + 1
            print("\n")
            
        
        serialNumber_label = tk.Label(self, text = 'Serial Number', font=('calibre',10, 'bold')).pack()
        serialNumber_entry = tk.Entry(self,textvariable = serialNumber_var, font=('calibre',10,'normal')).pack()
        sub_btn=tk.Button(self,text = 'Submit', height=2, width=10, command = submit).pack()
        tk.Button(self, text="Go back to start page", height=2, width=20,
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        company_var=tk.StringVar()
        productID_var=tk.StringVar()
        
        company = ""
        
        def submit():
            company=company_var.get()
            productID=productID_var.get()
            
            print("The company is : " + company)
            print("The productID is : " + productID)
            company_var.set("")
            productID_var.set("")
        entry_label = tk.Label(self, text = 'Enter a company and product to find vulnerabilites', font=('calibre',10, 'bold'))
        company_label = tk.Label(self, text = 'Company and Product Search', font=('calibre',10, 'bold')).pack()
  
        # creating a entry for input
        # name using widget Entry
        company_entry = tk.Entry(self,textvariable = company_var, font=('calibre',10,'normal')).pack()
  
        # creating a label for password
        productID_label = tk.Label(self, text = 'Product ID', font = ('calibre',10,'bold')).pack()
  
        # creating a entry for password
        productID_entry=tk.Entry(self, textvariable = productID_var, font = ('calibre',10,'normal')).pack()
  
        # creating a button using the widget
        # Button that will call the submit function
        sub_btn=tk.Button(self,text = 'Submit', height=2, width=10, command = submit).pack()


  
        # placing the label and entry in
        # the required position using grid
        # method
        tk.Button(self, text="Go back to start page", height=2, width=20,
                  command=lambda: master.switch_frame(StartPage)).pack()
        
class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Company Search", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        l = ('amazon',
            'apple',
            'asus',
            'android',
            'cisco',
            'google',
            'lg',
            'linksys',
            'microsoft',
            'netgear',
            'oneplus',
            'samsung',
            'tp-link' )
        
        def checkkey(event):
            value = event.widget.get()
            #print(value)
            # get data from l
            if value == '':
                data = l
            else:
                data = []
                for item in l:
                        if value.lower() in item.lower():
                                data.append(item)                               

            # update data in listbox
            update(data)


        def update(data):
            # clear previous data
            lb.delete(0, 'end')
            # put new data
            for item in data:
                lb.insert('end', item)
        

        def nextPage():
            global productList
            if productList:
                master.switch_frame(PageThreeTwo)
        
        def selected():
            global productList
            global company
            selection = lb.curselection()
            company = lb.get(ACTIVE)
            for i in selection:
                brandURL = "https://cve.circl.lu/api/browse/%s" % (lb.get(i))
                x = requests.get(brandURL)
                y = json.loads(x.text)
                productList = list( y['product'] )
            if company:
                nextPage()
            
        

                
        e = Entry(self)
        e.bind('<KeyRelease>', checkkey)
        e.pack()

        #creating list box
        lb = Listbox(self)
        lb.pack()
        update(l)
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y, anchor=NW)
        lb.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = lb.yview)
        myButton = Button(self, text="Select", height=2, width=10, command=selected)
        myButton.pack()
        tk.Button(self, text="Go back to start page", height=2, width=20,
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageThreeTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Product Search", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        
        def checkkey(event):
            value = event.widget.get()
            #print(value)
            # get data from l
            if value == '':
                data = productList
            else:
                data = []
                for item in productList:
                        if value.lower() in item.lower():
                                data.append(item)                               

            # update data in listbox
            update(data)


        def update(data):
            # clear previous data
            lb.delete(0, 'end')
            # put new data
            for item in data:
                lb.insert('end', item)
        
        def selected():
            selection = lb.curselection()
            for i in selection:
                productURL = "http://cve.revelio.space:8080/search/%s/%s" % (company, lb.get(i) )
                x = requests.get(productURL)
                y = json.loads(x.text)
                print("Company: " + str(company) + " ProductID: " + lb.get(i))
                count = 0
                for j in y:
                    if count % 5 == 0:
                        print("\n")
                    if count % 5 == 1:
                        print("CVSS: ",end = '')
                    if count % 5 == 2:
                        print("Description: ",end = '')
                    if count % 5 == 3:
                        print("Last (major) update: ",end = '')
                    if count % 5 == 4:
                        print("Published: ",end = '')
                    print(str(j))
                    count = count + 1
                print("\n")
                

             
                
        
        e = Entry(self)
        e.bind('<KeyRelease>', checkkey)
        e.pack()

        #creating list box
        lb = Listbox(self, selectmode = "multiple")
        lb.pack()
        update(productList)
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y, anchor=NW)
        lb.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = lb.yview)
        myButton = Button(self, text="Select", height=2, width=10, command=selected)
        myButton.pack()
        tk.Button(self, text="Go back to company selection", height=2, width=30,
                  command=lambda: master.switch_frame(PageThree)).pack()
        tk.Button(self, text="Go back to start page", height=2, width=20,
                  command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
