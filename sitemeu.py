import flet as ft
import pyautogui
import time



def main(pagina):
    
    noticia2=ft.Text("A onda de calor que atingirá o mundo em 2024 \n A Internet simplesmente não foi projetada para lidar com esse nível de calor que gera interferência na comunicação. Portanto, o período de 2024 a 2028 é um momento em que toda a Internet poderia ficar desligada por semanas a meses no caso de uma tempestade solar realmente extrema.")
                     
    texto=ft.Text("Notícias") 
    

    def ir_site(Evento):
      
     
      pyautogui.press("win")
      time.sleep(2)
      pyautogui.write(F"{navegador.value}")
      time.sleep(2)
      pyautogui.press("Enter")
      time.sleep(10)
      pyautogui.click(x=672, y=68)
      
    
      pyautogui.write('https://www.opovo.com.br/noticias/curiosidades/2023/11/14/tempestade-solar-pode-deixar-a-terra-sem-internet-por-meses-em-2024.html#:~:text=Onda%20de%20calor%3A%20"apocalipse%20da%20Internet"&text=Portanto%2C%20o%20período%20de%202024,introduziu%20Becker%20sobre%20seu%20estudo.')
      pyautogui.press('Enter')

    def abrir_popup2(Evento):
      pagina.dialog=popup2
      pagina.add(botao_link)
      pagina.remove(botao_navegador)
      
      popup2.open=True



      
      
      pagina.update()
      


    botao_navegador=ft.ElevatedButton("Saber mais" , on_click= abrir_popup2,
                                      )
    
    botao_link=ft.FilledTonalButton("Ler mais", on_click=ir_site)
    navegador=ft.TextField(label="Digite seu navegador para ir par a notícia completa")
   
    popup2= ft.AlertDialog(modal=True, open=False, content= navegador , actions=[(botao_link)])
    
  
    

    def ler_mais(Evento):
       popup.open = False
       pagina.add(noticia2)
       pagina.add(botao_navegador)
       pagina.add(popup2)
       pagina.update()
                  
       
       



    título_popup = ft.Text("últimas horas" )
    botao_lermais=ft.TextButton("interresante, quero ler mais", on_click= ler_mais)
    noticia=ft.Text('A Internet pode parar de funcionar em 2024 por alguns meses, quer saber mais? Clique no botão abaixo')

    popup= ft.AlertDialog(modal=True , open= False , title= título_popup, content=noticia, actions=[botao_lermais] )
    def abrir_popup(Evento):
      pagina.dialog=popup
      pagina.remove(botao_iniciar)
      popup.open=True
      
      pagina.update()
    
    botao_iniciar=ft.FloatingActionButton("começar a ler", on_click= abrir_popup)




    pagina.add(texto)
    pagina.add(popup)
    
    pagina.add(botao_iniciar)
   


ft.app(target=main)
    