from tkinter import *
from tkinter import messagebox
import main_01 
from pprint import *
from tkhtmlview import HTMLLabel

top=Tk()
top.title("ANIME PARSER")
top.geometry("1000x700")
top.resizable(width = False, height = False)

def get_data() : 
    main_01.main()
    all = main_01.returns_data()
    text.insert(1.0,pformat(all,width = text['width']))

def clear_data() : 
    text.delete(1.0,END)



#c = Canvas(top,bg="gray16",height=1000,width=700)
#filename = PhotoImage(file = r'ANIME_PARSER\background.png')

#background_label.place(x=0,y=0,relwidth=1,relheight=1)

#c.pack()

text = Text(top,width = 300,height = 300, wrap=WORD)  
text.place(width = 500 , height = 550 ,relx=0.5 )

btn = Button(top, text="Обновить данные", width=20, height= 5, command = get_data) 
btn.place(relx = 0.3, rely = 0.4)
btn2 = Button(top, text="Внимание!Перед повторным обновлении данных нажать сюда!!",command = clear_data )
btn2.place(relx = 0.1 , rely = 0.6)

label_info = Label(top,text="Парсер аниме сайта https://animevost.am", font=('Arial Bold',15),) 
label_info.config(bd = 0)
label_info.place(relx = 0.1 , rely = 0.1)

label_info2 = HTMLLabel(top, html= '<a href ="https://github.com/Lostskill" > Ссылка на GitHub автора</a>',fg = "blue" , cursor ="hand2")
label_info2.place(relx = 0.6 , rely= 0.9)


top.mainloop()


