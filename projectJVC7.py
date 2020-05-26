import sys
from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import *
def b3f():
    a=e.get("1.0","end-1c")
    if a=="":
        messagebox.showerror("Missing","Text Box Cannot Be Empty")
    else:
        b3_f()
def b3_f():
    a=e.get("1.0","end-1c")
    a=a.split('\n')
    v=''
    for h in a:
        if h == "'":
            v=v+""
        elif h== '[':
            v=v+''
        elif h == ']':
            v=v+''
        else:
            v=v+h
    z=v
    l=[]
    l.append(z)
    q=[]
    g=''
    for i in l:
            
        for p in i:
            if p == 'F':
                g=g+'a'
            elif p == 'C':
                g=g+'b'
            elif p == 'T':
                g=g+'c'
            elif p=='I':
                g=g+'d'
            elif p=='V':
                g=g+'e'
            elif p=='Q':
                g=g+'f'
            elif p=='W':
                g=g+'g'
            elif p=='L':
                g=g+'h'
            elif p=='Z':
                g=g+'i'
            elif p=='G':
                g=g+'j'
            elif p=='R':
                g=g+'k'
            elif p=='Y':
                g=g+'l'
            elif p=='U':
                g=g+'m'
            elif p=='X':
                g=g+'n'
            elif p=='K':
                g=g+'o'
            elif p=='A':
                g=g+'p'
            elif p=='D':
                g=g+'q'
            elif p=='B':
                g=g+'r'
            elif p=='E':
                g=g+'s'
            elif p=='H':
                g=g+'t'
            elif p=='J':
                g=g+'u'
            elif p=='M':
                g=g+'v'
            elif p=='N':
                g=g+'w'
            elif p=='P':
                g=g+'x'
            elif p=='S':
                g=g+'y'
            elif p=='O':
                g=g+'z'
            elif p=='f':
                g=g+'A'
            elif p=='c':
                g=g+'B'
            elif p=='t':
                g=g+'C'
            elif p=='i':
                g=g+'D'
            elif p=='v':
                g=g+'E'
            elif p=='q':
                g=g+'F'
            elif p=='w':
                g=g+'G'
            elif p=='l':
                g=g+'H'
            elif p=='z':
                g=g+'I'

            elif p == '%':
                g=g+'$'
            elif  p == '!':
                g=g+'@'
            elif  p == '#':
                g=g+'!'
            elif  p == '>':
                g=g+'.'
            elif  p == '<':
                g=g+','
            elif  p == ';':
                g=g+':'
            elif  p == '@':
                g=g+'?'
            elif  p == '.':
                g=g+'>'
            elif  p == ',':
                g=g+'\n'
            elif  p == '{':
                g=g+'9'
            elif  p == '}':
                g=g+'8'
            elif  p == '^':
                g=g+'7'
            elif  p == '&':
                g=g+'6'
            elif  p == '*':
                g=g+'5'
            elif  p == '(':
                g=g+'4'
            elif  p == ')':
                g=g+'3'
            elif  p == '-':
                g=g+'2'
            elif  p == '=':
                g=g+'1'
            elif  p == '+':
                g=g+'0'
            elif  p == '~':
                g=g+' '
            elif  p == 'o':
                g=g+'Z'
            elif  p == 's':
                g=g+'Y'
            elif  p == 'p':
                g=g+'X'
            elif  p == 'n':
                g=g+'W'
            elif  p == 'm':
                g=g+'V'
            elif  p == 'j':
                g=g+'U'
            elif  p == 'h':
                g=g+'T'
            elif  p == 'e':
                g=g+'S'
            elif  p == 'b':
                g=g+'R'
            elif  p == 'd':
                g=g+'Q'
            elif  p == 'a':
                g=g+'P'
            elif  p == 'k':
                g=g+'O'
            elif  p == 'x':
                g=g+'N'
            elif  p == 'u':
                g=g+'M'
            elif  p == 'y':
                g=g+'L'
            elif  p == 'r':
                g=g+'K'
            elif  p == 'g':
                g=g+'J'
            elif p == '%':
                g=g+'$'
            elif  p == '!':
                g=g+'@'
            elif  p == '#':
                g=g+'!'
            elif  p == '>':
                g=g+'.'
            elif  p == ';':
                g=g+':'
            elif  p == '@':
                g=g+'?'
            elif  p == '.':
                g=g+'>'
            elif  p == '<':
                g=g+'<'
            elif  p == '{':
                g=g+'9'
            elif  p == '}':
                g=g+'8'
            elif  p == '^':
                g=g+'7'
            elif  p == '&':
                g=g+'6'
            elif  p == '*':
                g=g+'5'
            elif  p == '(':
                g=g+'4'
            elif  p == ')':
                g=g+'3'
            elif  p == '-':
                g=g+'2'
            elif  p == '=':
                g=g+'1'
            elif  p == '+':
                g=g+'0'
            elif  p == '~':
                g=g+' '
            elif  p == 'o':
                g=g+'Z'
            elif  p == 's':
                g=g+'Y'
            elif  p == 'p':
                g=g+'X'
            elif  p == 'n':
                g=g+'W'
            elif  p == 'm':
                g=g+'V'
            elif  p == 'j':
                g=g+'U'
            elif  p == 'h':
                g=g+'T'
            elif  p == 'e':
                g=g+'S'
            elif  p == 'b':
                g=g+'R'
            elif  p == 'd':
                g=g+'Q'
            elif  p == 'a':
                g=g+'P'
            elif  p == 'k':
                g=g+'O'
            elif  p == 'x':
                g=g+'N'
            elif  p == 'u':
                g=g+'M'
            elif  p == 'y':
                g=g+'L'
            elif  p == 'r':
                g=g+'K'

                
                    
           
        q.append(g)
        g=''
    qq=q[0]
    re=messagebox.askquestion("Result","Following is your Encypted Code: \n"+qq+"\n\nDo You Want to Copy this?")
    if re=="yes":
        root.clipboard_clear()
        root.clipboard_append(qq)
        e.delete("1.0","end")
        pass
    else:
        e.delete("1.0","end")
        pass
