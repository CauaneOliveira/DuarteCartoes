import customtkinter as ctk

from style import Style

class telaCliente:
    def __init__(self,root,instance):

        self.root = root
        self.instance = instance

        frame = ctk.CTkFrame(self.root,width=100)
        frame.grid(row=0,column=0,sticky = 'ew')
        frame.columnconfigure(0,weight=1)
        frame.columnconfigure(1,weight=1)


        msg_label = ctk.CTkEntry(frame, placeholder_text="Pesquisar",width=600,height=40)
        msg_label.grid(row=0,column=0, sticky = 'w',pady=20, padx=20)

        btn_Pedido = ctk.CTkButton(frame,text="Novo Pedido",font=("Arial", 18, "bold"),width=150, height=40,text_color="white",fg_color=Style.color('fg'),hover_color=Style.color('hover'),corner_radius=10)
        btn_Pedido.grid(row=0,column=1, sticky = 'e',pady=20)
