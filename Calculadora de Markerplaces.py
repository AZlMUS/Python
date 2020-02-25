import os
x=0
np=0
while x<1:
	print("Quanto tem que sobrar na mao?")
	preco=input()
	print(" ")
	resultado1=(float(preco)+5)/0.89 
	resultado2=(float(preco)+5)/0.84
	resultado3=(float(preco)+24)/0.89 
	resultado4=(float(preco)+24)/0.84
	resultado5=(float(preco)/0.80)
	resultado6=(float(preco)/0.74)
	resultado7=(float(preco)/0.71)
	np=np+1	
	print("Produto Numero: "+str(np)+" '"+str(preco)+"$'")
	print(" ")
	if resultado1<120:
		print("-----------------------------------------------")
		print("ML Classico: "+str(resultado1))
		print("-----------------------------------------------")
	if resultado2<120:
		print("ML Premium: "+str(resultado2))
		print("-----------------------------------------------")
	if resultado1>120:
		print("Classico: "+str(resultado3))
		print("-----------------------------------------------")
	if resultado2>=120:
		print("Premium: "+str(resultado4))
		print("-----------------------------------------------")

	print("Na B2W: "+str(resultado5))
	print("-----------------------------------------------")
	print("Na Olist assessorada: "+str(resultado6))
	print("-----------------------------------------------")
	print("Na Olist NAO assessorada: "+str(resultado7))
	print("-----------------------------------------------")
	print(" ")
	print(" ")

	os.system("break")


 