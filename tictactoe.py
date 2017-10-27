#http://www.python-course.eu/tkinter_layout_management.php
#!usr/bin/python
import os
import time
import sys    
import termios
import fcntl
#import msvcrt
A = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
U = 'X'
I = 'O'
a = '0'

def getch():
  fd = sys.stdin.fileno()

  oldterm = termios.tcgetattr(fd)
  newattr = termios.tcgetattr(fd)
  newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
  termios.tcsetattr(fd, termios.TCSANOW, newattr)

  oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
  fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

  try:        
    while 1:            
      try:
        c = sys.stdin.read(1)
        break
      except IOError: pass
  finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
  return c


def Validate(z) :
	try :
		l = int(z)
		if  not(l>=1 and l<=9) :
			return 0
	except :
		return 0
	
	if    (z=='1') : 
		if  A[0][0]!=' ' : return 0
	elif (z=='2') :  
		if  A[0][1]!=' ' : return 0
	elif (z=='3') :  
		if  A[0][2]!=' ' : return 0
	elif (z=='4') :  
		if  A[1][0]!=' ' : return 0
	elif (z=='5') :  
		if  A[1][1]!=' ' : return 0
	elif (z=='6') :  
		if  A[1][2]!=' ' : return 0
	elif (z=='7') :  
		if  A[2][0]!=' ' : return 0
	elif (z=='8') :  
		if  A[2][1]!=' ' : return 0
	elif (z=='9') :  
		if  A[2][2]!=' ' : return 0
	else : return 1
def check() :

	if ( (A[0][0] == A[1][1]  and A[0][0] == A[2][2] and A[2][2] == U) or (A[0][2] == A[1][1] and A[0][2] == A[2][0] and A[2][0] == U) ) :
		return 1	
	
	for i in range(3) :
		if(( A[i][0] == A[i][1] and A[i][0] == A[i][2] and A[i][2] == U) or (A[0][i] == A[1][i] and A[0][i] == A[2][i] and A[2][i] == U)) :
			return 1

def Allocate( a , b ) :

	if    (a=='1') : A[0][0]=b
	elif (a=='2') : A[0][1]=b
	elif (a=='3') : A[0][2]=b
	elif (a=='4') : A[1][0]=b
	elif (a=='5') : A[1][1]=b
	elif (a=='6') : A[1][2]=b
	elif (a=='7') : A[2][0]=b
	elif (a=='8') : A[2][1]=b
	elif (a=='9') : A[2][2]=b			

def ComputerTurn(M) :

	if A[0][0] == M and A[1][1] == M and A[2][2] == ' ' :
		A[2][2] = I
		return 1 
	elif A[1][1] == M and A[2][2] == M and A[0][0] == ' ' :
		A[0][0] = I
		return 1
	elif A[0][0] == M and A[2][2] == M and A[1][1] == ' ' :
		A[1][1] = I
		return 1
	elif A[0][2] == M and A[1][1] == M and A[2][0] == ' ' :
		A[2][0] = I
		return 1
	elif A[1][1] == M and A[2][0] == M and A[0][2] == ' ' :
		A[0][2] = I
		return 1
	elif A[2][0] == M and A[0][2] == M and A[1][1] == ' ' :
		A[1][1] = I
		return 1
	for i in range(3) :
		if A[i][0] == M and A[i][1] == M and A[i][2] == ' ' :
			A[i][2] = I
			return 1
		elif A[i][1] == M and A[i][2] == M and A[i][0] == ' ' :
			A[i][0] = I
			return 1
		elif A[i][2] == M and A[i][0] == M and A[i][1] == ' ' :
			A[i][1] = I
			return 1
		elif A[0][i] == M and A[1][i] == M and A[2][i] == ' ' :
			A[2][i] = I
			return 1
		elif A[1][i] == M and A[2][i] == M and A[0][i] == ' ' :
			A[0][i] = I
			return 1
		elif A[2][i] == M and A[0][i] == M and A[1][i] == ' ' :
			A[1][i] = I
			return 1

	if ( A[0][0] == M and A[0][1] == M ) or ( A[0][1] == M and A[0][2] == M ) or ( A[0][2] == M and A[1][2] == M ) or ( A[1][2] == M and A[2][2] == M ) or ( A[2][2] == M and A[2][1] == M ) or ( A[2][1] == M and A[2][0] == M ) or ( A[2][0] == M and A[1][0] == M ) or ( A[1][0] == M and A[0][0] == M ) or ( A[0][0] == M and A[0][2] == M) or ( A[0][2] == M and A[2][2] == M) or ( A[2][2] == M and A[2][0] == M) or ( A[2][0] == M and A[0][0] == M) or ( A[0][1] == M and A[1][2] == M) or ( A[1][2] == M and A[2][1] == M) or ( A[2][1] == M and A[1][0] == M) or ( A[1][0] == M and A[0][1] == M):
		if ( A[1][1] == ' ' ) :
			A[1][1] = I
			return 1
	return 0			

def ComputerTurns() :
	for i in range(3) :
		for  j in range(3) :
			if A[i][j] == ' ' :
				A[i][j] = I
				return
				


