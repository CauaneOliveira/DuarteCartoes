import customtkinter as ctk

from style import Style

class telaHome():
    def __init__(self, root):
        self.root = root

        self.texBtn={0:'Negociação', 1:'Produção', 2:'Pendências', 3:'Expedição'}
        
        self.root.columnconfigure(0, weight=1)  # Espaço lateral
        self.root.columnconfigure(1, weight=4)  # Espaço central
        self.root.columnconfigure(2, weight=1)  # Espaço lateral

        central_frame = ctk.CTkFrame(self.root, fg_color=Style.color('bg'))
        central_frame.grid(row=0, column=1, pady=40, sticky="ew")
        central_frame.columnconfigure(tuple(range(len(self.texBtn))), weight=1)
        
        for i in range(0,4):
            card = f"card{i}"
            card = ctk.CTkScrollableFrame(central_frame, fg_color=Style.color('bg_frame'),width=345,height=560)
            card.grid(row=0, column=i)
            self.el_frame(i,card)

    def el_frame(self,n,card):

        btn_ifo = ctk.CTkButton(card,text=self.texBtn[n],font=("Arial", 18, "bold"),width=346, height=30,text_color="white",fg_color=Style.color('fg_2'),hover_color=Style.color('hover_2'),corner_radius=5)
        btn_ifo.grid(row=0, column=0)

        info = []
        r=1
            
        if n==0:

            info = [{'id':'1'},{'id':'2'},{'id':'1'},{'id':'2'},{'id':'1'},{'id':'2'}]
            
        for i in info:    
            ifo_frame = ctk.CTkFrame(card, corner_radius=10,fg_color=Style.color('bg'))
            ifo_frame.grid(row=r, column=0, pady=10,padx=10, sticky="ew")
            ifo_frame.grid_propagate(0)
            
            ped_label = ctk.CTkLabel(ifo_frame, text=f"ID:{i['id']}",text_color='black',font=("Lucida Grande", 16))
            ped_label.pack(pady=5)
            r+=1
            
        if not info:
            ifo_frame = ctk.CTkFrame(card, corner_radius=10,fg_color=Style.color('bg'))
            ifo_frame.grid(row=1, column=0, pady=10,padx=10, sticky="ew")
            ifo_frame.grid_propagate(0)

            msg_label = ctk.CTkLabel(ifo_frame, text="Nenhum resultado encontrado.",text_color='black',font=("Lucida Grande", 16))
            msg_label.pack(pady=5)