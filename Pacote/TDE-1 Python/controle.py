from tkinter import *

import mysql.connector

con = mysql.connector.connect(host='localhost', database='cadastro1',user='root',password='*******')

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor mysql", db_info)

def cadastrar_cliente():
    cursorauxiliar=con.cursor()
    cursorauxiliar.execute(f"insert into dados (nome, email) values ('{en_nome.get()}','{en_email.get()}')")
    con.commit()
    con.close()

master= Tk() 

master.title ("ADS-IMEPAC")
master.geometry("700x600")
master.resizable(width=1,height=1)


img_fundo=PhotoImage(file="imagens\\Cadastro.png") 
img_botao=PhotoImage(file="imagens\\ENVIAR.png")


lab_fundo=Label(master,image=img_fundo)
lab_fundo.pack()

en_nome=Entry(master,bd=2,font="calibri,15",justify=CENTER)
en_nome.place(width=480,height=54,x=150,y=223)


en_email=Entry(master,bd=2,font="calibri,15",justify=CENTER)
en_email.place(width=480,height=54,x=150,y=360)


bt_enviar=Button(master,bd=0, command=cadastrar_cliente,image=img_botao)
bt_enviar.place(width=175,height=117,x=263,y=447)








master.mainloop() 


