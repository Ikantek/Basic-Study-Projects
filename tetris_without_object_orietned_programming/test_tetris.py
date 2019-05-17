####################################################
#          '''IMPORTING THINGS'''
####################################################
import pygame
import time
from random import randint

####################################################
#          '''SCREEN VARIABLES'''
####################################################
pygame.init()
levels=[10,150,200]
levels_clock=[400,300,150,100]
empty_space=2
rows=21
columns=18
screen_width=20*(columns-2)+2*(columns-1)+125
screen_height=20*(rows-1)+2*(rows-1)
x_matrix=[0]*(columns-2)
x_matrix[0]=2
x_matrix2=[380,402,424,446]
y_matrix2=[50,72,94,116,138]
for i in range (1,columns-2):
    x_matrix[i]=x_matrix[i-1]+22
y_matrix=[0]*(rows-1)
y_matrix[0]=2
for i in range (1,rows-1):
    y_matrix[i]=y_matrix[i-1]+22
#print (x_matrix)
matrix = [[0 for x in range(columns)] for y in range(rows)] 
for i in range (0, columns):
    matrix[rows-1][i]=-1
for j in range (0, rows):
    matrix[j][0]=-1
    matrix[j][columns-1]=-1
clock=pygame.time.Clock()
window=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Tetris")
####################################################
#             BLOCKS
####################################################

