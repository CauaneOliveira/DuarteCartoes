import customtkinter as ctk

from menu import Menu
from telas.tela_home import telaHome

class Main:
    def __init__(self,root):
        self.menu = Menu(root,self)
        if self.menu:
            telaHome(root)
        
if __name__ == "__main__":
    jan = ctk.CTk()
    
    largura_janela = 1300
    altura_janela = 640

    jan.geometry(f"{largura_janela}x{altura_janela}")


    Main(jan)

    jan.mainloop()