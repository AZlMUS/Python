import os
x=0
np=0
while x<1:
	print("Quanto vale o produto no anuncio?")
	preco=input()
	pct11 =float(preco)*0.11 
	pct16 =float(preco)*0.16 
	pct20 =float(preco)*0.20 
	print(" ")
	resultado1=(float(preco)-pct11)-5
	resultado2=(float(preco)-pct16)-5
	resultado3=(float(preco)-pct11)-24
	resultado4=(float(preco)-pct16)-24
	resultado5=(float(preco)-pct20)
	np=np+1	
	print("Produto Numero: "+str(np)+" '"+str(preco)+"$'")
	print(" ")
	if resultado1<120:
		print("-------------------------------")
		print("O preco deveria ser no ML Classico: "+str(resultado1))
		print("-----------------------------------")
	if resultado2<120:
		print("O preco deveria ser no ML Premium: "+str(resultado2))
		print("-----------------------------------")
	if resultado1>120:
		print("O preco deveria ser no ML Classico: "+str(resultado3))
		print("-----------------------------------")
	if resultado2>=120:
		print("O preco deveria ser no ML Premium: "+str(resultado4))
		print("-----------------------------------")

	print("Na B2W: "+str(resultado5))
	print("-------------------------------")
	print(" ")
	print(" ")
	os.system("break")


 