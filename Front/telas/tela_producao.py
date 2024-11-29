import customtkinter as ctk

from style import Style

class telaProducao():
    def __init__(self, root, instance):
        self.root = root
        self.instance = instance

        self.info = []
        self.texBtn={0:'Iniciar', 1:'A fazer', 2:'Pronto', 3:'Aprovado'}
        
        self.root.columnconfigure(0, weight=1)  # Espaço lateral
        self.root.columnconfigure(1, weight=4)  # Espaço central
        self.root.columnconfigure(2, weight=1)  # Espaço lateral

        central_frame = ctk.CTkFrame(self.root, fg_color=Style.color('bg'))
        central_frame.grid(row=0, column=1, pady=40, sticky="ew")
        central_frame.columnconfigure(tuple(range(len(self.texBtn))), weight=1)
        
        for i in range(0,4):
            self.card = f"card{i}"
            self.card = ctk.CTkScrollableFrame(central_frame, fg_color=Style.color('bg_frame'),width=345,height=560)
            self.card.grid(row=0, column=i)
            self.el_frame(i,self.card)

    def el_frame(self,n,card):

        lb_ifo = ctk.CTkLabel(card,text=self.texBtn[n],font=("Arial", 18, "bold"),width=346, height=30,text_color="white",fg_color=Style.color('fg_2'),corner_radius=5)
        lb_ifo.grid(row=0, column=0)

        r=1
            
        if n==0:

            self.info = [{'status':0,'id':'1','data':'16/12/24','nome':'Carlos','produto':'Tags'},
                    {'status':0,'id':'2','data':'23/12/24','nome':'Maria','produto':'Cartao'},
                    {'status':0,'id':'3','data':'10/12/24','nome':'Julia','produto':'Convite'}]
        elif n==1:
            self.info=[]
        elif n ==2:
            self.info=[]
        elif n ==3:
            self.info=[]
            
        for i in self.info:    
            ifo_frame = ctk.CTkFrame(card, corner_radius=10, fg_color=Style.color('bg'))
            ifo_frame.grid(row=r, column=0, pady=10,padx=10, sticky="ew")
            ifo_frame.grid_propagate(0)
            
            ped_label = ctk.CTkLabel(ifo_frame, text=f"{i['data']} - {i['nome']} | {i['produto']}",text_color='black',font=("Lucida Grande", 16))
            ped_label.pack(pady=5)

            btn_prox = ctk.CTkButton(ifo_frame,text=">",font=("Arial", 18, "bold"),width=40, height=38,text_color="white",fg_color=Style.color('fg'),hover_color=Style.color('hover'),corner_radius=5,command=lambda b=i: self.mudar_pedido(b))
            btn_prox.grid()

            r+=1
            
        if not self.info:
            ifo_frame = ctk.CTkFrame(card, corner_radius=10,fg_color=Style.color('bg'))
            ifo_frame.grid(row=1, column=0, pady=10,padx=10, sticky="ew")
            ifo_frame.grid_propagate(0)

            msg_label = ctk.CTkLabel(ifo_frame, text="Nenhum resultado encontrado.",text_color='black',font=("Lucida Grande", 16))
            msg_label.pack(pady=5)
    
    def mudar_pedido(self,n):
        print(n)
        if n['status'] == 0:
            #status = 1
            n['status'] = 1
        self.info.append(n)
        self.instance.chama_producao()
        print(n)