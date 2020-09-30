from tkinter import*
from tkinter import messagebox
import googletrans
from tkinter.ttk import Combobox
from textblob import TextBlob
#Functions===============================
ln_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 
'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 
'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 
'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}
def Exit_func():
    rr = messagebox.askyesno("Notification","Are you sure you want to exit?")
    if rr==True:
          root.destroy()
def translate_func():
    dict1 = googletrans.LANGUAGES
    dict2 = {}
    #for i in dict1.items():
    #    dict2[i[1]] = i[0]
    #print(dict2)
    try:
        word3 = TextBlob(l1_txt.get())
        lan = word3.detect_language()
        lan_todict = languages.get()
        lan_to = ln_dict[lan_todict]
        word3 = word3.translate(from_lang=lan,to=lan_to)
        sp = word3.split()
        var2.set(word3)
    except:
        var2.set("Try any other word or sentence.")    
def translate_fn(e):
    dict1 = googletrans.LANGUAGES
    dict2 = {}
    #for i in dict1.items():
    #    dict2[i[1]] = i[0]
    #print(dict2)
    try:
        word3 = TextBlob(l1_txt.get())
        lan = word3.detect_language()
        lan_todict = languages.get()
        lan_to = ln_dict[lan_todict]
        word3 = word3.translate(from_lang=lan,to=lan_to)
        var2.set(word3)
    except:
        var2.set("Try any other word or sentence.")       
def l1_enter(e):
    trans_btn.config(bg="gold")
def l1_leave(e):
    trans_btn.config(bg="white")
def l2_enter(e):
    Exit_btn.config(bg="gold")
def l2_leave(e):
    Exit_btn.config(bg="red")
root = Tk()
root.title("Translator")
root.geometry("600x450+300+100")
root.config(bg="purple3")
root.resizable(False,False)
root.wm_iconbitmap("E:\Python projects - G\Translator\icont.ico")

var2 = StringVar()
head_f  = Frame(root,bd=10,relief=SUNKEN,bg="green3")
head_f.place(width=600,height=50)
#Photos======================================
translate_image = PhotoImage(file="E:\\Python projects - G\\Translator\\translate.png")
translate_image = translate_image.subsample(2,2)

Exit_image = PhotoImage(file="E:\Qr code generator\cancel.png")
Exit_image = Exit_image.subsample(18,18)
#Labels=========================================
head_l = Label(head_f,text="Translator",fg="blue",bg="green3",font=("times new roman","20","italic bold"))
head_l.pack()

l1 = Label(root,text="Enter the text:",fg="orange",bg="purple3",font=("times","17"," bold"))
l1.place(x=10,y=80)

l2 = Label(root,text="Text Translated:",fg="orange",bg="purple3",font=("times","17"," bold"))
l2.place(x=10,y=160)

#l3 = Label(root,text="Choose languages:",fg="white",bg="purple3",font=("times","17","underline bold"))
#l3.place(x=10,y=300)

languages = StringVar()
font_box = Combobox(root,width=15,textvariable=languages,state="readonly")
font_box["values"] = [e for e in ln_dict.keys()]
font_box.current(37)
font_box.place(x=436,y=200)
#Entries============================================
l1_txt = Entry(root,bg="pink",bd="10",relief=SUNKEN,font=("times","15"," bold"))
l1_txt.place(x=200,y=80,width=350,height=40)

l2_txt = Entry(root,textvariable=var2,bg="cyan",bd="10",relief=SUNKEN,font=("times","15"," bold"))
l2_txt.place(x=200,y=160,width=350,height=40)
#Buttons====================
trans_btn = Button(root,text="Translate",bg="white",font=("times new roman","8","italic bold"),bd=10,relief=GROOVE,compound=RIGHT,image=translate_image,command=translate_func)
trans_btn.place(x=100,y=250,width=100,height=50)

Exit_btn = Button(root,text="Exit",bg="red",font=("times new roman","8","italic bold"),bd=10,relief=GROOVE,compound=RIGHT,image=Exit_image,command=Exit_func)
Exit_btn.place(x=400,y=250,width=100,height=50)

#Binding===============================
trans_btn.bind('<Enter>',l1_enter)
trans_btn.bind('<Leave>',l1_leave)

l1_txt.bind('<Return>',translate_fn)

Exit_btn.bind('<Enter>',l2_enter)
Exit_btn.bind('<Leave>',l2_leave)
root.mainloop()