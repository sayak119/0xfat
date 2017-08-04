w=input()
s=0
for i in range(len(w)):
	if w[i]>='0' and w[i]<='9':
		s=s+int(w[i])
	elif w[i]=='a':
		s=s+2*2
	elif w[i]=='b':
		s=s+2*3
	elif w[i]=='c': 
                s=s+2*4

	elif w[i]=='d': 
	        s=s+3*2
	elif w[i]=='e': 
	        s=s+3*3
	elif w[i]=='f':
	        s=s+3*4

	elif w[i]=='g': 
	        s=s+4*2
	elif w[i]=='h': 
	        s=s+4*3
	elif w[i]=='i':
	        s=s+4*4

	elif w[i]=='j': 
	        s=s+5*2
	elif w[i]=='k': 
	        s=s+5*3
	elif w[i]=='l':
	        s=s+5*4

	elif w[i]=='m': 
	        s=s+6*2
	elif w[i]=='n': 
	        s=s+6*3
	elif w[i]=='o':
	        s=s+6*4
	
	elif w[i]=='p': 
	        s=s+7*2
	elif w[i]=='q': 
	        s=s+7*3
	elif w[i]=='r':
	        s=s+7*4
	elif w[i]=='s':
		s=s+7*5

	elif w[i]=='t': 
	        s=s+8*2
	elif w[i]=='u': 
	        s=s+8*3
	elif w[i]=='v':
	        s=s+8*4

	elif w[i]=='w': 
	        s=s+9*2
	elif w[i]=='x': 
	        s=s+9*3
	elif w[i]=='y':
	        s=s+9*4
	elif w[i]=='z':
		s=s+9*5
print(s)
