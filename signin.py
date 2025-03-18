import customtkinter as ck

# create signin class
class Signin(ck.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x550")
        self.resizable(False,False)
        self.title("TODO APP | sign in ")
        title_font = ck.CTkFont(size=30,weight='bold')
        self.main_title = ck.CTkLabel(self, text='Sign in', pady= 35 , font=title_font )
        self.main_title.pack()

        self.username = ck.CTkEntry(self, 250,50, 20,0,placeholder_text='type username ....')
        self.username.pack(pady=25)

        self.password = ck.CTkEntry(self, 250, 50, 20, 0, placeholder_text='type password ....')
        self.password.pack(pady=25)

        self.submit_btn = ck.CTkButton(self, 120, 40,40, text='Sign in', command=self.btn_callback)
        self.submit_btn.pack(pady=15)


    def btn_callback(self):

        username = self.username.get()
        password = self.password.get()

        if len(username) < 5:
            pass

        elif len(password) < 6:
            pass

        else:
            pass



