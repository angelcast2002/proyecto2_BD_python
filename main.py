from tkinter import *
from tkinter import messagebox
from expediente import ExpedienteWindow
import connection as con


def main():
    results = con.connect(r"""select * from prueba;""")
    print(results)
    principalWindow()
   
   

def principalWindow():
    win = Tk()
    win.title("Login")
    
    etiUsername = Label(win, text="Username")
    inputUsername = Entry(win)
    
    etiPassword = Label(win, text="Password")
    inputPassword = Entry(win)
    
    buttonLogin = Button(win, text="Login", command= lambda: login(inputPassword, inputUsername, win))
    
    etiUsername.pack()
    inputUsername.pack()
    etiPassword.pack()
    inputPassword.pack()
    buttonLogin.pack()

    win.geometry("300x200")
    win.mainloop()
    
# Login function
def login(inputUsername, inputPassword, win):
    usuario = inputUsername.get()
    contrasena = inputPassword.get()
    query = f"SELECT COUNT(*) FROM usuarios WHERE usuario='{usuario}' AND contrasena='{contrasena}'" # Query
    results = con.connect(query)
    
    # None type data verification
    if results is not None and results[0][0] == 1:
        ExpedienteWindow(win, administrador=True)
        
    # Error message if credentials do not match
    else:
        messagebox.showerror("Error de inicio de sesión", "Usuario o contraseña incorrectos")

if __name__ == '__main__':
    main()