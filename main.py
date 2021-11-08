from tkinter import *
from tkinter import messagebox

option1=['english','finglish']
WORDS =[]

class Translator:
      def __init__(self , master , *args , **kwargs):
          self.master = master
          self.master = master
          self.heading = Label(master,text="Translator ", font="arial 30 bold", fg="black")
          self.heading.place(x=310,y=20)

  
          self.button_0 =  Button(master,width=25,height=2,text="search" ,font="arial 12 ", fg="white",bg="green",command=self.change1)
          self.button_0.place(x=170,y=150)
          
          self.button_1 =  Button(master,width=25,height=2,text="create" ,font="arial 12 ", fg="white",bg="blue",command=self.change2)
          self.button_1.place(x=470,y=150)


      def change1(self):
          
            self.first_lang = StringVar()
            self.first_lang.set(option1[0])
          
            self.second_lang = StringVar()
            self.second_lang.set(option1[1])
          
            self.first_drop = OptionMenu(self.master,self.first_lang,*option1)
            self.first_drop.place(x=200,y=150)
          
            self.second = OptionMenu(self.master,self.second_lang,*option1)
            self.second.place(x=480,y=150)
          
            self.text_1 = Text(self.master, height=12, width=30)
            self.text_1.place(x=130,y=200)
        
          
            self.text_2 = Text(self.master, height=12, width=30)
            self.text_2.place(x=430,y=200)
            self.text_2.config(state=DISABLED)
          
            self.button =  Button(self.master,width=25,height=2,text="Sumbit" ,font="arial 12 ", fg="white",bg="green",command=self.search)
            self.button.place(x=270,y=450)

            self.button_0.place(x=11170,y=50)
            self.button_1.place_forget()

            self.back_button =  Button(self.master,width=15,height=2,text="back" ,font="arial 12 ", fg="white",bg="orange",command=self.back_menu2)
            self.back_button.place(x=70,y=20)

            
      def change2(self):
            self.first_lang = StringVar()
            self.first_lang.set(option1[0])
          
            self.second_lang = StringVar()
            self.second_lang.set(option1[1])
          
            self.heading_1 = Label(self.master,text="enter the lettter ", font="arial 15 bold", fg="black")
            self.heading_1.place(x=130,y=150)

            self.text_3 = Text(self.master, height=5, width=30)
            self.text_3.place(x=130,y=200)

            self.heading_2 = Label(self.master,text="enter the meanig ", font="arial 15 bold", fg="black")
            self.heading_2.place(x=430,y=150)
          
            self.text_4 = Text(self.master, height=5, width=30)
            self.text_4.place(x=430,y=200)
          
            self.button_s =  Button(self.master,width=25,height=2,text="Sumbit" ,font="arial 12 ", fg="white",bg="green",command=self.add_words)
            self.button_s.place(x=270,y=450)

            self.button_0.place_forget()
            self.button_1.place(x=11170,y=50)

            self.back_button =  Button(self.master,width=15,height=2,text="back" ,font="arial 12 ", fg="white",bg="orange",command=self.back_menu)
            self.back_button.place(x=70,y=20)

      def back_menu(self):
          if( self.text_4):
             self.text_4.destroy()
             self.text_3.destroy()
             self.heading_1.configure(text="")
             self.heading_2.configure(text="")
             self.button_s.destroy()
        
           
      

          self.button_0 =  Button(self.master,width=25,height=2,text="search" ,font="arial 12 ", fg="white",bg="green",command=self.change1)
          self.button_0.place(x=170,y=150)
          
          self.button_1 =  Button(self.master,width=25,height=2,text="create" ,font="arial 12 ", fg="white",bg="blue",command=self.change2)
          self.button_1.place(x=470,y=150)
          self.back_button.place(x=2270,y=20)


      def back_menu2(self):
           self.text_2.destroy()
           self.text_1.destroy()
           self.first_drop.destroy()
           self.second.destroy()
           self.button.destroy()
           self.button_0 =  Button(self.master,width=25,height=2,text="search" ,font="arial 12 ", fg="white",bg="green",command=self.change1)
           self.button_0.place(x=170,y=150)
          
           self.button_1 =  Button(self.master,width=25,height=2,text="create" ,font="arial 12 ", fg="white",bg="blue",command=self.change2)
           self.button_1.place(x=470,y=150)

           self.back_button.place(x=2270,y=20)


          
      def search(self):

          out_put = ''
          self.text_2.config(state='normal')
          self.tt = self.text_1.get("1.0",END)

          self.options_1=self.first_lang.get()
          self.options_2=self.second_lang.get()
         
          with open('words_bank.txt','r') as f:
              all_text = f.read()
             
              lines = all_text.split('\n')
              for i in range(0,len(lines),2):
                  my_dict = {'english': lines[i], 'finglish':lines[i+1]}
                 
                  WORDS.append(my_dict)


          if self.options_1 == 'english' and  self.options_2 == 'finglish':
             for texts in self.tt.split('\n')[0].split(' '):
                  for word in WORDS:
                      if texts == word['english']:
                          out_put += word['finglish'] + " "
                          break
                  else:
                     out_put += texts + " "

          elif self.options_1 == 'finglish' and  self.options_2 == 'english': 
               for texts in self.tt.split('\n')[0].split(' '):
                  for word in WORDS:
                      if texts == word['finglish']:
                          out_put += word['english'] + " "
                          break
                  else:
                     out_put += texts + " "   
          else:
                out_put += self.tt.split('\n')[0].split(' ')
       
          self.text_2.insert(INSERT, out_put)
          self.text_2.config(state=DISABLED)


      def add_words(self):
           self.word_main = self.text_3.get("1.0",END)
           self.word_translate = self.text_4.get("1.0",END)
           print(self.word_translate)
           with open('words_bank.txt','r') as f:
              all_text = f.read()
              lines = all_text.split('\n')
              print(lines)
              for i in range(0,len(lines),2):
                  my_dict = {'english': lines[i], 'finglish':lines[i+1]}
                  WORDS.append(my_dict)
           with open('words_bank.txt','w') as f:
                for texts in self.word_main.split('\n')[0].split(' '):
                  for word in WORDS:
                      if texts == word['english']:
                          f.write(all_text)
                          self.text_3.delete('1.0', END)
                          self.text_4.delete('1.0', END)
                          messagebox.showerror("error","this word is exist ! ")
                          break
                  else:
                      f.write(all_text)
                      f.write("\n"+self.word_main.split('\n')[0] + "\n" + self.word_translate.split('\n')[0] )
                      self.text_3.delete('1.0', END)
                      self.text_4.delete('1.0', END)
                      messagebox.showinfo("updated","new word added !")
               
            

root = Tk()
b = Translator(root)
root.geometry("900x900+30+30") 
root.title(" translator ")

root.mainloop()