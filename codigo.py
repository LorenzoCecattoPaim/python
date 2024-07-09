import flet as ft
def main(Pagina):
    texto= ft.Text("Mateus e Marta")

    chat= ft.Column()

    def enviar_mensagem_tunel(mensagem):
        print(mensagem)
       
        texto_mensagem=ft.Text(mensagem)
        chat.controls.append(texto_mensagem)
        Pagina.update()

    Pagina.pubsub.subscribe(enviar_mensagem_tunel)


    def enviar_mensagem(Evento):
        Pagina.pubsub.send_all(f'{nome_usuário.value}:{campo_mensagem.value}')
        campo_mensagem.value = ""   
        Pagina.update()
        
    


    campo_mensagem= ft.TextField(label=' envie uma mensagem ', on_submit=enviar_mensagem)
    botao_enviar=ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar=ft.Row([botao_enviar, campo_mensagem])

    def entrar_chat(Evento):
        popup.open = False
        Pagina.remove(botao_Iniciar)
        Pagina.remove(texto)
        Pagina.add(chat)
        Pagina.pubsub.send_all(f'{nome_usuário.value} ENTROU NO CHAT')
        Pagina.add(linha_enviar)
        Pagina.update()




    Titulo_popup= ft.Text("BEM VINDO ao meu chat")
    nome_usuário = ft.TextField(label= "Escreva seu nome pra usar na conversa")
    botao_entrar= ft.ElevatedButton("Entrar na conversa", on_click=entrar_chat)
    popup=ft.AlertDialog(open= False, modal =True, title=Titulo_popup , content= nome_usuário, actions=[botao_entrar])









    def abrir_popup(Evento):
        Pagina.dialog= popup
        popup.open= True
        Pagina.update()
        
    
       
    botao_Iniciar=ft.ElevatedButton("iniciar conversa com muito amor", on_click=abrir_popup)
    Pagina.add (texto)
    Pagina.add (botao_Iniciar)




ft.app(target=main, view=ft.WEB_BROWSER)

