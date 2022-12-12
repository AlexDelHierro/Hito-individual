import pprint
#Creamos el diccionario con los productos que se pueden comprar
ropa={'Camiseta':15.99,'Gorro':9.99,'Calcetines':9.99,'Gorra':17.99,'Pantalon':30.99,'Bandolera':15.99,'Bermudas':9.99,'Gafas':10.99,'Chaqueta':153.24}

class Bienvenida:
    def __init__(self,nombre,apellido,edad,fecha_nacimiento,vivienda,tlf,email): #Construimos una funcion para crear un formulario para los datos del cliente
        self.nombre=nombre  #Damos valores a las variables
        self.apellido=apellido
        self.edad=edad
        self.fecha_nacimiento=fecha_nacimiento
        self.vivienda=vivienda
        self.tlf=tlf
        self.email=email
    print('Bienvenido/a, para seguir con su compra realize el siguiente registro')
    def registro(self): #Esta funcion nos servira para mostrar el registro en pantalla
        print('')
        print('Su registro:')
        #Con este print hacemos que se muestren todos los datos rellenados por el cliente
        print(f'nombre: {self.nombre}\napellidos: {self.apellido}\nedad: {self.edad} años\nfecha de nacimiento: {self.fecha_nacimiento}\nvivienda: {self.vivienda}\nTelefono: {self.tlf}\nEmail: {self.email}')
        #Creo una funcion confirmar para asi darle la opción al cliente de volver a rellenar sus datos en caso de que se haya equivocado
        confirmar = input('Confirme si sus datos soncorrectos: ')
        #La variable de este ehile es que siempre y cuando la respuesta no sea si volvera a dar la opcón al cliente de volver a rellenar sus datos
        while confirmar.lower()!='si':
            print()
            print('Vuelva a rellenar el registro')
            cliente1=Bienvenida(input('Nombre: '),input('apellido: '),input('edad: '),input('fecha de nacimiento(xx/xx/xxxx): '),input('vivienda: '),int(input('Telefono movil: ')),input('Email: '))
            print()
            print('Su registro:')
            print(f'nombre: {self.nombre}\napellidos: {self.apellido}\nedad: {self.edad} años\nfecha de nacimiento: {self.fecha_nacimiento}\nvivienda: {self.vivienda}\nTelefono movil: {self.tlf}\nEmail: {self.email}')
            confirmar = input('Confirme si sus datos soncorrectos: ')


        print(f'Prosigamos con la compra {self.nombre}')
        print()
        print('Estos son nuestros productos')
#Con el objeto cliente1 hacemos que sea posible el registro del cliente
cliente1 = Bienvenida(input('Nombre: '), input('apellido: '), input('edad: '),input('fecha de nacimiento(dd/mm/yyyy): '), input('vivienda: '),int(input('Telefono movil: ')),input('Email: '))
cliente1.registro()
#Esta funcion lo que hace es imprimir el diccionario para mostrar al cliente los productos y sus precios
pprint.pprint(ropa)

#A continuacion creamos dos listas vacias en las que se almacenarán los productos según el usuario desée
cesta={}
lista_deseos={}

#La funcion Producto nos permite seleccionar donde queremos almacenar nuestros productos
def Producto():
    nomp=input('Elige el producto deseado(El nombre debe estar exacto): ')
    print('--------------------------------------------------------------')
    # ¿Agregar a la cesta o a la lista de desos?
    agrega = float(input(f'Quieres agregar "{nomp}" a la cesta (1) o a la lista de deseos (2): '))
    # si lo agregamos a la cesta
    if agrega == 1:
        # Almacena el valor en la cesta
        cesta[nomp] = ropa[nomp]
        # Y nos muestra que tenemos en la cesta
        print(f'Cesta: {cesta}')
        # Y nos imprime el total de lo que hay en la cesta sin haber sumado el IVA
        print(f'Total: {sum(cesta.values())}')
    # si lo agregamos a la lista de deseos
    elif agrega == 2:
        # Almacena el valor en la lista de deseos
        lista_deseos[nomp] = ropa[nomp]
        # Y nos muestra la lista de deseos
        print(f'Lista de deseos: {lista_deseos}')
        # Y nos imprime el total de lo que hay en la lista sin haber sumado el IVA
        print(f'Total: {sum(lista_deseos.values())}')
    # Si Seleccionas algo sin querer que no sea ni 1 ni 2 volvera a preguntarte el valor para poder hacerlo
    elif agrega >= 3:
        print('Introduce una opción válida')



Producto()

#Con esta funcion logramos recordar al cliente que si tiene productos en la lista de desos que los mueva a la cesta
def scompra():
    print()
    seguir_compra=input('¿Desea seguir comprando?\n')
    #En caso de seguir comprando nos volvera a mostras el stock de la tienda y nos dejara volver a seleccionar productos y añadirlos a la cesta o la lista de deseos
    if seguir_compra.lower() == 'si':
        #Invocamos el diccionario de los productos
        pprint.pprint(ropa)
        #Invocamo las funciones para poder seleccionar y agregar productos
        Producto()
        scompra()
    #Si no queremos seguir comprando nos recuerda que debemos mover los productos de la lista de deseos a la cesta
    #Aquí el problema que he teneido es que no sabia como hacer para que nos dejase seleccionar más de un producto
    elif seguir_compra.lower() == 'no':
        print('Recuerda mover tus productos de la lista de deseos a la cesta')
        mdeseo=float(input('¿Quieres añadir los productos de la lista de deseos a la cesta? SI(1) NO(2)\n'))
        #Lo que nos hace el match case es que en caso de haber seleccionado 1 nos permite seleccionar los productos y moverlos a la cesta, y nos muestra la cesta y el total
        # y en caso de haber seleccionado 2 nos llevara a la zona de pago
        match mdeseo:
            case 1:
                pprint.pprint(lista_deseos)
                cambio=input('Añada sus productos a la cesta (recuerde escribirlos a cholon:\n')
                cesta[cambio] = ropa[cambio]
                print(f'Cesta: {cesta}')
                print(f'Total: {sum(cesta.values())}')

            case 2:
                print('Estas yendo a pagar')
    else:
        print('Debe escribir si o no')
        scompra()
