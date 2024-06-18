#Criado por Pablo Matias, pablomatias@hotmail.com
# Configurações iniciais
import pygame
import random

pygame.init()
pygame.display.set_caption("Jogo Snake Python")
largura, altura = 600, 400
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

# Cores (RGB)
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

# Parâmetos da cobrinha
tamanho_quadrado = 20
Velocidade_do_jogo = 10

def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x , comida_y

def desenhar_comida(tamanho , comida_x, comida_y):
    pygame.draw.rect(tela, verde, [comida_x, comida_y, tamanho, tamanho])

def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branca, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, vermelha)
    tela.blit(texto, [1, 1])

def selecionar_direcao(tecla):
    if tecla == pygame.K_DOWN:
        direcao_x = 0
        direcao_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        direcao_x = 0
        direcao_y = -tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        direcao_x = tamanho_quadrado
        direcao_y = 0
    elif tecla == pygame.K_LEFT:
        direcao_x = -tamanho_quadrado
        direcao_y = 0
    return direcao_x, direcao_y

# função para rodar o jogo
def rodar_jogo():
    #informar que o jogo não acabou
    fim_jogo = False

    x = largura / 2
    y = altura / 2

    direcao_x = 0
    direcao_y = 0

    tamanho_da_cobra = 1
    pixels = []

    comida_x, comida_y = gerar_comida()

    #Loop pra verificar se o jogo acabou
    while not fim_jogo:
        tela.fill(preta)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                direcao_x, direcao_y = selecionar_direcao(evento.key)
        
        # Desenhar comida
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)

        # Atualizar posição da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True

        x += direcao_x
        y += direcao_y

        # Desenhar cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_da_cobra:
            del pixels[0]    

        # Se a cobra bater no proprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x,y]:
                fim_jogo = True
        
        # Desenhar cobra
        desenhar_cobra(tamanho_quadrado, pixels)

        # Desenhar pontos
        desenhar_pontuacao(tamanho_da_cobra - 1)

        # Atualizar tela
        pygame.display.update()

        # Criar uma nova comida
        if x == comida_x and y == comida_y:
            tamanho_da_cobra += 1
            comida_x, comida_y = gerar_comida()


        relogio.tick(Velocidade_do_jogo)

rodar_jogo()