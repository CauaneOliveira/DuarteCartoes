import customtkinter as ctk
from telas.tela_home import telaHome

class Menu:
    def __init__(self, root, instance):
        self.root = root
        self.instance = instance

        self.root.rowconfigure(0, weight=0)  # altura fixa
        self.root.columnconfigure(0, weight=1)  # horizontal fixo
        
        buttons = [
            ("Home", self.go_to_home),
            ("Produção", self.go_to_production),
            ("Cliente", self.go_to_client),
            ("Pedido", self.go_to_order),
            ("Relatório", self.go_to_report),
        ]

        frame = ctk.CTkFrame(root, fg_color="#2E402D", height=100)  # Cor e altura ajustada
        frame.grid(row=0, column=0, sticky="ew")  # Expansão horizontal (topo da janela)
        frame.columnconfigure(0, weight=1)  # Espaço para o logo
        frame.columnconfigure(1, weight=5)  # Espaço central para os botões
        frame.columnconfigure(2, weight=1)  # Espaço para o botão "Novo Pedido"

        btn_logo = ctk.CTkButton(frame,text="DUARTE\nCARTÕES",font=("Arial", 15, "bold"),text_color="white",fg_color="#2E402D", hover=False,corner_radius=10,width=120,command=lambda:self.change_button_color(0))
        btn_logo.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        central_frame = ctk.CTkFrame(frame, fg_color="#2E402D")
        central_frame.grid(row=0, column=1, pady=10, sticky="ew")
        central_frame.columnconfigure(tuple(range(len(buttons))), weight=1)

        self.menu_buttons = []
        for index, (text, command) in enumerate(buttons):
            button = ctk.CTkButton(central_frame,text=text,font=("Arial", 18, "bold"),width=150, height=40,text_color="white",fg_color="#698F67",hover_color="#4E7050", corner_radius=3,command=lambda b=index: self.change_button_color(b))
            button.grid(row=0, column=index, padx=10)
            self.menu_buttons.append((button, command))

        btn_new_order = ctk.CTkButton(frame,text="Novo Pedido",font=("Arial", 18, "bold"),width=150, height=40,text_color="white",fg_color="#698F67",hover_color="#4E7050",corner_radius=5,command=self.new_order)
        btn_new_order.grid(row=0, column=2, padx=10, pady=10, sticky="e")

    def change_button_color(self, button_index):
        
        for index, (button, command) in enumerate(self.menu_buttons):
            if index == button_index:
                button.configure(fg_color="#4E7050")  # Cor do botão selecionado
                command()  # Executa a função associada ao botão
            else:
                button.configure(fg_color="#698F67")  # Cor padrão dos outros botões

    def go_to_home(self):
        telaHome(self.instance)

    def go_to_production(self):
        print("Indo para a tela Produção")

    def go_to_client(self):
        print("Indo para a tela Cliente")

    def go_to_order(self):
        print("Indo para a tela Pedido")

    def go_to_report(self):
        print("Indo para a tela Relatório")

    def new_order(self):
        print("Abrindo tela de Novo Pedido")
