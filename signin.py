import customtkinter as ck
from db import Db
from tkinter import messagebox

class SignIn(ck.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x550")
        self.resizable(False, False)
        self.title("TODO APP | Sign In")
        self.result = None  # تعریف ویژگی result
        title_font = ck.CTkFont(size=30, weight='bold')
        self.main_title = ck.CTkLabel(self, text='Sign In', pady=35, font=title_font)
        self.main_title.pack()

        self.username = ck.CTkEntry(self, width=250, height=50, corner_radius=20, placeholder_text='Type username...')
        self.username.pack(pady=25)

        self.password = ck.CTkEntry(self, width=250, height=50, corner_radius=20, placeholder_text='Type password...', show='*')
        self.password.pack(pady=25)

        self.submit_btn = ck.CTkButton(self, width=120, height=40, corner_radius=40, text='Sign In', command=self.btn_callback)
        self.submit_btn.pack(pady=15)

        parent_bg_color = self.cget('bg')
        self.change_action = ck.CTkButton(
            self,
            width=80,
            height=40,
            corner_radius=50,
            text='Sign Up',
            bg_color='transparent',
            fg_color=parent_bg_color,
            hover_color=parent_bg_color,
            text_color='#ADD8E6',
            font=('Arial', 15, 'underline'),
            command=self.change_act,
        )
        self.change_action.pack(pady=30)

    def change_act(self):
        self.destroy()
        from signup import SignUp
        app = SignUp()
        app.mainloop()

    def btn_callback(self):
        self._db = Db('database.db')

        username = self.username.get()
        password = self.password.get()

        if 40 > len(username) > 5 and 40 > len(password) > 6:
            value = self._db.select_user(username)
            if value and value[1] == password:
                messagebox.showinfo("Success", "Login successful!")
                self.result = True
            else:
                messagebox.showerror("Error", "Username or password is incorrect.")
                self.result = False
        else:
            messagebox.showerror("Error", "Username must be longer than 5 characters and password must be longer than 6 characters.")
            self.result = False