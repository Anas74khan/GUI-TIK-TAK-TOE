
import pygame
import time
import random


pygame.init()

screen= pygame.display.Info()
#setting game display
dw=screen.current_w
dh=screen.current_h
gameDisplay = pygame.display.set_mode((dw,dh))
pygame.display.set_caption('Tik Tak Toe')

#background colors and images
green= (0,255,0)
blue = (0,0,128)
black = (0,0,0)
white = (255,255,255)
bg = pygame.image.load('assets/sprites/background.jpeg')
bg = pygame.transform.scale(bg,(dw,dh))
board = pygame.image.load('assets/sprites/board.png')
zero = pygame.image.load('assets/sprites/zero.png')
cross = pygame.image.load('assets/sprites/cross.png')
board_bg = pygame.image.load('assets/sprites/board_bg.png')
board_bg = pygame.transform.scale(board_bg,(dw,((2*(dh//5))+(dh//100))))
won = pygame.image.load('assets/sprites/won.png')
won = pygame.transform.scale(won,(dw,(dh//2)+(dh//17)))
lost = pygame.image.load('assets/sprites/lost.png')
lost = pygame.transform.scale(lost,(dw,(dh//2)+(dh//17)))
tie = pygame.image.load('assets/sprites/tie.png')
tie = pygame.transform.scale(tie,(dw,(dh//2)+(dh//17)))
logo = pygame.image.load('assets/sprites/logo.png')
logo = pygame.transform.scale(logo,((dw-(dw//25)),dh//8))
play = pygame.image.load('assets/sprites/play.png')
play = pygame.transform.scale(play,(dw//3,dh//23))
exit = pygame.image.load('assets/sprites/exit.png')
exit = pygame.transform.scale(exit,(dw//3,dh//23))
reset = pygame.image.load('assets/sprites/reset.png')
reset = pygame.transform.scale(reset,(dw//4,dh//32))
quit = pygame.image.load('assets/sprites/quit_1.png')
quit = pygame.transform.scale(quit,(dw//4,dh//32))
restart = pygame.image.load('assets/sprites/restart.png')
restart =pygame.transform.scale(restart,(dw//8,dh//20))
quit_1 = pygame.image.load('assets/sprites/quit.png')
quit_1 =pygame.transform.scale(quit_1,(dw//8,dh//20))


#variables and objects used
clock = pygame.time.Clock()
crashed = False


#checking if element exist or not
def isAvailable(v):
	if b[v]==' ':
		return True
	return False

#Entering value
def enterVal(img,v):
		if img==zero:
			gameDisplay.blit(img,(placex[v]+15,placey[v]+15))
			b[v]='O'
		if img==cross:
			gameDisplay.blit(img,(placex[v],placey[v]+10))
			b[v]='X'

#Board is full
def isFull():
		for i in b:
			if i==' ':
				return False
		return True
		
#Winner
def isWinner(y):
    if((b[0]==y)and(b[0]==b[1]) and(b[1]==b[2])):
        return True
    if((b[3]==y)and(b[3]==b[4]) and(b[4]==b[5])):
        return True
    if((b[6]==y)and(b[6]==b[7]) and(b[7]==b[8])):
        return True
    if((b[0]==y)and(b[0]==b[3]) and(b[3]==b[6])):
        return True
    if((b[1]==y)and(b[1]==b[4]) and(b[4]==b[7])):
        return True
    if((b[2]==y)and(b[2]==b[5]) and(b[5]==b[8])):
        return True
    if((b[0]==y)and(b[0]==b[4]) and(b[4]==b[8])):
        return True
    if((b[2]==y)and(b[2]==b[4]) and(b[4]==b[6])):
        return True
    return False

#computer move
def compmove(x,uv):
    true=True
    for i in range(0,9,3):
        if(b[i]==x and b[i+1]==b[i] and b[i+2]==' ' and true==True):
            b[i+2]=x
            return (i+2)
        elif(b[i+1]==x and b[i+1]==b[i+2] and b[i]==' ' and true==True):
            b[i]=x
            return(i)
        elif(b[i]==x and b[i]==b[i+2] and b[i+1]==' ' and true==True):
            b[i+1]=x
            return(i+1)
    for i in range(3):
        if(b[i]==x and b[i+3]==b[i] and b[i+6]==' ' and true==True):
            b[i+6]=x
            return(i+6)
        elif(b[i+3]==x and b[i+3]==b[i+6] and b[i]==' ' and true==True):
            b[i]=x
            return(i)
        elif(b[i]==x and b[i]==b[i+6] and b[i+3]==' ' and true==True):
            b[i+3]=x
            return(i+3)
    if(b[0]==x and b[4]==b[0] and b[8]==' ' and true==True):
        b[8]=x
        return(8)
    elif(b[4]==x and b[4]==b[8] and b[0]==' ' and true==True):
        b[0]=x
        return(0)
    elif(b[0]==x and b[0]==b[8] and b[4]==' ' and true==True):
        b[4]=x
        return(4)
    elif(b[2]==x and b[4]==b[2] and b[6]==' ' and true==True):
        b[6]=x
        return(6)
    elif(b[4]==x and b[4]==b[6] and b[2]==' ' and true==True):
        b[2]=x
        return(2)
    elif(b[2]==x and b[2]==b[6] and b[4]==' ' and true==True):
        b[4]=x
        return(4)
    for i in range(0,9,3):
        if(b[i]==uv and b[i+1]==b[i] and b[i+2]==' ' and true==True):
            b[i+2]=x
            return(i+2)
        elif(b[i+1]==uv and b[i+1]==b[i+2] and b[i]==' ' and true==True):
            b[i]=x
            return(i)
        elif(b[i]==uv and b[i]==b[i+2] and b[i+1]==' ' and true==True):
            b[i+1]=x
            return(i+1)
    for i in range(3):
        if(b[i]==uv and b[i+3]==b[i] and b[i+6]==' ' and true==True):
            b[i+6]=x
            return(i+6)
        elif(b[i+3]==uv and b[i+3]==b[i+6] and b[i]==' ' and true==True):
            b[i]=x
            return(i)
        elif(b[i]==uv and b[i]==b[i+6] and b[i+3]==' ' and true==True):
            b[i+3]=x
            return(i+3)
    if(b[0]==uv and b[4]==b[0] and b[8]==' ' and true==True):
        b[8]=x
        return(8)
    elif(b[4]==uv and b[4]==b[8] and b[0]==' ' and true==True):
        b[0]=x
        return(0)
    elif(b[0]==uv and b[0]==b[8] and b[4]==' ' and true==True):
        b[4]=x
        return(4)
    elif(b[2]==uv and b[4]==b[2] and b[6]==' ' and true==True):
        b[6]=x
        return(6)
    elif(b[4]==uv and b[4]==b[6] and b[2]==' ' and true==True):
        b[2]=x
        return(2)
    elif(b[2]!=uv and b[2]==b[6] and b[4]==' ' and true==True):
        b[4]=x
        return(4)
    elif(true==True):
        m=[]
        n=[]
        for i in range(9):
        	if b[i]==' ':
        		if(i==0 or i==2 or i==6 or i==8):
        			n.append(i)
        		else:
        			m.append(i)
        if 4 in set(m):
                b[4]=x
                return(4)
        elif(b[0]==b[8] and b[0]==uv):
        	i=random.choice(m)
        	b[i]=x
        	return(i)
        elif(len(n)>0):
        	i= random.choice(n)
        	b[i]=x
        	return(i)
        else:
                i=random.choice(m)
                b[i]=x
                return(i)


def displayBoard(x,y):
    gameDisplay.blit(board_bg,(0,((dh//3)-(dh//100))))
    gameDisplay.blit(board, (x,y))
    
#Board description don't interfare with this code'
x =  ((dw - board.get_width())/2)
y = ((dh - board.get_height())/2)
w=int(board.get_width()/3)
h=int(board.get_height()/3)
area = {
				0 : pygame.Rect(x,y,w,h),
				1 : pygame.Rect((x+w),y,w,h),
				2 : pygame.Rect((x+(2*w)),y,w,h),
				3 : pygame.Rect(x,(y+h),w,h),
				4 : pygame.Rect((x+w),(y+h),w,h),
				5 : pygame.Rect((x+(2*w)),(y+h),w,h),
				6 : pygame.Rect(x,(y+(2*h)),w,h),
				7 : pygame.Rect((x+w),(y+(2*h)),w,h),
				8 : pygame.Rect((x+(2*w)),(y+(2*h)),w,h)
}
				
placex=[x,(x+w),(x+(2*w)),x,(x+w),(x+(2*w)),x,(x+w),(x+(2*w))]

placey=[y,y,y,(y+h),(y+h),(y+h),(y+(2*h)),(y+(2*h)),(y+(2*h))]
				



#Home Screen
gameDisplay.blit(bg,(0,0))
gameDisplay.blit(logo,(dw//50,dh//9))
gameDisplay.blit(play,(dw//11,((dh//2)+35)))
gameDisplay.blit(exit,((dw//2+(dw//11)),((dh//2)+35)))
ar={
			'play' : pygame.Rect(dw//11,((dh//2)+35),dw//3,dh//23),
			'exit' : pygame.Rect((dw//2+(dw//11)),((dh//2)+35),dw//3,dh//23),
			'reset' : pygame.Rect(dw//6,((dh//2)+(dh//6)),dw//4,dh//32),
			'quit' : pygame.Rect(((dw-(dw//6))-dw//4),((dh//2)+(dh//6)),dw//4,dh//32),
			'restart' : pygame.Rect(dw//4,dh-(2*(dh//5)),dw//8,dh//20),
			'quit_1' : pygame.Rect((dw-(dw//3)),dh-(2*(dh//5)),dw//8,dh//20)
}
q=False
crash=False
while not crash:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			crashed= True
		elif event.type == pygame.MOUSEBUTTONDOWN:
	                if event.button == 1:
	                	if ar['play'].collidepoint(event.pos):
	                		crash= True
	                	elif ar['exit'].collidepoint(event.pos):
	                		crash= True
	                		crashed= True
	                		q=True
	pygame.display.update()
	



gameDisplay.fill(black)
#Game screen
while not q:
	res=False
	crashed=False
	status=''
	b = [' ' for i in range(9)]
	gameDisplay.blit(bg,(0,0))
	gameDisplay.blit(logo,(dw//50,dh//9))
	displayBoard(x,y)
	gameDisplay.blit(reset,(dw//6,((dh//2)+(dh//6))))
	gameDisplay.blit(quit,(((dw-(dw//6))-dw//4),((dh//2)+(dh//6))))
	img= cross
	d='X'
	while not crashed:
		if d=='X':
		    for event in pygame.event.get():
		        if event.type == pygame.QUIT:
		            crashed = True
		            q= True
		        elif event.type == pygame.MOUSEBUTTONDOWN:
		                if event.button == 1:
		                	for i in range(9):
		                		if area[i].collidepoint(event.pos):
		                			if isAvailable(i):
		                				enterVal(img,i)
		                				if(isWinner(d)):
		                					status='won'
		                					crashed=True
		                				img=zero
		                				d='O'
		                	if ar['quit'].collidepoint(event.pos):
		                		crashed=True
		                		q=True
		                	if ar['reset'].collidepoint(event.pos):
		                		crashed=True
		                		img = cross
		                		res=True
		                		d = 'X'
		    pygame.display.update()
		else:
		   i=compmove('O','X')
		   time.sleep(0.1)
		   enterVal(img,i)
		   if(isWinner(d)):
		   	status='lost'
		   	crashed = True
		   img=cross
		   d='X'
		if(isFull()):
		   	status='tie'
		   	crashed=True
		pygame.display.update()
	while(crashed and (not q)and (not res)):
		    if status=='won':
		    	gameDisplay.blit(won,(0,(dh//4)+(dh//90)))
		    elif status=='lost':
		    	gameDisplay.blit(lost,(0,(dh//4)+(dh//90)))
		    elif status=='tie':
		    	gameDisplay.blit(tie,(0,(dh//4)+(dh//90)))
		    gameDisplay.blit(restart,(dw//4,dh-(2*(dh//5))))
		    gameDisplay.blit(quit_1,((dw-(dw//3)),dh-(2*(dh//5))))
		    for event in pygame.event.get():
		        if event.type == pygame.QUIT:
		            crashed = True
		            q= True
		        elif event.type == pygame.MOUSEBUTTONDOWN:
		                if event.button == 1:
		                	if ar['restart'].collidepoint(event.pos):
		                		crashed=False
		                	elif ar['quit_1'].collidepoint(event.pos):
		                		crashed= True
		                		q=True
		        pygame.display.update()
	if(q== True):
			pygame.quit()
	