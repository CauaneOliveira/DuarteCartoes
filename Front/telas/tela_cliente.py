import customtkinter as ctk

from style import Style

class telaCliente():
    def __init__(self, root, instance):
        self.root = root
        self.instance = instance

        self.info = []
        
        self.root.columnconfigure(0, weight=1)  # Espaço lateral
        self.root.columnconfigure(1, weight=1)  # Espaço central
        self.root.columnconfigure(2, weight=1)  # Espaço lateral

        msg_label = ctk.CTkEntry(self.root, placeholder_text="Pesquisar",width=600,height=40, corner_radius=10)
        msg_label.grid(row=0,column=0, sticky="w",pady=20,padx=40)

        btn_Pedido = ctk.CTkButton(self.root,text="Novo Pedido",font=("Arial", 18, "bold"),width=150, height=40,text_color="white",fg_color=Style.color('fg'),hover_color=Style.color('hover'),corner_radius=10)
        btn_Pedido.grid(row=0,column=0, sticky="e",pady=20,padx=40)

        central_frame = ctk.CTkFrame(self.root, fg_color=Style.color('bg'))
        central_frame.grid(row=1, column=0, pady=10, sticky="ew")

        self.card1 = ctk.CTkScrollableFrame(central_frame, fg_color=Style.color('bg_frame'),width=1500,height=500)
        self.card1.grid(row=1, column=0,padx=40)
        self.el_frame(self.card1)

    def el_frame(self,card):

        r=1

        self.info = [{'status':0,'id':'1','data':'16/12/24','nome':'Carlos','produto':'Tags','empresa':'SkyTech'},
                {'status':0,'id':'2','data':'23/12/24','nome':'Maria','produto':'Cartao','empresa':'ProCard'},
                {'status':0,'id':'3','data':'10/12/24','nome':'Julia','produto':'Convite','empresa':'SisMas'}]

            
        for i in self.info:    
            
            ifo_frame = ctk.CTkFrame(card, corner_radius=10, fg_color=Style.color('bg'))
            ifo_frame.grid(row=r, column=0,padx=10, pady=10, sticky="ew")
            ifo_frame.grid_propagate(0)
            
            ped_label = ctk.CTkLabel(ifo_frame, text=f"{i['nome']} | {i['empresa']}",text_color='black',font=("Lucida Grande", 16))
            ped_label.pack(pady=5)

            r+=1
            
        if not self.info:
            ifo_frame = ctk.CTkFrame(card, corner_radius=10,fg_color=Style.color('bg'))
            ifo_frame.grid(row=1, column=0, pady=10,padx=10, sticky="ew")
            ifo_frame.grid_propagate(0)

            msg_label = ctk.CTkLabel(ifo_frame, text="Nenhum resultado encontrado.",text_color='black',font=("Lucida Grande", 16))
            msg_label.pack(pady=5)
    
