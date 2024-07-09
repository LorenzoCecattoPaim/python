import pygame
import os
import random
TELA_ALTURA=500
TELA_LARGURA=800

IMAGEM_CANO=pygame.transform.scale2x(pygame.image.load(os.path.join("html1","pipe.png")))
IMAGEM_CHAO=pygame.transform.scale2x(pygame.image.load(os.path.join("html1","base.png")))
IMAGEM_BACKGROUND=pygame.transform.scale2x(pygame.image.load(os.path.join("html1","bg.png")))
IMAGENS_PASSARO=[
    pygame.transform.scale2x(pygame.image.load(os.path.join("html1","bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("html1","bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("html1","bird3.png"))),]

pygame.font.init(
)
Fonte_pontos=pygame.font.SysFont("arial", 50)

class Passaro: 
    imgs=IMAGENS_PASSARO
    ROTACAO_MAXIMA=25
    VELOCIDADE_ROTACAO=20
    TEMPO_ANIMAÇAO=5

    def __init__(self, x, y):
        self.x=x
        self.y=y
        self.angulo=0
        self.velocidade=0
        self.altura=0
        self.tempo=0
        self.contagem_imagem=0
        self.imagem=self.imgs[0]

    def pular(self):
        self.velocidade= -10.5
        self.tempo=0
        self.altura=self.y

    def mover(self):
        #calcular deslocamento
        self.tempo += 1
        deslocamento= 1.5 *  (self.tempo**2)+ self.velocidade*self.tempo
        #formula do sorvetão^
        #restringir velocidade
        #angulo
        if deslocamento >16:
            deslocamento=16
        elif deslocamento<0:
            deslocamento -=2 #ganho extra do pulo

        self.y += deslocamento
        if deslocamento<0 or self.y < (self.altura +50): #animaçao
            if self.angulo< self.ROTACAO_MAXIMA:
             self.angulo=self.ROTACAO_MAXIMA
        else:
            if self.angulo> -90:
                self.angulo -= self.VELOCIDADE_ROTACAO   
    def desenhar(self):
        #QUAL IMAGEM USAR
        self.contagem_imagem+=1

        if self.contagem_imagem> self.TEMPO_ANIMAÇAO:
            self.imagem=self.imgs[0]
        elif self.contagem_imagem<self.TEMPO_ANIMAÇAO*2:    
            self.imagem=self.imgs[1]
        elif self.contagem_imagem<self.TEMPO_ANIMAÇAO*3:
            self.imagem=self.imgs[2]
        
        elif self.contagem_imagem> self.TEMPO_ANIMAÇAO*4:
            self.imagem=self.imgs[1]
        elif self.contagem_imagem>= self.TEMPO_ANIMAÇAO*4+1:
            self.imagem=self.imgs[0]
            self.contagem_imagem=0
        #definir imagem
        #subir
        #cair nao usar asa
        if self.angulo<= -80:
            self.imagem= self.imgs[1]
            self.contagem_imagem= self.TEMPO_ANIMAÇAO*2
        imagem_rotacionada=pygame.transform.rotate(self.imagem, self.angulo) 
        posicao_centro_imagem= self.imagem.get_rect(topleft=(self.x, self.y)). center
        retangulo=imagem_rotacionada.get_rect(center=posicao_centro_imagem)
        

class Cano:
    pass

class chao:
    pass

