import customtkinter as ctk

from style import Style
from menu import Menu

class Main:
    def __init__(self,root):
        Menu(root)
        
if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Duarte Cartões")
    ctk.set_appearance_mode("light")

    largura_janela = 1600
    altura_janela = 700

    Style.centralizar_janela(root, largura_janela, altura_janela)
    
    Main(root)
    root.mainloop()