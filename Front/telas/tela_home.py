import customtkinter as ctk

from style import Style


class telaHome():
    def __init__(self, root):
        self.root = root

        btn_logo = ctk.CTkButton(self.root,text="DUARTE\nCARTÕES",font=("Arial", 15, "bold"),text_color=Style.color('fg'),fg_color=Style.color('bg_top'), hover=False,corner_radius=10,width=120)
        btn_logo.grid(row=0, column=0, padx=10, pady=10, sticky="w")
