import pygame
import math
import random
import decimal

pygame.init()
width=800
height=400
green=(0,255,0)
black=(0,0,0)
screen=pygame.display.set_mode((width,height))
loop=True

font=pygame.font.Font('freesansbold.ttf',32)
text=font.render('GAME OVER',True,green,black)
textRect=text.get_rect()
textRect.center=(width//2,height//2)

score=0

a=0

code_hub_=pygame.image.load('icon.png')

player_img=pygame.image.load('ship.png')
playerx=400
playery=350
player_change=0
speed=[0.01,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5]
alien_img=[]
alienx=[]
alieny=[]
num_of_aliens=10
alienx_change=[]
alieny_change=[]
for i in range(num_of_aliens):
	alien_img.append(pygame.image.load('alien.png'))	
	alienx.append(random.randint(32,750))	
	alieny.append(random.randint(0,200))	
	alienx_change.append(random.choice(speed))	
	alieny_change.append(40)


	
bullet_img=pygame.image.load('bullet.png')
bulletx=playerx
bullety=playery
bullety_change=-0.5
bullet_fired=False

def player(x,y):
	screen.blit(player_img,(x,y))

def alien(x,y,i):
	screen.blit(alien_img[i],(x,y))

def bullet(x,y):
	bulletx=playerx
	bullety=playery
	screen.blit(bullet_img,(x,y))

def collision(x,y,w,z):
	distance=math.sqrt(math.pow((x-y),2)+math.pow((w-z),2))
	if distance<27:
		return True	
def gameover(x,y,w,z):
	distance=math.sqrt(math.pow((x-y),2)+math.pow((w-z),2))
	if distance<27:
		return True	



while loop:
	screen.fill((0,0,0))
	screen.blit(code_hub_,(725,0))
	
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			loop=False
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				player_change=-0.4
			elif event.key==pygame.K_RIGHT:
				player_change=0.4
			if event.key==pygame.K_SPACE:
				bullet_fired=True	
		if event.type==pygame.KEYUP:
			if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
				player_change=0		
	playerx+=player_change
	if bullet_fired==False:
		bulletx=playerx
	if playerx<0:
		playerx=0
		player_change=0
	elif playerx>768:
		playerx=768
		player_change=0


	for i in range(num_of_aliens):
		alienx[i]+= alienx_change[i]
		if alienx[i]<0:
			alienx[i]=0
			alienx_change[i]=+0.2
			alieny[i]+=alieny_change[i]
		elif alienx[i]>768:
			alienx[i]=768
			alienx_change[i]=-0.2
			alieny[i]+=alieny_change[i]

		if collision(bulletx,alienx[i],bullety,alieny[i]) and bullety<350:
			score+=1
			bulletx=playerx
			bullety=playery
			bullet_fired=False
			alienx[i]=random.randint(32,750)	
			alieny[i]=random.randint(0,200)
			print(score)
		
		alien(alienx[i],alieny[i],i)	
		if gameover(playerx,alienx[i],playery,alieny[i]):
			alienx[i]=random.randint(32,750)	
			alieny[i]=random.randint(0,200)
			a=1



	if a==1:
		screen.blit(text,textRect)		
	if bullet_fired:
		bullety+=bullety_change
	if bullety<0:
		bullety=playery
		bullet_fired=False
	
	bullet(bulletx,bullety)
	player(playerx,playery)
	
	
	
	pygame.display.update()		