import customtkinter as ctk

from style import Style
from telas.tela_home import telaHome
from telas.tela_pedido import telaPedido
from telas.tela_producao import telaProducao
from telas.tela_cliente import telaCliente


class Menu:
    def __init__(self, root,):
        self.root = root
        self.frame_inferior = None

        self.root.columnconfigure(0, weight=1)  # horizontal fixo

        buttons = [
            ("Home", self.chamar_home),
            ("Produção", self.chama_producao),
            ("Cliente", self.chama_cliente),
            ("Pedido", self.chama_pedido),
            ("Relatório", self.chama_relatorio),
        ]
        
        frame = ctk.CTkFrame(root, fg_color=Style.color('bg_top'), height=100)
        frame.grid(row=0, column=0, sticky="ew")
        frame.columnconfigure(0, weight=1)  # Espaço para o logo
        frame.columnconfigure(1, weight=5)  # Espaço central para os botões
        frame.columnconfigure(2, weight=1)  # Espaço para o botão "Novo Pedido"

        btn_logo = ctk.CTkButton(frame,text="DUARTE\nCARTÕES",font=("Arial", 15, "bold"),text_color=Style.color('fg'),fg_color=Style.color('bg_top'), hover=False,width=120,command=lambda:self.mudanca_color(0))
        btn_logo.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        central_frame = ctk.CTkFrame(frame, fg_color=Style.color('bg_top'))
        central_frame.grid(row=0, column=1, pady=10, sticky="ew")
        central_frame.columnconfigure(tuple(range(len(buttons))), weight=1)

        self.menu_btn = []
        for i, (text, command) in enumerate(buttons):
            button = ctk.CTkButton(central_frame,text=text,font=("Arial", 18, "bold"),width=170, height=40,text_color="white",fg_color=Style.color('fg'),hover_color=Style.color('hover'), corner_radius=10,command=lambda b=i: self.mudanca_color(b))
            button.grid(row=0, column=i)
            self.menu_btn.append((button, command))

        btn_Pedido = ctk.CTkButton(frame,text="Novo Pedido",font=("Arial", 18, "bold"),width=150, height=40,text_color="white",fg_color=Style.color('fg'),hover_color=Style.color('hover'),corner_radius=10,command=self.novo_pedido)
        btn_Pedido.grid(row=0, column=2, padx=40, pady=10, sticky="e")


        #self.mudanca_color(0)
        self.mudanca_color(3)

    def mudanca_color(self, btn_i):
        
        for i, (btn, command) in enumerate(self.menu_btn):
            if i == btn_i:
                btn.configure(fg_color=Style.color('hover'))
                command()
            else:
                btn.configure(fg_color=Style.color('fg'))

    def dest_frame(self):
        if self.frame_inferior is not None:
            self.frame_inferior.destroy()
            self.frame_inferior = None

    #chamar telas

    def chamar_home(self):
        self.dest_frame()
        self.root.rowconfigure(1,weight=1)
        self.frame_inferior = ctk.CTkFrame(self.root, fg_color=Style.color('bg'))
        self.frame_inferior.grid(row=1, column=0, sticky="nsew")
        telaHome(self.frame_inferior)

    def chama_producao(self):
        self.dest_frame()
        self.root.rowconfigure(1,weight=1)
        self.frame_inferior = ctk.CTkFrame(self.root,fg_color=Style.color('bg'))
        self.frame_inferior.grid(row=1,column=0,sticky="nsew")
        telaProducao(self.frame_inferior,self)

    def chama_cliente(self):
        self.dest_frame()
        self.root.rowconfigure(1,weight=1)
        self.frame_inferior = ctk.CTkFrame(self.root,fg_color=Style.color('bg'))
        self.frame_inferior.grid(row=1,column=0,sticky="nsew")
        telaCliente(self.frame_inferior,self)

    def chama_pedido(self):

        self.dest_frame()
        self.root.rowconfigure(1,weight=1)
        self.frame_inferior = ctk.CTkFrame(self.root, fg_color=Style.color('bg'))
        self.frame_inferior.grid(row=1, column=0, sticky="nsew")
        telaPedido(self.frame_inferior)

    def chama_relatorio(self):
        print("Indo para a tela Relatório")

    def novo_pedido(self):
        print("Abrindo tela de Novo Pedido")
    