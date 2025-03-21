import customtkinter as ck
from db import Db
from tkinter import messagebox

# create signup class
class SignUp(ck.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x550")
        self.resizable(False,False)
        self.title("TODO APP | sign up")
        title_font = ck.CTkFont(size=30,weight='bold')
        self.main_title = ck.CTkLabel(self, text='Sign up', pady= 35 , font=title_font )
        self.main_title.pack()

        self.username = ck.CTkEntry(self, 250,50, 20,0,placeholder_text='type username ....')
        self.username.pack(pady=25)

        self.password = ck.CTkEntry(self, 250, 50, 20, 0, placeholder_text='type password ....')
        self.password.pack(pady=25)

        self.submit_btn = ck.CTkButton(self, 120, 40,40, text='Sign Up', command=self.btn_callback)
        self.submit_btn.pack(pady=15)




    def btn_callback(self):
        self._db = Db('database.db')

        username = self.username.get()
        password = self.password.get()

        if  40 > len(username) > 5 and   40> len(password) > 6:
            try :
                self._db.insert_into_db(username, password)
                return True
            except ValueError:
                messagebox.showerror("Error",
                                     "Username Already Exists")
                return False

        else:
            messagebox.showerror("Error",
                                 "Username must be longer than 5 characters and password must be longer than 6 characters.")
            return False


app = SignUp()
app.mainloop()