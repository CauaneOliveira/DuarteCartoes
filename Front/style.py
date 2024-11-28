from PIL import Image
import customtkinter as ctk

class Style:
    def color (color_nome):

        colors = {
            
            'bg_top': "#2C4631", # Cor Top - Verde Escuro
            'bg' : "#D9D9D9",  # Cor de fundo - Cinza
            'bg_frame' : "#E7E7E7",  # Cor de fundo do frame - Quase Branco
            'fg' : "#77a075",  # Cor para botões - Verde Claro
            'hover' : "#3c743c",  # Cor ao passar o mouse - Verde Escuro
            'fg_2' : "#a0a0a0", # Cor para botões - Cinza escuro
            'hover_2' : "#cdcdcd", # Cor ao passar o mouse - Cinza Claro
            'fg_red' : "#c30000", #Cor do botao - Vermelho
            'hover_red':"#6f0000", #Cor ao passar o mouse - Vermelho claro
            'bg_frame2': "#ACABAB" #Cor para titulo de frame - Cinza Escuro
        }
        return colors.get(color_nome)
    
    def img(img_nome):
        
        def abrir_img(caminho,size):

            img = ctk.CTkImage(Image.open(caminho), size=size)  
            return img  
      
        imgs={'img_icon_producao':abrir_img("img\\icon_producao.png",(40, 40))}
        return imgs.get(img_nome)
    
    def centralizar_janela(root, largura, altura):
        
        tela_largura = root.winfo_screenwidth()
        tela_altura = root.winfo_screenheight()

        x = (tela_largura // 2) - (largura // 2)
        y = (tela_altura // 2) - (altura // 2)

        root.geometry(f"{largura}x{altura}+{x}+{y}")