def b1f():
    a=e.get("1.0","end-1c")

    if a=="":
        messagebox.showerror("Missing","Text Box cannot be empty")
        e.focus()
    else:
        b1_f()
def b1_f():
    a=e.get("1.0","end-1c")
    a=a.split('\n')
    q=[]
    cc=''
    g=''
    for i in a:
            
        for p in i:
            if p == 'a':
                g=g+'2F03'
            elif p == 'b':
                g=g+'C605'
            elif p == 'c':
                g=g+'85T5'
            elif p == 'd':
                g=g+'417I'
            elif p == 'e':
                g=g+"3V60"
            elif p == 'f':
                g=g+'6Q49'
            elif p == 'g':
                g=g+'202W'
            elif p == 'h':
                g=g+'83L5'
            elif p == 'i':
                g=g+'2Z02'
            elif p =='j':
                g=g+'471G'
            elif p == 'k':
                g=g+'309R'
            elif p == 'l':
                g=g+'0Y00'
            elif p == 'm':
                g=g+'106U'
            elif p == 'n':
                g=g+'9X40'
            elif p == 'o':
                g=g+'254K'
            elif p == 'p':
                g=g+'4A02'
            elif p == 'q':
                g=g+'D235'
            elif p == 'r':
                g=g+'14B7'
            elif p == 's':
                g=g+'99E2'
            elif p == 't':
                g=g+'H487'
            elif p == 'u':
                g=g+'8J30'
            elif p == 'v':
                g=g+'0M76'
            elif p == 'w':
                g=g+'5N70'
            elif p == 'x':
                g=g+'4P55'
            elif p == 'y':
                g=g+'3S07'
            elif p == 'z':
                g=g+'7O77'
            elif p == 'A':
                g=g+'2f13'
            elif p == 'B':
                g=g+'c905'
            elif p == 'C':
                g=g+'85t6'
            elif p == 'D':
                g=g+'017i'
            elif p == 'E':
                g=g+'3v60'
            elif p == 'F':
                g=g+'q629'
            elif p== 'G':
                g=g+'202w'
            elif p == 'H':
                g=g+'6l50'
            elif p == 'I':
                g=g+'2z72'
            elif p == 'J':
                g=g+'476g'
            elif  p == 'K':
                g=g+'0r39'
            elif p == 'L':
                g=g+'0y00'
            elif p == 'M':
                g=g+'102u'
            elif p == 'N':
                g=g+'3x70'
            elif p == 'O':
                g=g+'25k3'
            elif p == 'P':
                g=g+'9a02'
            elif p == 'Q':
                g=g+'d235'
            elif p == 'R':
                g=g+'14b0'
            elif  p == 'S':
                g=g+'90e3'
            elif p == 'T':
                g=g+'0h40'
            elif p== 'U':
                g=g+'0j65'
            elif p == 'V':
                g=g+'30m6'
            elif p == 'W':
                g=g+'03n8'
            elif p == 'X':
                g=g+'1p05'
            elif p == 'Y':
                g=g+'0s97'
            elif p =='Z':
                g=g+'7o77'
            elif p ==' ':
                g=g+'00~00'
            elif p == '0':
                g=g+'9+87'
            elif p == '1':
                g=g+'5=73'
            elif p == '2':
                g=g+'541-'
            elif p == '3':
                g=g+')475'
            elif p == '4':
                g=g+'10(0'
            elif p == '5':
                g=g+'797*'
            elif p == '6':
                g=g+'51&4'
            elif p == '7':
                g=g+'3^21'
            elif p== '8':
                g=g+'24}1'
            elif p=='9':
                g=g+'911{'
            elif p =='<':
                g=g+'8<09'
            elif p =='>':
                g=g+'4.76'
            elif p =='?':
                g=g+'7@34'
            elif p ==';':
                g=g+'0:98'
            elif p =='.':
                g=g+'43>9'
            elif p == '!':
                g=g+'98#0'
            elif p == '@':
                g=g+'5!87'
            elif p == '$':
                g=g+'0%87'
            else:
                g=g+''
            
        q.append(g)
  
        g=''
    qq=','.join(q)
    re=messagebox.askquestion("Result","Following is your Encypted Code: \n"+qq+"\n\nDo You Want to Copy this?")
    if re=="yes":
        root.clipboard_clear()
        root.clipboard_append(qq)
        e.delete("1.0","end")
        pass
    else:
        e.delete("1.0","end")
        pass
 
   

