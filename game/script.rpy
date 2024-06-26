define s = Character('Luna', color="#c8ffc8")
define pov = Character('[povname]',color="#FF7F50")
define sin = Character('',color="#FF7F50")
image bedroom day = 'Scenes/Bedroom_Day.png'
image fondo negro = 'Scenes/fondo_negro.png'
image pp1 = 'Characters/Personaje_principal.png'


init python: 
    
    class Inventario: 
        def __init__(self): 
            self.items = [] 

        def add_item(self,item): 
            self.items.append(item)

        def search_item(self,nombre): 
            for item in self.items: 
                if item.nombre == nombre: 
                    return item
            return none

        def __str__(self): 
            cadena = "" 

            if len(self.items) <1:
                s("No tengo nada en mi inventario.")
                return cadena 
            else: 
                s("En mi inventario tengo...")
                for item in self.items: 
                    #s(item.get_cadena())
                    s(str(item))
                return cadena 

        def mostrar_inventario(self):
            if len(self.items) < 1:
                sin("No tengo nada en mi bolso.")
            else:
                sin("En mi bolso tengo...")
                for item in self.items: 
                    #sin(item.get_cadena())
                    sin(str(item))
                    #in(item.get_image_icon())

        def __len__(self): 
            return len(self.items)

        def aum_cantidad(self,nombre,cantidad): 
            objeto = self.search_item(nombre)
            if objeto:
                if (cantidad + objeto.cantidad <= objeto.cantidad_maxima):
                    objeto += cantidad
                else:
                    objeto.cantidad = objeto.cantidad_maxima

        def dis_cantidad(self,nombre,cantidad):
            objeto = self.search_item(nombre)
            if objeto: 
                if(objeto.cantidad <=0):
                    self.items.remove(objeto)
                else: 
                    objeto -= cantidad


init python: 

    import class2 as cl

    manzana_roja = cl.Comida("0001","Manzana roja", 5,50,15,7)
    manzana_verde = cl.Comida("0002","Manzana roja", 5,2500,30,15)
    manzana_azul = cl.Comida("0003","Manzana roja", 5,10000,60,30)
    cuaderno_matematicas = cl.Item("0004",'cuaderno de matematicas',1,1000)
    cuaderno_matematicas.mod_car(False,False,False)
    cuaderno_lengua = cl.Item("0005","Cuaderno de lengua",1,1000)
    cuaderno_lengua.mod_car(False,False,False)

label start: 

    
    $from clas import Objeto
    scene fondo negro
    show pp1

    $ povname = renpy.input("¿Cual es tu nombre?", length = 32) #para modificar el nombre
    #La variable se almacena en povname
    $print(str(povname))
    $pj = cl.Personaje(name_=str(povname))
    $elemento = str(pj) #Me permite extraer el __str__ de pj
    #$pov(elemento) #Me muestra en pantalla del juego elemento
    pov "Este soy yo, [povname]."
    pov "Actualmente, estoy a punto de curzar el último año."
    pov "Soy estadounidense."
    pov "Vivia con mi madre en la ciudad de New York desde la separación de mis padres."
    pov "Debido a problemas en mi antiguo colegio, 
    mi madre decidio mandarme a vivir a Japón con mi padre."
    pov "Ahora vivo con mi padre en la ciudad de Tokyo."

    hide pp1
    show bedroom day
    pov "Mi habitación no es tan grande como la que tenia en mi antigua casa,
    pero toca conformarme con eso."
    pov "Revisemos que tengo en mi bolso"

    $inventory = Inventario()
    #Comida(codigo_,nombre_,cantidad_, precio_,reg_life_,reg_mana_,image_icon_="Direccion")
    #Item(codigo_,nombre_,cantidad_, precio_, image_icon_= 'No_direccion'):
    
    $inventory.mostrar_inventario()
    $inventory.add_item(manzana_roja)
    $inventory.add_item(cuaderno_matematicas)
    $inventory.add_item(cuaderno_lengua)
    $inventory.mostrar_inventario()
    $inventory.add_item(cuaderno_matematicas)
    $inventory.mostrar_inventario()
    

    pov "Esto esta bien, ya tengo mi cuaderno de matematicas y mi cuaderno de lengua,
    ademas tengo una manzana para comer en receso."
    pov "Me faltaria empacar mi cuaderno de ciencias y un cuaderno de kanji"
    pov "Algunos se preguntaran que sucede con el idioma ..."
    pov "Resulta que desde pequeño se me instruyo por parte de mi madre en el aprendizaje de japones
    esto ya que ambos, tanto padre y madre son japoneses, pero por la separación papá volvio a vivir
    a Japón"
    pov "Aparte tengo un plus en el colegio y es que también se hablar ingles, así que no tendre problemas
    con el aprendizaje de este."