tetris_blocks=[0,1,2,3,4,5,6]
position1 = [
            [7,7,0,0],
            [7,7,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position2 = [
            [1,1,1,1],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position3 = [
            [1,0,0,0],
            [1,0,0,0],
            [1,0,0,0],
            [1,0,0,0],
            [0,0,0,0],
]
position4 = [
            [2,2,0,0],
            [0,2,2,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position5 = [
            [0,2,0,0],
            [2,2,0,0],
            [2,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position6 = [
            [0,3,3,0],
            [3,3,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position7 = [
            [3,0,0,0],
            [3,3,0,0],
            [0,3,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position8 = [
            [0,4,0,0],
            [0,4,0,0],
            [4,4,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position9 = [
            [4,0,0,0],
            [4,4,4,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position10 = [
            [4,4,0,0],
            [4,0,0,0],
            [4,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position11 = [
            [4,4,4,0],
            [0,0,4,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position12 = [
            [5,0,0,0],
            [5,0,0,0],
            [5,5,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position13 = [
            [5,5,5,0],
            [5,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position14 = [
            [5,5,0,0],
            [0,5,0,0],
            [0,5,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position15 = [
            [0,0,5,0],
            [5,5,5,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position16 = [
            [6,6,6,0],
            [0,6,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position17 = [
            [0,6,0,0],
            [6,6,0,0],
            [0,6,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position18 = [
            [0,6,0,0],
            [6,6,6,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position19 = [
            [6,0,0,0],
            [6,6,0,0],
            [6,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position20 = [
            [8,8,8,0],
            [8,0,8,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position21 = [
            [8,8,0,0],
            [0,8,0,0],
            [8,8,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position22 = [
            [8,0,8,0],
            [8,8,8,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
position23 = [
            [8,8,0,0],
            [8,0,0,0],
            [8,8,0,0],
            [0,0,0,0],
            [0,0,0,0],
]
tetris_shapes = [
	[position1,
     position1,
     position1,
     position1],
    [position2,
	 position3,
     position2,
     position3],
	
	[position4,
	 position5,
     position4,
     position5],
	
	[position6,
	 position7,
     position6,
     position7],
	
	[position8,
     position9,
     position10,
	 position11],
	
	[position12,
     position13,
     position14,
	 position15],
  
    [position16,
     position17,
     position18,
	 position19],
    [position20,
     position21,
     position22,
	 position23]
]

####################################################
#                '''DEFINING COLORS'''
####################################################
BLACK=(0,0,0)
RED=(255,0,0)
LIGHT_RED=(200,0,0)
GREEN=(0,255,0)
LIGHT_GREEN=(0,200,0)
YELLOW=(255,255,0)
LIGHT_YELLOW=(220,220,0)
WHITE=(255,255,255)
PINK=(255,0,255)
ORANGE=(255,80,0)
BLUE=(0,0,255)
LIGHT_BLUE=(0,0,170)

####################################################
#          '''VARIABLES OF POSITION'''
####################################################
velocity=20
square_height=20
square_width=20
x=0
y=0
PLACE=(x, y, square_width, square_height)
####################################################
#          '''DEF OF DRAW FUNCTION'''
####################################################
def draw(matrix,rows,columns):
        k=0
        for i in range (0,rows-1):
            z=0
            for j in range (1,columns-1):
                if (matrix[i][j]==0):
                    PLACE=(x_matrix[z], y_matrix[k], square_width, square_height)
                
                
                    pygame.draw.rect(window, BLACK, PLACE)
                if (matrix[i][j]==1):
                    PLACE=(x_matrix[z], y_matrix[k], square_width, square_height)
                
                
                    pygame.draw.rect(window, RED, PLACE)
                if (matrix[i][j]==2):
                    PLACE=(x_matrix[z], y_matrix[k], square_width, square_height)
                
                
                    pygame.draw.rect(window, GREEN, PLACE)
                if (matrix[i][j]==3):
                    PLACE=(x_matrix[z], y_matrix[k], square_width, square_height)
                
                
                    pygame.draw.rect(window, YELLOW, PLACE)
                if (matrix[i][j]==4):
                    PLACE=(x_matrix[z], y_matrix[k], square_width, square_height)
                
                
                    pygame.draw.rect(window, WHITE, PLACE)
                if (matrix[i][j]==5):
                    PLACE=(x_matrix[z], y_matrix[k], square_width, square_height)
                
                
                    pygame.draw.rect(window, PINK, PLACE)
                if (matrix[i][j]==6):
                    PLACE=(x_matrix[z], y_matrix[k], square_width, square_height)
                
                
                    pygame.draw.rect(window, ORANGE, PLACE)
                if (matrix[i][j]==7):
                    PLACE=(x_matrix[z], y_matrix[k], square_width, square_height)
                
                
                    pygame.draw.rect(window, BLUE, PLACE)
                if (matrix[i][j]==8):
                    PLACE=(x_matrix[z], y_matrix[k], square_width, square_height)
                
                
                    pygame.draw.rect(window, LIGHT_GREEN, PLACE)
                z+=1
            k+=1
def draw2(matrix):
        k=0
        for i in range (0,5):
            z=0
            for j in range (0,4):
                if (matrix[i][j]==0):
                    PLACE=(x_matrix2[z], y_matrix2[k], square_width, square_height)
                
                
                    pygame.draw.rect(window, BLACK, PLACE)
                if (matrix[i][j]==1):
                    PLACE=(x_matrix2[z], y_matrix2[k], square_width, square_height)
                
                
                    pygame.draw.rect(window, RED, PLACE)
                if (matrix[i][j]==2):
                    PLACE=(x_matrix2[z], y_matrix2[k], square_width, square_height)
                
                
                    pygame.draw.rect(window, GREEN, PLACE)
                if (matrix[i][j]==3):
                    PLACE=(x_matrix2[z], y_matrix2[k], square_width, square_height)
                
                
                    pygame.draw.rect(window, YELLOW, PLACE)
                if (matrix[i][j]==4):
                    PLACE=(x_matrix2[z], y_matrix2[k], square_width, square_height)
                
                
                    pygame.draw.rect(window, WHITE, PLACE)
                if (matrix[i][j]==5):
                    PLACE=(x_matrix2[z], y_matrix2[k], square_width, square_height)
                
                
                    pygame.draw.rect(window, PINK, PLACE)
                if (matrix[i][j]==6):
                    PLACE=(x_matrix2[z], y_matrix2[k], square_width, square_height)
                
                
                    pygame.draw.rect(window, ORANGE, PLACE)
                if (matrix[i][j]==7):
                    PLACE=(x_matrix2[z], y_matrix2[k], square_width, square_height)
                
                
                    pygame.draw.rect(window, BLUE, PLACE)
                if (matrix[i][j]==8):
                    PLACE=(x_matrix2[z], y_matrix2[k], square_width, square_height)
                
                
                    pygame.draw.rect(window, LIGHT_GREEN, PLACE)
                z+=1
            k+=1
                
####################################################
#          '''DEF OF MOVE RIGHT FUNCTION'''
####################################################
def check_right(matrix,y_position,x_position,actual_block,w,A):
    check=True
    for i in range(w,-1,-1):
        if(y_position+i<rows):
            for j in range (A[i],-1,-1):
                if(x_position+j+1<columns):
                    if (matrix[y_position+i][x_position+j]!=0):
                        if (matrix[y_position+i][x_position+j+1]!=0):
                            check=False
                        break
            if(check==False):
                break
    return check
def move_right(matrix,y_position,x_position,actual_block,w,A):
    check=check_right(matrix,y_position,x_position,actual_block,w,A)
    if (check==True):
        for i in range(w,-1,-1):
            if(y_position+i<rows):
                for j in range (A[i],-1,-1):
                    if(x_position+j+1<columns):
                        if (actual_block[i][j]!=0):
                            matrix[y_position+i][x_position+j+1]=actual_block[i][j]#matrix[y_position+i][x_position+j]
                            matrix[y_position+i][x_position+j]=0
        x_position+=1                
        draw (matrix,rows,columns)
        pygame.display.update()
                       
    return x_position
####################################################
#          '''DEF OF MOVE LEFT FUNCTION'''
####################################################
def check_left(matrix,y_position,x_position,actual_block,w,A):
    check=True
    for i in range(0,w+1):
        if(y_position+i<rows):
            for j in range (0,A[i]+1):
                if(x_position+j>0):
                    if (matrix[y_position+i][x_position+j]!=0):
                        if (matrix[y_position+i][x_position+j-1]!=0):
                            check=False
                        break
            if(check==False):
                break
    return check
def move_left(matrix,y_position,x_position,actual_block,w,A):
    check=check_left(matrix,y_position,x_position,actual_block,w,A)
    if (check==True):
        for i in range(0,w+1):
            if(y_position+i<rows):
                for j in range (0,A[i]+1):
                    if(x_position+j-1>0):
                        if (actual_block[i][j]!=0):
                            matrix[y_position+i][x_position+j-1]=actual_block[i][j]#matrix[y_position+i][x_position+j]
                            matrix[y_position+i][x_position+j]=0
        
        x_position-=1             
        draw (matrix,rows,columns)
        pygame.display.update()
                       
    return x_position

####################################################
#          '''DEF OF GAME_OVER FUNCTION'''
####################################################
def game_overr():
    message_display('Game Over')
def text_objects(text,font_size):
    TextSurface=font_size.render(text, True, RED)
    return TextSurface, TextSurface.get_rect()
def text_objects2(text,font_size,color):
    TextSurface=font_size.render(text, True, color)
    return TextSurface, TextSurface.get_rect()
def message_display(text):
    LargeText=pygame.font.Font('freesansbold.ttf',50)
    TextSurface, TextRect= text_objects(text, LargeText)
    TextRect.center=((screen_width/2),(screen_height)/2)
    window.blit(TextSurface, TextRect) 
    pygame.display.update()

    time.sleep(4)
    window.fill(BLACK)
    pygame.display.update()
    menu()
####################################################
#          '''Score, block, level'''   
####################################################
def right_window(next_block,score,level,matrix):
     window.fill(BLACK)
     draw (matrix,rows,columns)
     pygame.draw.line(window,RED,(356,0),(356,440))
     
     next_block_Text=pygame.font.Font('freesansbold.ttf',20)
     TextSurface, TextRect= text_objects2("Next block:", next_block_Text, BLUE)
     TextRect.center=(418,25)
     window.blit(TextSurface, TextRect)
     draw2(next_block)
     
     scorez=pygame.font.Font('freesansbold.ttf',20)
     TextSurface, TextRect= text_objects2("SCORE:", scorez, GREEN)
     TextRect.center=(418,150)
     window.blit(TextSurface, TextRect)
     score_str=str(score)
     TextSurface, TextRect= text_objects2(score_str, scorez, LIGHT_GREEN)
     TextRect.center=(418,175)
     window.blit(TextSurface, TextRect)
     
     levelz=pygame.font.Font('freesansbold.ttf',20)
     TextSurface, TextRect= text_objects2("LEVEL:", levelz, YELLOW)
     TextRect.center=(418,200)
     window.blit(TextSurface, TextRect)
     level_str=str(level+1)
     TextSurface, TextRect= text_objects2(level_str, levelz, YELLOW)
     TextRect.center=(418,225)
     window.blit(TextSurface, TextRect)
    
    
####################################################
#          '''help LOOP'''   
####################################################
def helpp():
    z=True
    while (z):
        mouse=pygame.mouse.get_pos()
        click =pygame.mouse.get_pressed()
        window.fill(WHITE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        arrows_mov = pygame.image.load('movement_keys.png')
        smalltext=pygame.font.Font('freesansbold.ttf',30)
        textSurface, textRect=text_objects2("- MOVEMENT KEYS", smalltext, RED)
        textRect.center=(300,85)
        window.blit(textSurface, textRect)
        
        
        arrow_up = pygame.image.load('key_up.png')
        smalltext=pygame.font.Font('freesansbold.ttf',30)
        textSurface, textRect=text_objects2("- PRESS TO PAUSE", smalltext, RED)
        textRect.center=(300,185)
        window.blit(textSurface, textRect)
        
        arrow_down = pygame.image.load('key_down.png')
        smalltext=pygame.font.Font('freesansbold.ttf',30)
        textSurface, textRect=text_objects2("- PRESS TO ROTATE", smalltext, RED)
        textRect.center=(300,285)
        window.blit(textSurface, textRect)
        if ((screen_width/2)-50+100 >mouse[0]>(screen_width/2)-50 and (405>mouse[1]>365)):
                pygame.draw.rect(window, RED,((screen_width/2)-50,365,100,40))
                if (click[0]==1):
                    menu()
        else:
            pygame.draw.rect(window, LIGHT_RED,((screen_width/2)-50,365,100,40))
        smalltext=pygame.font.Font('freesansbold.ttf',20)
        textSurface, textRect=text_objects2("BACK", smalltext, BLACK)
        textRect.center=((screen_width/2),385)
        window.blit(textSurface, textRect)
        
        window.blit(arrows_mov,(10, 50))
        window.blit(arrow_up,(50, 150))
        window.blit(arrow_down,(50, 250))
        
        pygame.display.update()
        clock.tick(15)
####################################################
#          '''MENU LOOP'''   
####################################################
    
def menu():
    intro=True
    while (intro):
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                intro=False
                pygame.quit()
                quit()
        if (intro):
            window.fill(BLACK)
            LargeText=pygame.font.Font('freesansbold.ttf',50)
            TextSurface, TextRect= text_objects("TETRIS", LargeText)
            TextRect.center=((screen_width/2),50)
            window.blit(TextSurface, TextRect)
            
            mouse=pygame.mouse.get_pos()
            click =pygame.mouse.get_pressed()
            
            ########PLAY##########
            if ((screen_width/2)-50+100 >mouse[0]>(screen_width/2)-50 and (140>mouse[1]>100)):
                pygame.draw.rect(window, GREEN,((screen_width/2)-50,100,100,40))
                if (click[0]==1):
                    game_loop()
            else:
                pygame.draw.rect(window, LIGHT_GREEN,((screen_width/2)-50,100,100,40))
            smalltext=pygame.font.Font('freesansbold.ttf',20)
            textSurface, textRect=text_objects2("PLAY", smalltext, BLACK)
            textRect.center=((screen_width/2),120)
            window.blit(textSurface, textRect) 
            
            '''########SCOREBOARD#####
            if ((screen_width/2)-50+100 >mouse[0]>(screen_width/2)-50 and (225>mouse[1]>175)):
                pygame.draw.rect(window, YELLOW,((screen_width/2)-50,175,100,40))
            else:
                pygame.draw.rect(window, LIGHT_YELLOW,((screen_width/2)-50,175,100,40))
            smalltext=pygame.font.Font('freesansbold.ttf',12)
            textSurface, textRect=text_objects2("SCOREBOARD", smalltext, BLACK)
            textRect.center=((screen_width/2),195)
            window.blit(textSurface, textRect) 
            '''
            ########HELP#####
            if ((screen_width/2)-50+100 >mouse[0]>(screen_width/2)-50 and (225>mouse[1]>175)):
                pygame.draw.rect(window, BLUE,((screen_width/2)-50,175,100,40))
                if (click[0]==1):
                    helpp()
            else:
                pygame.draw.rect(window, LIGHT_BLUE,((screen_width/2)-50,175,100,40))
            smalltext=pygame.font.Font('freesansbold.ttf',20)
            textSurface, textRect=text_objects2("HELP", smalltext, BLACK)
            textRect.center=((screen_width/2),195)
            window.blit(textSurface, textRect) 
            
            ########EXIT#####
            if ((screen_width/2)-50+100 >mouse[0]>(screen_width/2)-50 and (290>mouse[1]>250)):
                pygame.draw.rect(window, RED,((screen_width/2)-50,250,100,40))
                if (click[0]==1):
                    pygame.quit()
                    quit()
            else:
                pygame.draw.rect(window, LIGHT_RED,((screen_width/2)-50,250,100,40))
            smalltext=pygame.font.Font('freesansbold.ttf',20)
            textSurface, textRect=text_objects2("EXIT", smalltext, BLACK)
            textRect.center=((screen_width/2),270)
            window.blit(textSurface, textRect)
            
            
            pygame.display.update()
            clock.tick(15)
####################################################
#          PAUSE   
####################################################
def Paused(paused,matrix,rows,columns,next_block,score,level):
    if (paused):
        message_display_true('Paused')
        time.sleep(1)
    if (paused==False):
        window.fill(BLACK)
        draw (matrix,rows,columns)
        right_window(next_block,score,level,matrix)
        message_display_true('Game starts in:')
        time.sleep(1)
        window.fill(BLACK)
        draw (matrix,rows,columns)
        right_window(next_block,score,level,matrix)
        
        for i in range(3,0,-1):
            right_window(next_block,score,level,matrix)
            s=str(i)
            message_display_true(s)
            time.sleep(1)
            window.fill(BLACK)
            draw (matrix,rows,columns)
            
            pygame.display.update()
            
        window.fill(BLACK)
        draw (matrix,rows,columns)
        
        right_window(next_block,score,level,matrix)
        pygame.display.update()
def message_display_true(text):
    LargeText=pygame.font.Font('freesansbold.ttf',30)
    TextSurface, TextRect= text_objects(text, LargeText)
    TextRect.center=((screen_width/2),(screen_height)/2)
    window.blit(TextSurface, TextRect) 
    pygame.display.update()
  
####################################################
#          '''DEF OF CLEARING FULL LANES'''   
####################################################
def clearing_lanes(matrix,rows,columns,score,level,levels):
    z=0
    for i in range (1,rows-1):
        for j in range(1,columns-1):
            if (matrix[i][j]!=0):
                z+=1
                if(z==columns-2):
                    for k in range(i,0,-1):
                        for l in range(1,columns-1):
                            matrix[k][l]=matrix[k-1][l]
                            matrix[k-1][l]=0
                    score=score+10
                    for m in range(0,len(levels)):
                        if (score==levels[m]):
                            level+=1
                    
                    z=0
                    
                #print (z)
            else:
                z=0
                break
    return matrix,score,level
####################################################
#          '''ROTATION'''   
####################################################
def rotation(matrix,tetris_shapes,which_block,y_position,x_position,which_rotation,actual_block,w,A):
    
    if (which_rotation==3):
        which_rotation=0
    else:
        which_rotation+=1
    new_block=tetris_shapes[which_block][which_rotation]
    
    check=True
    for i in range(0,4):
        if(y_position+i<rows):
            for j in range (3,-1,-1):
                z=100
                if(x_position+j>0):
                    temporary=x_position
                    if (x_position+j>columns-1):
                            x_position=x_position-(j+1)
                            z=-1
                    if (new_block[i][j]!=0):
                        if (new_block[i][j]!=actual_block[i][j]):
                                
                            if (matrix[y_position+i][x_position+j]!=0):
                                print (x_position+j)
                                print (x_position)
                                print('')
                                check=False
                                break
                            else:
                                x_position=temporary
                if(z==-1):
                   x_position=temporary 
        if(check==False):
            break
        
    
    if(check==True):
        A[0]*4
        for i in range (0,4):
            for j in range (0,4):
                if(actual_block[i][j]!=0):
                   matrix[y_position+i][x_position+j]=0 
        for i in range (0,4):
            for j in range (0,4):
                if (new_block[i][j]!=0):
                    matrix[y_position+i][x_position+j]=new_block[i][j]
                    w=i
                    A[i]=j
        actual_block=new_block
    else:
        which_rotation-=1
        if(which_rotation==-1):
            which_rotation=3
    return matrix,w,A,actual_block,which_rotation   
####################################################
#                    '''GAME LOOP'''
####################################################


def game_loop():
    level=0
    score=0
    window.fill(BLACK)
    pygame.key.set_repeat(0,50)
    paused=False
    rows=21
    columns=18
    x_matrix=[0]*(columns-2)
    x_matrix[0]=2
    for i in range (1,columns-2):
        x_matrix[i]=x_matrix[i-1]+22
    y_matrix=[0]*(rows-1)
    y_matrix[0]=2
    for i in range (1,rows-1):
        y_matrix[i]=y_matrix[i-1]+22
    #print (x_matrix)
    matrix = [[0 for x in range(columns)] for y in range(rows)] 
    for i in range (0, columns):
        matrix[rows-1][i]=-1
    for j in range (0, rows):
        matrix[j][0]=-1
        matrix[j][columns-1]=-1
        run = True
    x_position=int(columns/2)
    y_position=0
    check = True
    next_piece=True
    which_block=randint(0,7)
    next_block=tetris_shapes[which_block][0]
    while (run):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit
                run=False
        
        keys=pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paused=not paused
            Paused(paused,matrix,rows,columns,next_block,score,level)
            
        
        if not (paused):        
        
            if (next_piece==True):
                
                which_rotation=0
                #print (matrix)
                A=[0]*4
                actual_block=next_block
                first=which_block
                which_block=randint(0,7)
                next_block=tetris_shapes[which_block][which_rotation]
                for i in range (0,4):
                    for j in range (0,4):
                        if (actual_block[i][j]!=0):
                            if (matrix[y_position+i][x_position+j]==0):
                                matrix[y_position+i][x_position+j]=actual_block[i][j]
                                w=i
                                A[i]=j
                                
                next_piece=False                
                draw (matrix,rows,columns)
                right_window(next_block,score,level,matrix)
                
                pygame.display.update()
            
            if keys[pygame.K_RIGHT]:
                x_position=move_right(matrix,y_position,x_position,actual_block,w,A)
            if keys[pygame.K_LEFT]:
                x_position=move_left(matrix,y_position,x_position,actual_block,w,A)
            if keys[pygame.K_DOWN]:
                matrix,w,A,actual_block,which_rotation=rotation(matrix,tetris_shapes,first,y_position,x_position,which_rotation,actual_block,w,A)
                draw (matrix,rows,columns)
                pygame.display.update()
                    
        
        
            check=True
            
            #print (matrix)
            for i in range (0,4):
                if(y_position+i+1<rows):
                    for j in range (0,4):
                        if (actual_block[i][j]!=0):
                            if (actual_block[i+1][j]==0):
                                if (matrix[y_position+1+i][x_position+j]!=0):
                                    check=False
                                    break
                
                if(check==False):
                    
                    matrix,score,level=clearing_lanes(matrix,rows,columns,score,level,levels)
                    x_position=int(columns/2)
                    y_position=0
                    for i in range(0,4):
                        for j in range (0,4):
                            if (next_block[i][j]!=0):
                                if (matrix[y_position+i][x_position+j]!=0):
                                    game_overr()
                    next_piece=True
                    break
                
            if(check==True):
                for i in range (3,-1,-1):
                      if(y_position+i<rows):
                          for j in range (0,4):
                              if (actual_block[i][j]!=0):
                                  matrix[y_position+1+i][x_position+j]=actual_block[i][j]
                                  matrix[y_position+i][x_position+j]=0
                y_position+=1       
            
                pygame.time.delay(levels_clock[level])           
                draw (matrix,rows,columns)
                right_window(next_block,score,level,matrix)
                
                pygame.display.update()
                
        
               
####################################################
menu()
#game_loop()
####################################################
pygame.quit()