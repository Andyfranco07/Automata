import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageTk

lengu=["-","0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","Ñ","O","P","Q","R","S","T","U","V","W","X","Y","Z",]

class inicio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ventana Principal")
        self.geometry("1084x700")
        self._frame = None
        self.crear_interfaz()

    def crear_interfaz(self):

        self.label = tk.Label(self, text="Pon una cadena de serie", font=('Arial', 16))
        self.label.place(x=410, y=230)

        self.entry_variable = tk.Entry(self, font=('Arial', 16))
        self.entry_variable.place(x=410, y=270)

        estilo_boton = {
            'font': ('Arial', 20, 'bold'), 
            'fg': '#272878',
            'bg': 'white',
            'width': 11,
            'height': 0,
            'relief': 'raised',
            'borderwidth': 2,
        }

    
        self.label_resultado = tk.Label(self, text="")
        self.label_resultado.place(x=470, y=300)

        self.button_login = tk.Button(self, text="Iniciar", command=self.iniciar, **estilo_boton)
        self.button_login.place(x=430, y=350)

        self.label = tk.Label(self, text="Recorrido:", font=('Arial', 16))
        self.label.place(x=460, y=430)

        self.label_recorrido = tk.Label(self, text="")
        self.label_recorrido.place(x=400, y=470)


    def iniciar(self):
        cadena = self.entry_variable.get()
        cad = list(cadena)
        if(len(cad)== 9):
            self.q_0(cad)
        else:
            self.label_resultado.config(text="Tamaño de cadena no valida")
            self.label_recorrido.config(text="")

    def q_0(self, cad):
        print("------------")
        print("q0")
        self.label_recorrido.config(text="Q0")
        global tipo_cad
        if(cad[0]==lengu[15]):
            self.q_1(cad)
        elif(cad[0]==lengu[16]):
            #self.label_resultado.config(text="valido")
            self.q_2(cad)
        else:
            self.label_resultado.config(text="cadena no valido")

    def q_1(self,cad):
        print("q1")
        texto_actual = self.label_recorrido.cget("text")
        nuevo_texto = "->Q1"
        nuevo_texto_acumulado = f"{texto_actual} {nuevo_texto}"
        self.label_recorrido.config(text=nuevo_texto_acumulado)
        for i in range(18, len(lengu)):
            if cad[1]==lengu[i]:
                self.q_3(cad)
                break
            else: 
                self.label_resultado.config(text="cadena no valido")
    
    def q_2(self,cad):
        print("q2")
        texto_actual = self.label_recorrido.cget("text")
        nuevo_texto = "->Q2"
        nuevo_texto_acumulado = f"{texto_actual} {nuevo_texto}"
        self.label_recorrido.config(text=nuevo_texto_acumulado)
        if cad[1]==lengu[11] or cad[1]==lengu[12]:
            self.q_3(cad)
        else: 
            self.label_resultado.config(text="cadena no valido")

    def q_3(self,cad):
        print("q3")
        texto_actual = self.label_recorrido.cget("text")
        nuevo_texto = "->Q3"
        nuevo_texto_acumulado = f"{texto_actual} {nuevo_texto}"
        self.label_recorrido.config(text=nuevo_texto_acumulado)
        if cad[2]==lengu[0]:
            self.q_4(cad)
            #self.label_resultado.config(text="valido")

    def q_4(self,cad):
        print("q4")
        texto_actual = self.label_recorrido.cget("text")
        nuevo_texto = "->Q4"
        nuevo_texto_acumulado = f"{texto_actual} {nuevo_texto}"
        self.label_recorrido.config(text=nuevo_texto_acumulado)
        if cad[3]==lengu[1]:
            self.q_5(cad)
        else:
            for i in range(2, 11):
                if cad[3]==lengu[i]:
                    self.q_11(cad)
                    break
                else: 
                    self.label_resultado.config(text="cadena no valido")

    def q_5(self,cad):
        print("q5")
        texto_actual = self.label_recorrido.cget("text")
        nuevo_texto = "->Q5"
        nuevo_texto_acumulado = f"{texto_actual} {nuevo_texto}"
        self.label_recorrido.config(text=nuevo_texto_acumulado)
        
        if cad[4]==lengu[1]:
            self.q_6(cad)
        else:
            for i in range(2, 11):
                if cad[4]==lengu[i]:
                    self.q_12(cad)
                    break
                else: 
                    self.label_resultado.config(text="cadena no valido")

    def q_6(self,cad):
        print("q6")
        texto_actual = self.label_recorrido.cget("text")
        nuevo_texto = "->Q6"
        nuevo_texto_acumulado = f"{texto_actual} {nuevo_texto}"
        self.label_recorrido.config(text=nuevo_texto_acumulado)
        
        if cad[5]==lengu[1]:
            self.q_7(cad)
            
            #self.label_resultado.config(text="valido")
        else:
            for i in range(2, 11):
                if cad[5]==lengu[i]:
                    self.q_13(cad)
                    #self.label_resultado.config(text="valido")
                    break
                else: 
                    self.label_resultado.config(text="cadena no valido")
    
    def q_7(self,cad):
        print("q7")
        texto_actual = self.label_recorrido.cget("text")
        nuevo_texto = "->Q7"
        nuevo_texto_acumulado = f"{texto_actual} {nuevo_texto}"
        self.label_recorrido.config(text=nuevo_texto_acumulado)
        for i in range(2, 11):
            if cad[6]==lengu[i]:
                self.q_8(cad)
                break
            else: 
                self.label_resultado.config(text="cadena no valido")
    
    def q_8(self,cad):
        print("q8")
        texto_actual = self.label_recorrido.cget("text")
        nuevo_texto = "->Q8"
        nuevo_texto_acumulado = f"{texto_actual} {nuevo_texto}"
        self.label_recorrido.config(text=nuevo_texto_acumulado)
        if cad[7]==lengu[0]:
            self.q_9(cad)
    
    def q_9(self,cad):
        print("q9")
        texto_actual = self.label_recorrido.cget("text")
        nuevo_texto = "->Q9"
        nuevo_texto_acumulado = f"{texto_actual} {nuevo_texto}"
        self.label_recorrido.config(text=nuevo_texto_acumulado)
        for i in range(11, len(lengu)):
            if cad[8]==lengu[i]:
                self.q_10(cad)
                break
            else: 
                self.label_resultado.config(text="cadena no valido")
    
    def q_10(self,cad):
        print("q10")
        texto_actual = self.label_recorrido.cget("text")
        nuevo_texto = "->Q10"
        nuevo_texto_acumulado = f"{texto_actual} {nuevo_texto}"
        self.label_recorrido.config(text=nuevo_texto_acumulado)
        self.label_resultado.config(text="Cadena Valida")

    def q_11(self,cad):
        print("q11")
        texto_actual = self.label_recorrido.cget("text")
        nuevo_texto = "->Q11"
        nuevo_texto_acumulado = f"{texto_actual} {nuevo_texto}"
        self.label_recorrido.config(text=nuevo_texto_acumulado)
        for i in range(1, 11):
            if cad[4]==lengu[i]:
                self.q_12(cad)
                break
            else: 
                self.label_resultado.config(text="cadena no valido")

    def q_12(self,cad):
        print("q12")
        texto_actual = self.label_recorrido.cget("text")
        nuevo_texto = "->Q12"
        nuevo_texto_acumulado = f"{texto_actual} {nuevo_texto}"
        self.label_recorrido.config(text=nuevo_texto_acumulado)
        for i in range(1, 11):
            if cad[5]==lengu[i]:
                self.q_13(cad)
                break
            else: 
                self.label_resultado.config(text="cadena no valido")

    def q_13(self,cad):
        print("q13")
        texto_actual = self.label_recorrido.cget("text")
        nuevo_texto = "->Q13"
        nuevo_texto_acumulado = f"{texto_actual} {nuevo_texto}"
        self.label_recorrido.config(text=nuevo_texto_acumulado)
        for i in range(1, 11):
            if cad[6]==lengu[i]:
                self.q_8(cad)
                break
            else: 
                self.label_resultado.config(text="cadena no valido")
               
if __name__ == "__main__":
    app = inicio()
    app.mainloop()