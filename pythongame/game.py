/*
 * python-game
 * author:Yufeng Fan 1102194283@qq.com
 * ‎2016‎年‎4‎月‎24日 下午11：18：47
*/

import pygame
import math
import random

from pygame.locals import *

keys=[False,False,False,False]
playerpos=[400,50]
acc=[0,0]
arrows=[]
badtimer=100
badtimer1=0
badguys=[[640,100]]
healthvalue=194

pygame.init()
width,height=960,640
screen=pygame.display.set_mode((width,height))
player=pygame.image.load("resources/images/tupian/tuzi.png")
grass=pygame.image.load("resources/images/tupian/cao.png")
castle=pygame.image.load("resources/images/tupian/2.png")
arrow=pygame.image.load("resources/images/tupian/bullet.png")
badguying1=pygame.image.load("resources/images/tupian/bullet.png")
badguying =badguying1


while(1):
	badtimer-=1
	screen.fill(0)
	for x in range(width/grass.get_width()+1):
		for y in range(height/grass.get_height()+1):
			screen.blit(grass,(x*50,y*50))
	screen.blit(castle,(0,50))	
	screen.blit(castle,(0,150))	
	screen.blit(castle,(0,250))
	screen.blit(castle,(0,350))
	for bullet in arrows:
		index=0
		velx=math.cos(bullet[0])*10
		vely=math.sin(bullet[0])*10
		bullet[1]+=velx
		bullet[2]+=vely
		if bullet[1]<-64 or bullet[1]>640 or bullet[2]<-64 or bullet[2]>480:
			arrows.pop(index)
		index +=1
		for projectile in arrows:
			arrow1=pygame.transform.rotate(arrow,360-projectile[0]*57.29)
			screen.blit(arrow1,(projectile[1],projectile[2]))

#	screen.blit(player,playerpos)
	
	position=pygame.mouse.get_pos()
	angle=math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
	playerrot=pygame.transform.rotate(player,360-angle*57.29)
	playerpos1=(playerpos[0]-playerrot.get_rect().width/2,playerpos[1]-playerrot.get_rect().height/2)
	screen.blit(playerrot,playerpos1)
	


	
	if badtimer==0:
		badguys.append([640,random.randint(50,430)])
		badtimer=100-(badtimer1*2)
		if badtimer1>=35:
			badtimer1=35
		else:
			badtimer1+=5
	index=0
	for badguy in badguys:
		if badguy[0]<-64:
			badguys.pop(index)
		badguy[0]-=7
		badrect =pygame.Rect(badguying.get_rect())
		badrect.top=badguy[1]
		badrect.left=badguy[0]
		if badrect.left<64:
			healthvalue-=random.randint(5,20)
			badguys.pop(index)
		index1=0
		for bullet in arrows:
			bullrect=pygame.Rect(arrow.get_rect())
			bullrect.left=bullet[1]
			bullrect.top=bullet[2]
		
			if badrect.colliderect(bullrect):
				acc[0]+=1
				badguys.pop(index)
				arrows.pop(index1)
		index1+=1
		index +=1
	for badguy in badguys:
		screen.blit(badguying,badguy)
	

	pygame.display.flip()
	
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
		if event.type==pygame.KEYDOWN:
			if event.key==K_w:
				keys[0]=True
			elif event.key==K_a:
				keys[1]=True
			elif event.key==K_s:
				keys[2]=True
			elif event.key==K_d:
				keys[3]=True	
		if event.type==pygame.KEYUP:
			if event.key==K_w:
				keys[0]=False
			elif event.key==K_a:
				keys[1]=False
			elif event.key==K_s:
				keys[2]=False
			elif event.key==K_d:
				keys[3]=False
		if event.type==pygame.MOUSEBUTTONDOWN:
			position=pygame.mouse.get_pos()
			acc[1]+=1
			arrows.append([math.atan2(position[1]-(playerpos1[1]+32),position[0]-(playerpos1[0]+26)),playerpos1[0]+32,playerpos1[1]+32])					
	if keys[0]:
		playerpos[1]-=5
	elif keys[2]:
		playerpos[1]+=5
	if keys[1]:
		playerpos[0]-=5
	elif keys[3]:
		playerpos[0]+=5	

			
	#exit(0)