count = 0
os.system('clear')
print 'TIC TAC TOE GAME \n'
print '- - - - - - -'
print '|' + ' ' + '1' + ' ' + '|' + ' ' + '2' + ' ' + '|' + ' ' + '3' + ' ' + '|'
print '- - - - - - -'
print '|' + ' ' + '4' + ' ' + '|' + ' ' + '5' + ' ' + '|' + ' ' + '6' + ' ' + '|'
print '- - - - - - -'
print '|' + ' ' + '7' + ' ' + '|' + ' ' + '8' + ' ' + '|' + ' ' + '9' + ' ' + '|'
print '- - - - - - -'
print '\n'
print '- - - - - - -'
print '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|'
print '- - - - - - -'
print '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|'
print '- - - - - - -'
print '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|' + ' ' + ' ' + ' ' + '|'
print '- - - - - - -'

#print   " X or O ? "
#type = raw_input()
#if type == 'X' :
#else :
#U = 'O'
#I = 'X'

print "Yours is X"
U = 'X'
I = 'O'

while (2>1) :
	
	print "Its your turn Enter a number :"
#	a = msvcrt.getch()
	a = getch()
	y = Validate(a)
	
	if y == 0 :
		os.system('clear')
		print 'TIC TAC TOE GAME \n'
		print '- - - - - - -'
		print '|' + ' ' + '1' + ' ' + '|' + ' ' + '2' + ' ' + '|' + ' ' + '3' + ' ' + '|'
		print '- - - - - - -'
		print '|' + ' ' + '4' + ' ' + '|' + ' ' + '5' + ' ' + '|' + ' ' + '6' + ' ' + '|'
		print '- - - - - - -'
		print '|' + ' ' + '7' + ' ' + '|' + ' ' + '8' + ' ' + '|' + ' ' + '9' + ' ' + '|'
		print '- - - - - - -'	
		print '\n'
		print '- - - - - - -'
		for i in A :
			print '|' + ' ' + i[0] + ' ' + '|' + ' ' + i[1] + ' ' + '|' + ' ' + i[2] + ' ' + '|'
			print '- - - - - - -'
		continue
	Allocate( a , U )
	os.system('clear')
	print 'TIC TAC TOE GAME \n'
	print '- - - - - - -'
	print '|' + ' ' + '1' + ' ' + '|' + ' ' + '2' + ' ' + '|' + ' ' + '3' + ' ' + '|'
	print '- - - - - - -'
	print '|' + ' ' + '4' + ' ' + '|' + ' ' + '5' + ' ' + '|' + ' ' + '6' + ' ' + '|'
	print '- - - - - - -'
	print '|' + ' ' + '7' + ' ' + '|' + ' ' + '8' + ' ' + '|' + ' ' + '9' + ' ' + '|'
	print '- - - - - - -'
	print '\n'
	print '- - - - - - -'
	for i in A :
		print '|' + ' ' + i[0] + ' ' + '|' + ' ' + i[1] + ' ' + '|' + ' ' + i[2] + ' ' + '|'
		print '- - - - - - -'
	print "Its Computer's turn"
	time.sleep(1)
	os.system('clear')
#	clear
	
	k = check()
	if k==1 :
		output =  " You won ! "
		break	
	
	k = ComputerTurn(I)
	if k==1 :
		output = "You lose"
		break
	k1 = ComputerTurn(U)
	if k==0 and k1==0 :
		ComputerTurns()	
	
	if count == 4 :
		output =  "The game is draw"
		break
#	print '\n'
	print 'TIC TAC TOE GAME \n'
	print '- - - - - - -'
	print '|' + ' ' + '1' + ' ' + '|' + ' ' + '2' + ' ' + '|' + ' ' + '3' + ' ' + '|'
	print '- - - - - - -'
	print '|' + ' ' + '4' + ' ' + '|' + ' ' + '5' + ' ' + '|' + ' ' + '6' + ' ' + '|'
	print '- - - - - - -'
	print '|' + ' ' + '7' + ' ' + '|' + ' ' + '8' + ' ' + '|' + ' ' + '9' + ' ' + '|'
	print '- - - - - - -'	
	print '\n'
	print '- - - - - - -'
	for i in A :
		print '|' + ' ' + i[0] + ' ' + '|' + ' ' + i[1] + ' ' + '|' + ' ' + i[2] + ' ' + '|'
		print '- - - - - - -'	
	
	
	count = count + 1
#print '\n'
print 'TIC TAC TOE GAME \n'
print '- - - - - - -'
print '|' + ' ' + '1' + ' ' + '|' + ' ' + '2' + ' ' + '|' + ' ' + '3' + ' ' + '|'
print '- - - - - - -'
print '|' + ' ' + '4' + ' ' + '|' + ' ' + '5' + ' ' + '|' + ' ' + '6' + ' ' + '|'
print '- - - - - - -'
print '|' + ' ' + '7' + ' ' + '|' + ' ' + '8' + ' ' + '|' + ' ' + '9' + ' ' + '|'
print '- - - - - - -'
print '\n'
print '- - - - - - -'
for i in A :
	print '|' + ' ' + i[0] + ' ' + '|' + ' ' + i[1] + ' ' + '|' + ' ' + i[2] + ' ' + '|'
	print '- - - - - - -'
print output
