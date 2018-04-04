import pygame , sys , glob
pygame.init()

#contact email : emprexx42@gmail.com

#Couleurs

black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)

#Fenêtre

fen = pygame.display.set_mode ((602,598))
screenWidth=602

pygame.display.set_caption("BombermanMTM")

walkRight =  [pygame.image.load('right1.png'), pygame.image.load('right2.png'), pygame.image.load('right3.png')
            , pygame.image.load('right4.png'), pygame.image.load('right5.png'), pygame.image.load('right6.png'),
              pygame.image.load('right7.png'), pygame.image.load('right8.png'), pygame.image.load('right9.png')]

walkLeft = [pygame.image.load('left1.png'), pygame.image.load('left2.png'), pygame.image.load('left3.png'),
            pygame.image.load('left4.png'), pygame.image.load('left5.png') , pygame.image.load('left6.png'),
            pygame.image.load('left7.png'), pygame.image.load('left8.png'), pygame.image.load('left9.png')]

walkUp = [pygame.image.load('up1.png'), pygame.image.load('up2.png'), pygame.image.load('up3.png'),
          pygame.image.load('up4.png'), pygame.image.load('up5.png'), pygame.image.load('up6.png'),
          pygame.image.load('up7.png'), pygame.image.load('up8.png'), pygame.image.load('up9.png')]

walkDown = [pygame.image.load('down1.png'), pygame.image.load('down2.png'), pygame.image.load('down3.png')
            , pygame.image.load('down4.png'), pygame.image.load('down5.png'), pygame.image.load('down6.png'),
            pygame.image.load('down7.png'), pygame.image.load('down8.png'), pygame.image.load('down9.png')]


bg = pygame.image.load('bg_resized2.png')

char = pygame.image.load('standing.png')

clock= pygame.time.Clock()

#Notre personnage

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7
        self.walkCount = 0
        self.left = False
        self.right = False
        self.down = False
        self.up = False
    def draw(self, fen):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if self.up:
            fen.blit(walkUp [self.walkCount//3] ,(self.x,self.y))
            self.walkCount +=1

        elif self.left:
            fen.blit(walkLeft [self.walkCount//3] ,(self.x,self.y))
            self.walkCount += 1

        elif self.right:
            fen.blit(walkRight [self.walkCount//3] ,(self.x,self.y))
            self.walkCount +=1

        elif self.down:
            fen.blit(walkDown [self.walkCount//3 ],(self.x,self.y))
            self.walkCount +=1

        else:
            fen.blit(char,(self.x,self.y))

class bombe(object):
    def __init__(self,x,y,radius,color,timer):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.timer = timer
        self.vel = 8
    def draw(self,fen):
        pygame.draw.circle(fen,self.color,(self.x,self.y),self.radius)
    
def redrawGame():
    
    fen.blit(bg,(0,0))
    bomberman.draw( fen)
    for bullet in bullets:
        bullet.draw(fen)
    pygame.display.update()

#Loop

bomberman =player(0,0,64,64)
bullets = [ ]
run= True
while run:
    clock.tick(27)
    
    for event in pygame.event.get():
        if event .type== pygame.QUIT:
            run= False
    for bullet in bullets:
        if bullet.x < 602 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))
            
    keys = pygame.key.get_pressed()
     
    if keys [pygame.K_LEFT] and bomberman.x > bomberman.vel:
         bomberman.x -= bomberman.vel
         bomberman.left = True
         bomberman.right = False

    elif keys [pygame.K_SPACE]:
        if len (bullets)< 3:
            bullets.append(bombe(round(bomberman.x + bomberman.width //2), round(bomberman.y + bomberman.height//2), 13, black, 5))
            
    elif keys [pygame.K_RIGHT] and bomberman.x < screenWidth - bomberman.width - bomberman.vel:
          bomberman.x += bomberman.vel
          bomberman.right = True
          bomberman.left = False

    elif keys [pygame.K_UP] and bomberman.y > bomberman.vel :
          bomberman.y -= bomberman.vel
          bomberman.up= True

    elif keys [pygame.K_DOWN] and bomberman.y < screenWidth - bomberman.height - bomberman.vel:
          bomberman.y += bomberman.vel
          bomberman.down = True

    elif keys [pygame.K_ESCAPE]:
        pygame.quit()

    else:
        bomberman.right = False
        bomberman.left = False
        bomberman.up = False
        bomberman.down = False
        bomberman.walkCount = 0
        

    redrawGame()



pygame.quit()
