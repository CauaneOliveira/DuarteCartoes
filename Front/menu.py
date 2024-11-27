import customtkinter as ctk

from telas.tela_home import telaHome
from style import Style

class Menu:
    def __init__(self,root,instance):
        self.root = root
        self.instance = instance
        
        frame = ctk.CTkFrame(root)
        frame.grid(row=0)

        btn_logo = ctk.CTkButton(frame,text="logo",width=0)
        btn_logo.grid(row=0,column=0)

        buttons = [
            ("Home"),
            ("Produção"),
            ("Cliente"),
            ("Pedido"),
            ("Relatorio")]
        
        self.menu_buttons = []
        for text in buttons:
            button = ctk.CTkButton(frame, text=text, font=('Arial', 15, 'bold'), corner_radius=3, width=200, height=40)
            button.grid(row=0,column=0)
            self.menu_buttons.append(button)
        

