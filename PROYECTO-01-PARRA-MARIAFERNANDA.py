from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
#lista_administradores lista con listas, [usuario, contraseña]

administradores = [["Fernanda Parra", "contraseña12"], ["Juan Solis", "candado29"], ["Mario Dominguez", "luna3"], ["Andrea Garcia", "perrito2"], ["Luis Sanchez", "123456"], ["a","a"]]

#Aquí pido que pongan en el programa su usuario y contraseña
usuario = input("Ingresa tu usuario: ")
contraseña = input("Ingresa tu contraseña: ")

es_administrador = 0
intentos = 1

#si administrador es 1 e intentos es menor o igual a 2
while es_administrador !=1 and intentos<=2:
  for administrador in administradores: #busca el admin en la lista administradores
    if usuario==administrador[0] and contraseña==administrador[1]:
      print("Bienvenido") #imprime una vez ya lo encontro en la lista
      es_administrador=1
    
#si administrador es 0 y no está en la lista boto datos incorrectos y doy otra oportunidad hasta 3, de ahi lo comunica con el personal porque no existe el usuario
  if es_administrador == 0:
    print("Datos incorrectos")
    usuario=input("Ingresa el usuario: ")
    contraseña = input("Ingresa la contraseña: ")
    intentos += 1
    if intentos == 3: 
      print("Favor de contactar al personal")     

#Ya que si es admin doy menú de los productos
if es_administrador == 1:
  print ("Selecciona una opción: ")     
  print ("1) Mostrar productos más vendidos\n2) Mostrar productos rezagados\n3) Mostrar productos más buscados\n4) Mostrar productos menos buscados")
  opcion=int(input("Elija opción: "))
  if opcion==1: #si pido de mayor a menor
    contador=0
    ventas_producto=[] #nueva lista con las ventas de c/producto
    for producto in lifestore_products: 
      for venta in lifestore_sales: 
        if producto [0]==venta[1]:#checo las ventas que tiene cada producto
          contador +=1 #contabilizo las ventas de cada producto
      if contador !=0:
        ventas_producto.append([producto[0], producto[1], contador]) #añado a la lista vacía los productos unicamente con su id, nombre y las veces que se conto se han vendido
        contador=0
    productos_ordenados=[] #nueva lista ordenada
    while ventas_producto:
      maximo = ventas_producto[0][2] #ordeno por id y cantidad
      lista_max = ventas_producto[0]
      for totalventas in ventas_producto:
        if totalventas[2]>maximo: #Aqui estoy acomodando de mayor en menos acorde al indice 2, es decir, el contador
          maximo=totalventas[2]
          lista_max=totalventas
      productos_ordenados.append(lista_max) #a la nueva lista vacia de productos ordenados le añado la lista ya acomodada por ventas
      ventas_producto.remove(lista_max) #freno el codigo
    print(productos_ordenados)
  if opcion==2: #si pido de menor a mayor, dando a rezagados como aquellos que se venden menos
    contador=0
    productos_rezagados=[] #nueva lista con ventas de c/producto
    for producto in lifestore_products:
      for venta in lifestore_sales: 
        if producto [0]==venta[1]: #checo las ventas que tiene cada producto
          contador +=1 #las contabilizo
      if contador !=0:
        productos_rezagados.append([producto[0], producto[1], contador]) #añado a la lista vacía los productos unicamente con su id, nombre y las veces que se conto se han vendido
        contador=0
    rezagados_ordenados=[]
    while productos_rezagados: #nueva lista ordenada de menor a mayor
      minimo = productos_rezagados[0][2] #ordeno por id y cantidad
      lista_min = productos_rezagados[0] #los dejo unicamente el id en la nueva lista
      for rezagados in productos_rezagados:
        if rezagados[2]<minimo:#Aqui estoy acomodando de menor a mayor acorde al indice 2, es decir, el contador
          minimo=rezagados[2]
          lista_min=rezagados
      rezagados_ordenados.append(lista_min) #a la nueva lista vacia de productos rezagados le añado la lista ya acomodada por ventas de menor a mayor
      productos_rezagados.remove(lista_min) #freno el código
    print(rezagados_ordenados)
  if opcion==3: #si pido más buscados
    contador=0
    busqueda_producto=[] #nueva lista con las busquedas de c/producto
    for producto in lifestore_products: 
      for busqueda in lifestore_searches: 
        if producto [0]==busqueda[1]:#checo las busquedas que tiene cada producto
          contador +=1 #contabilizo las busquedas de cada producto
      if contador !=0:
        busqueda_producto.append([producto[0], producto[1], contador]) #añado a la lista vacía los productos unicamente con su id, nombre y las veces que se conto se han buscado
        contador=0
    cuantas_busquedas=[] #nueva lista ordenada de más a menos busquedas
    while busqueda_producto:
      mas = busqueda_producto[0][2] #ordeno por id y cantidad de busquedas
      lista_mas = busqueda_producto[0]
      for totalbusqueda in busqueda_producto:
        if totalbusqueda[2]>mas: #Aqui estoy acomodando de mayor a menor acorde al indice 2, es decir, el contador
          mas=totalbusqueda[2]
          lista_mas=totalbusqueda
      cuantas_busquedas.append(lista_mas) #a la nueva lista vacia de productos ordenados por busqueda le añado la lista ya acomodada por cantidad de veces buscadas
      busqueda_producto.remove(lista_mas) #freno el codigo
    print(cuantas_busquedas)
  if opcion==4: #si pido menos buscados
    contador=0
    impopular_producto=[] #nueva lista con las busquedas de c/producto
    for producto in lifestore_products: 
      for busqueda in lifestore_searches: 
        if producto [0]==busqueda[1]:#checo las busquedas que tiene cada producto
          contador +=1 #contabilizo las busquedas de cada producto
      if contador !=0:
        impopular_producto.append([producto[0], producto[1], contador]) #añado a la lista vacía los productos unicamente con su id, nombre y las veces que se conto se han buscado
        contador=0
    menos_busquedas=[] #nueva lista ordenada de menos a más busquedas
    while impopular_producto:
      menos = impopular_producto[0][2] #ordeno por id y cantidad de busquedas
      lista_menos = impopular_producto[0]
      for totalbusqueda in impopular_producto:
        if totalbusqueda[2]<menos: #Aqui estoy acomodando de menor a mayor acorde al indice 2, es decir, el contador
          menos=totalbusqueda[2]
          lista_menos=totalbusqueda
      menos_busquedas.append(lista_menos) #a la nueva lista vacia de productos ordenados por busqueda le añado la lista ya acomodada por cantidad de veces buscadas
      impopular_producto.remove(lista_menos) #freno el codigo
    print(menos_busquedas)