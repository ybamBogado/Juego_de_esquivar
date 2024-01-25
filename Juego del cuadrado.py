# Importamos pygame
import pygame
import sys
import random

# Inicializacion de pygame
pygame.init()
# Tamaño de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
# Titulo de la ventana
pygame.display.set_caption("Esquivando FIGURAS")
#icono
icono = pygame.image.load("assets\icono.png")
#FIJAR ICONO
pygame.display.set_icon(icono)
# Definimos algunos colores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
verde_oliva=(134,137,93)

#TAMAÑO Jugador
jugador_size= 50

#POSICION Jugador
jugador_pos=[screen_width/2 , screen_height - jugador_size*2]

#ENEMIGO
enemigo_size=50
enemigo_pos=[random.randint(0,screen_width - enemigo_size),0]
#Enemigo 2
enemigo_dos_size=20
enemigo_dos_pos=[random.randint(0,screen_width - enemigo_size),0]

#TEXTO CONTROLES
texto_controles = "Controles: flecha derecha y flecha izquierda"

# Definimos una fuente para el texto
font = pygame.font.SysFont("Arial", 32)
# Definimos dos botones para el menú
button_play = pygame.Rect(300, 200, 200, 50)
button_quit = pygame.Rect(300, 300, 200, 50)
# Definimos el texto de los botones
text_play = font.render("Jugar", True, black)
text_quit = font.render("Salir", True, black)

#--------------------METODOS---------------------------------------------------------------------------------------
#metodo de colisiones

def colision(pos_j,pos_e,enemy_size):
    jx=pos_j[0]
    jy=pos_j[1]
    ex=pos_e[0]
    ey=pos_e[1]    

    if (ex >= jx and ex <(jx+jugador_size))or (jx>= ex and jx <(ex+ enemy_size)):
        if (ey >= jy and ex <(jy+jugador_size))or (jy>= ey and jy <(ey+ enemy_size)):
            return True
    return False
                
# Funcion para dibujar el texto de los controles

def dibujar_texto_controles(screen, pos):
    #cambiar tamaño de fuente
    font = pygame.font.SysFont("Arial", 20)
    # Dibujamos el texto
    text_controles = font.render(texto_controles, True, white)
    screen.blit(text_controles, pos)
    #cambiar tamaño de fuente
    font = pygame.font.SysFont("Arial", 32)

#--------------------METODOS---------------------------------------------------------------------------------------




# Definimos una variable para el bucle principal
running = True
# Comenzamos el bucle principal
while running:
    # Rellenamos la pantalla de blanco
    screen.fill(black)
    # Dibujamos los botones en la pantalla
    pygame.draw.rect(screen, (134,137,93), button_play)
    pygame.draw.rect(screen, (134,137,93), button_quit)
    # Dibujamos el texto de los botones en el centro de los mismos
    screen.blit(text_play, (button_play.centerx - text_play.get_width() // 2, button_play.centery - text_play.get_height() // 2))
    screen.blit(text_quit, (button_quit.centerx - text_quit.get_width() // 2, button_quit.centery - text_quit.get_height() // 2))
    # Actualizamos la pantalla
    pygame.display.flip()
    # Obtenemos los eventos que ocurren
    for event in pygame.event.get():
        # Si el evento es salir de la ventana, terminamos el bucle
        if event.type == pygame.QUIT:
            running = False
        # Si el evento es hacer clic con el ratón, verificamos si se presionó algún botón
        if event.type == pygame.MOUSEBUTTONDOWN:
            # posición del ratón
            mouse_pos = pygame.mouse.get_pos()
            # Si se presionó el botón de jugar inicia el juego
            if button_play.collidepoint(mouse_pos):
                #para comprobar si funciona
                #print("Iniciar el juego")
                
                #bucle del juego 

                game_over = False

                #definir un reloj

                clock = pygame.time.Clock()

# #--------------------METODOS---------------------------------------------------------------------------------------
#                 #metodo de colisiones

#                 def colision(pos_j,pos_e,enemy_size):
#                     jx=pos_j[0]
#                     jy=pos_j[1]
#                     ex=pos_e[0]
#                     ey=pos_e[1]    

#                     if (ex >= jx and ex <(jx+jugador_size))or (jx>= ex and jx <(ex+ enemy_size)):
#                         if (ey >= jy and ex <(jy+jugador_size))or (jy>= ey and jy <(ey+ enemy_size)):
#                             return True
#                     return False
                
#                 # Funcion para dibujar el texto de los controles
#                 def dibujar_texto_controles(screen, pos):

#                 # Dibujamos el texto
#                 text_controles = font.render(texto_controles, True, black)
#                 screen.blit(text_controles, pos)

# #--------------------METODOS---------------------------------------------------------------------------------------


                while not game_over:
                    for event in pygame.event.get():
                        #Esto es para ver las acciones que se registran
                        #print(event)
                        if event.type == pygame.QUIT:#si se trata de cerrar el juego cerramos
                            sys.exit()

                    #MAPEO DE INPUTS

                        if event.type== pygame.KEYDOWN:

                        #VARIABLE PARA ALMACENAR POSICION DEL JUGADOR

                            x = jugador_pos[0]

                            if event.key == pygame.K_LEFT:
                            #pass ignora el if con pass
                                x-=jugador_size
                            if event.key== pygame.K_RIGHT:
                                x +=jugador_size
                        #if event.key==

                        #ACTUALIZAR COORDENADA DEL JUGADOR
                            jugador_pos[0]=x

                #CAMBIO DE COLOR DE LA PANTALLA

                    screen.fill(black)

                    #MOVIMIENTO ENEMIGO
                    if enemigo_pos[1]>= 0 and enemigo_pos[1]< screen_height:
                        enemigo_pos[1] += 20
                    else:
                        enemigo_pos[0] = random.randint(0 ,screen_width - enemigo_size )
                        enemigo_pos[1] = 0
                    
                    #MOVIMIENTO ENEMIGO 2
                    if enemigo_dos_pos[1]>= 0 and enemigo_dos_pos[1]< screen_height:
                        enemigo_dos_pos[1] += 20
                    else:
                        enemigo_dos_pos[0] = random.randint(0 ,screen_width - enemigo_size )
                        enemigo_dos_pos[1] = 0

                    #INVOCAR FUNCION

                    if colision(jugador_pos,enemigo_pos,enemigo_size):
                        game_over=True
                        
                    if colision(jugador_pos,enemigo_dos_pos,enemigo_dos_size):
                        game_over=True


                    #dentro del for creamos nuestro personaje que sera una figura geometrica

                    #DIBUJAR ENEMIGO

                    enemigo = pygame.draw.rect(screen, (0,255,0),(enemigo_pos[0],enemigo_pos[1], enemigo_size,enemigo_size))
                    
                    #Enemigo 2
                    
                    enemigo = pygame.draw.circle(screen, verde_oliva ,(enemigo_dos_pos[0],enemigo_dos_pos[1]), enemigo_dos_size)

                    #DIBUJAR JUGAdOR

                    jugador = pygame.draw.rect(screen, red,(jugador_pos[0],jugador_pos[1], jugador_size,jugador_size))

                        # Dibujar texto de controles
                    dibujar_texto_controles(screen, (2 , screen_height - jugador_size ))

                    #FOTOGRAMAS
                    clock.tick(30)

                    #PARA QUE SE ACTUALICE
                    pygame.display.update()
                
            # If para finalizar bucle principal
            if button_quit.collidepoint(mouse_pos):
                running = False
# Salimos de pygame
pygame.quit()