scompra()

#La función pagar lo que nosn hace es que segun el pais que pongamos nos aplique un IVA u otro
def pagar():
    #Escribimos el país
    pais=input('Dinos tu pais\n')
    #Si el pais es españa nos aplica un 21%
    if pais.lower() == 'españa':
        print('El IVA de España es del 21%')
        print(f'El total con IVA incluido será de {sum(cesta.values())*1.21}€')
    #Si el pais es otro nos aplica un 15%
    else:
        print('Al ser internacional el IVA que se aplicara será de un 15%')
        print(f'El total con IVA incluido será de {sum(cesta.values())*1.15}€')

    print()
    print('Para finalizar su compra deberá elegir la forma de pago')
    #Elegimos la forma de pago y tenemos 4 opciones
    fpago=int(input('1| Pago con tarjeta\n2| PayPal\n3| Bitcoin\nSeleccione su forma de pago (Formato numero): '))
    print()
    #Con el match case lo que hacemos es que segun la forma de pago que elijamos rellenemos unos datos u otros
    match fpago:
        case 1:
            print('Usted ha decidido pagar con tarjeta rellene los siguientes datos')
            print()
            ntarjeta=input('Numero de tarjeta: ')
            fcaduca=input('Fecha de caducidad(mm/yy): ')
            cvv=input('CVV: ')
            print(f'Numero de tarjeta: {ntarjeta}\nFecha de caducidad: {fcaduca}\nCVV: {cvv}')
            confirmdat1=input('¿Sus datos son correctos?')
            #Con estos whiles lo que hacemos es que si el cliente se equivoca pueda volver a rellernarlos hasta tenerlos bien
            while confirmdat1.lower() != 'si':
                ntarjeta = input('Numero de tarjeta: ')
                fcaduca = input('Fecha de caducidad(mm/yy): ')
                cvv = input('CVV: ')
                print()
                print(f'Numero de tarjeta: {ntarjeta}\nFecha de caducidad: {fcaduca}\nCVV: {cvv}')
                confirmdat1 = input('¿Sus datos son correctos?\n')
            fact=input('Desea que la factura se envie ¿por Email? o ¿por SMS?\n')
            if fact.lower() == 'email':
                print('La factura ha sido enviada a su correo electrónico')
            else:
                if fact.lower() == 'sms':
                    print('La factura ha sido enviada a por sms')
                else:
                    print('Opción erronea porfavor reinicie el programa')
                print()


        case 2:
            print('Usted ha decidido pagar con Paypal rellene los siguientes datos')
            print()
            correo=input('Correo electrónico: ')
            contra=input('contraseña: ')
            print()
            print(f'correo: {correo}\ncontraseña: {contra}')
            confirmdat2 = input('¿Sus datos son correctos?\n')
            while confirmdat2.lower() != 'si':
                print()
                print('Rellene de nuevo sus datos')
                correo = input('Correo electrónico: ')
                contra = input('contraseña: ')
                print(f'correo: {correo}\ncontraseña: {contra}')
                confirmdat2 = input('¿Sus datos son correctos?\n')
            fact1 = input('Desea que la factura se envie ¿por Email? o ¿por SMS?\n')
            if fact1.lower() == 'email':
                print('La factura ha sido enviada a su correo electrónico')
            else:
                if fact1.lower() == 'sms':
                    print('La factura ha sido enviada a por sms')
                else:
                    print('Opción erronea porfavor reinicie el programa')
                print()

        case 3:
            print('Usted ha decidido pagar con Bitcoin rellene los siguientes datos')
            print()
            nbolsa = input('Nº bolsa: ')
            contra2 = input('contraseña: ')
            print()
            print(f'Nº bolsa: {nbolsa}\ncontraseña: {contra2}')
            confirmdat2 = input('¿Sus datos son correctos?\n')
            while confirmdat2.lower() != 'si':
                print()
                print('Rellene de nuevo sus datos')
                nbolsa = input('Nº bolsa: ')
                contra2 = input('contraseña: ')
                print(f'correo: {nbolsa}\ncontraseña: {contra2}')
                confirmdat2 = input('¿Sus datos son correctos?\n')
            fact1 = input('Desea que la factura se envie ¿por Email? o ¿por SMS?\n')
            if fact1.lower() == 'email':
                print('La factura ha sido enviada a su correo electrónico')
            else:
                if fact1.lower() == 'sms':
                    print('La factura ha sido enviada a por sms')
                else:
                    print('Opción erronea porfavor reinicie el programa')
                print()

pagar()
#Y por último con esta funcion imprime un texto dando las gracias
def agradecer():
    print()

    print('Muchas gracias por su compra esperemos volver a verle')
agradecer()


