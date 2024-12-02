import customtkinter as ctk

from style import Style

class telaPedido:
    def __init__(self,root):
        self.root = root

        self.root.columnconfigure(0, weight=1)  # Espaço lateral
        self.root.columnconfigure(1, weight=1)  # Espaço central
        self.root.columnconfigure(2, weight=1)  # Espaço lateral

        central_frame = ctk.CTkFrame(self.root, fg_color=Style.color('bg'))
        central_frame.grid(row=0, column=1, pady=20, sticky="ew")

        btn_graf = ctk.CTkButton(central_frame,text="Grafica",image=Style.img('img_icon_grafica'),font=("Arial", 18, "bold"),width=200, height=150,text_color="black",fg_color=Style.color('hover_2'),hover_color=Style.color('fg_2'),border_width=3, border_color=Style.color('fg_2'),corner_radius=5)
        btn_graf.grid(row=0,column=0,padx=20)

        btn_ped = ctk.CTkButton(central_frame,text="Pendências",image=Style.img('img_icon_pendencias'),font=("Arial", 18, "bold"),width=200, height=150,text_color="black",fg_color=Style.color('hover_2'),hover_color=Style.color('fg_2'),border_width=3, border_color=Style.color('fg_2'),corner_radius=5)
        btn_ped.grid(row=0,column=1,padx=20)

        btn_prod = ctk.CTkButton(central_frame,text="Produto",image=Style.img('img_icon_produto'),font=("Arial", 18, "bold"),width=200, height=150,text_color="black",fg_color=Style.color('hover_2'),hover_color=Style.color('fg_2'),border_width=3, border_color=Style.color('fg_2'),corner_radius=5)
        btn_prod.grid(row=0,column=2,padx=20)