factura={}
lista=[]
cobro=[]
lista1=[]
opcion=""
saldo=0

def consultar(clave):
	print("***CONSULTA DE USUARIO***")
	if factura.get(clave): 
		print("Usuario ",lista[0]," debe pagar :",lista[1])	
	elif len(factura)==0:
		print("Diccionario vacío no es posible localizar factura")
	else:
		print("La factura no se encuentra registrada")	
	return

def listado():
	if len(factura)==0:
		print("No existen registros")
	else:
		print("***REGISTROS DE FACTURACION***")
		for llave,lista in factura.items():
			print("Factura nro:"+str(llave)+" usuario :",lista[0]," vale ",lista[1])
	return

while opcion!="T":
	print("@@ MENU FACTURACION @@")
	print("Añadir(A):Pagar(P):Consultar(C):Listar(L):Totalizar($)--Terminar(T)")
	opcion=input("Digite opción:")
	if opcion=="A":
		lista=[]
		clave=int(input("Introduce el código de la factura: "))
		lista.append(input("Introduce el nombre del usuario: "))
		valor=(float(input("Introduce el coste de la factura: ")))
		lista.append(valor)
		lista1.append(valor)
		factura[clave]=lista
	elif opcion=="P":
		clave=int(input("Introduce el código de la factura a pagar: "))
		valor=factura.pop(clave,0)
		cobro.append(valor[1])
	elif opcion=="C":
		clave=int(input("Ingrese código a consultar factura :"))	
		consultar(clave)		
	elif opcion=="L":		
		listado()
	elif opcion=="$":
		print("***INFORMACION CONTABLE***")
		if len(factura)==0:
			print("No existen registros")
		gen=sum(lista1)
		cobrado=sum(cobro)		
		print("Total cobrado :",cobrado," Pendiente :",(gen-cobrado))
		cobro=[]		
	elif opcion=="T":
		print("Fin de la Aplicación")
		break