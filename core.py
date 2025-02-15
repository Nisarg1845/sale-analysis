from tkinter import Tk, Canvas, Button
from LoginPage import loginPage
from SignInPage import signinPage
from main_menu import mainScreen
from register_update import registerProduct
from resetPass import resetPassword
from mostSold import mostSoldGraph
from datebyrange import dateRange

def main():
    # Initialize the main Tkinter window
    window = Tk()
    window.geometry("1440x788")
    window.title("ShopLens")
    window.configure(bg="#0F3ADA")

    # Create a shared canvas to manage both pages
    canvas = Canvas(
        window,
        bg="#A5D1E1",
        height=788,
        width=1440,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.pack()

    # Function to switch to the login page
    def show_login():
        canvas.delete("all")  # Clear the canvas for the new page
        loginPage(canvas, show_signin, show_mainmenu,show_forget)

    # Function to switch to the sign-in page
    def show_signin():
        canvas.delete("all")  # Clear the canvas for the new page
        signinPage(canvas, show_login)

    def show_mainmenu(shopname):
        canvas.delete("all")
        mainScreen(canvas,show_register,shopname,show_mostSold,show_dateRange)

    def show_register(shopname):
        canvas.delete("all")
        registerProduct(canvas,shopname,show_mainmenu)

    def show_forget(email):
        canvas.delete("all")
        resetPassword(canvas,email,show_login)

    def show_mostSold(shopname):
        canvas.delete("all")
        mostSoldGraph(canvas,shopname,show_mainmenu)

    def show_dateRange(shopname):
        canvas.delete("all")
        dateRange(canvas,shopname,show_mainmenu)




    # Initially, show the login page
    show_login()


    # Run the Tkinter main loop
    window.resizable(False,False)
    window.mainloop()


if __name__ == "__main__":
    main()
