import customtkinter as ctk

from style import Style

class telaCliente:
    def __init__(self,root,instance):

        self.root = root
        self.instance = instance

        msg_label = ctk.CTkEntry(self.root, placeholder_text="Pesquisar",width=600,height=40)
        msg_label.grid(row=0,column=0,pady=20, padx=30)

        #btn_Pedido = ctk.CTkButton(self.root,text="Novo Pedido",font=("Arial", 18, "bold"),width=150, height=40,text_color="white",fg_color=Style.color('fg'),hover_color=Style.color('hover'),corner_radius=10)
        #btn_Pedido.grid(row=0,column=1,pady=20)

        self.card = ctk.CTkScrollableFrame(self.root, fg_color=Style.color('bg_frame'),width=1510,height=510)
        self.card.grid(row=1,padx=30)

        self.contudo()
    def contudo(self):
        info = [{'status':0,'id':'1','data':'16/12/24','nome':'Carlos','produto':'Tags'},
                    {'status':0,'id':'2','data':'23/12/24','nome':'Maria','produto':'Cartao'},
                    {'status':0,'id':'3','data':'10/12/24','nome':'Julia','produto':'Convite'}]
        
        r=1
        for i in info:
            ifo_frame = ctk.CTkFrame(self.card, corner_radius=10, fg_color=Style.color('bg'))
            ifo_frame.grid(row=r, column=0, pady=10,padx=10, sticky="nsew")
            ifo_frame.grid_propagate(0)
            
            ped_label = ctk.CTkLabel(ifo_frame, text=f"{i['data']} - {i['nome']} | {i['produto']}",text_color='black',font=("Lucida Grande", 16))
            ped_label.pack(pady=5)

            r+=1
        