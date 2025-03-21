from signup import SignUp
from signin import SignIn




def check_signup_result(signup):
    if signup.result is not None:
        if signup.result:
            pass
            # here we should open a new page
        else:
            print('not ok')
    else:
        signup.after(100, check_signup_result, signup)





# def check_signin_result(signin, counter=0):
#     if signin.result is not None:
#         if signin.result:
#             print('Login successful!')
#         else:
#             print('Login failed.')
#     else:
#         if counter < 100:
#             signin.after(100, check_signin_result, signin, counter + 1)
#         else:
#             print("Timeout: No result found.")
#
#
# if __name__ == "__main__":
#     signin = SignIn()
#     signin.after(100, check_signin_result, signin )
#     signin.mainloop()