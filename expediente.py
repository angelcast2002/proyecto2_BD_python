from tkinter import *
import connection as con
from resultadosExpediente import ResultadoExpediente
from signup import SignupWindow

class ExpedienteWindow:
    def __init__(self, parent, administrador):
        self.parent = parent
        self.win = Toplevel(parent)
        self.win.title("Expediente")
        
        etiNombrePaciente = Label(self.win, text="Nombre del paciente")
        etiCodigopaciente = Label(self.win, text="Codigo del paciente")
        
        inputNombrePaciente = Entry(self.win)
        inputCodigoPaciente = Entry(self.win)
        
        buttonBuscar = Button(self.win, text="Buscar", command= lambda: self.buscarPaciente(inputIdPaciente))
        buttonCrearUsuario = Button(self.win, text="Crear usuario", command= lambda: self.crearUsuario())
        buttonEditarUsuario = Button(self.win, text="Editar usuario", command= lambda: self.close())
        
        etiNombrePaciente.pack()
        inputNombrePaciente.pack()
        etiCodigopaciente.pack()
        inputCodigoPaciente.pack()
        buttonBuscar.pack()
        if (administrador == True):
            buttonCrearUsuario.pack()
            buttonEditarUsuario.pack()
        
        self.win.geometry("300x200")
        
    def buscarPaciente(self, inputIdPaciente):
        query = f"SELECT * FROM paciente p WHERE p.dpi = '{inputIdPaciente.get()}'"
        results = con.connect(query)
        column_names = con.column_names(query)
        ResultadoExpediente(self.win, results, column_names)
        
    def crearUsuario(self):
        SignupWindow(self.win)
    
        
        etiNombreResultado.pack()
        etiCodigoResultado.pack()
        