def b2f():
    result = messagebox.askquestion("Warning", "Are You Sure to want to Exit.", icon='warning')
    if result == 'yes':
        sys.exit()
    else:
        e.focus()
        pass
def b11f():
    b1.place( x = 355 , y = 470 )
    b3.place_forget()
    b3.update()
    l1.place( x = 47 , y = 165 )
    l2.place_forget()
    l2.update()
    
def b12f():
    b3.place( x = 355 , y = 470 )
    b1.place_forget()
    b1.update()
    l2.place( x = 47 , y = 165 )
    l1.place_forget()
    l1.update()
    

root = Tk()
root.title("JigViroCryptor7 (JVC7)")
root.resizable(0,0)
root.geometry('550x535')
root.iconbitmap("jvc7.ico")
photo = PhotoImage(file="example.png")
photo_label = Label(root,image=photo)
photo_label.pack(side=TOP)             
w = 550 # width for my screen
h = 535 # height for my screen
# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
global var
global a
var=IntVar()
b11=Radiobutton(root , text = 'Encrypt',font = ("times new roman",15,'bold',"italic"),value=0,variable=var,command=b11f)
b12=Radiobutton(root , text = 'Decrypt',font = ("times new roman",15,'bold',"italic"),value=1,variable=var,command=b12f)
b11.place(x= 40 , y=125)
b12.place(x= 415 , y=125)
l1=Label(root, text = "Enter Your Message Here : " , font = ("times new roman",12,"bold","italic"))
l2=Label(root, text = "Enter Your Encrypted Message Here : " ,font = ("times new roman",12,"bold","italic")    )
l1.place( x = 47 , y = 165 )
e=ScrolledText(root , width  = 55 , height = 16,bd='5')
e.place( x = 49 , y = 195 )
e.focus()

b1= Button(root , padx = 40 , pady = 4 , text = 'ENCRYPT', fg  = 'white' ,bd="4",bg='black' ,font = ("times new roman",10,'bold',"italic"),command=b1f  )
b2 = Button(root , padx = 55 , pady = 4 , text = 'EXIT',  bd="4", fg = 'white' , bg  = 'red'  ,font = ("times new roman",10,'bold',"italic") ,command=b2f )
b3= Button(root , padx = 40 , pady = 4 , text = 'DECRYPT', fg  = 'white' ,bd="4",bg='black' ,font = ("times new roman",10,'bold',"italic"),command=b3f  )
b1.place( x = 355 , y = 470 )
b2.place( x = 49 , y = 470 )



root.mainloop()
