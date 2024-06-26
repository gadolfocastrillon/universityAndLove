#import numpy as np
#import matplotlib.pyplot as plt 
#import matplotlib.image as mping

class Objeto: 
    
    def __init__(self,codigo_,nombre_,cantidad_, precio_, image_icon_= 'No_direccion'):
        self.codigo = codigo_
        self.nombre = nombre_ 
        self.cantidad = cantidad_
        self.precio = precio_
        self.image_icon = image_icon_
        self.active_to_sell = True #Se puede vender en la tienda
        self.active_to_eat = True  #Se puede comer fuera de combate
        self.active_to_use = True  #Se puede usar en combate
        self.cantidad_maxima = 20
       
    #---------------------------------------------------------------------
    #--------------------Getters------------------------------------------
    #---------------------------------------------------------------------
    def get_active_to_sell(self):
        return self.active_to_sell
    
    def get_active_to_eat(self): 
        return self.active_to_eat
    
    def get_active_to_use(self): 
        return self.active_to_use
    
    def get_cantidad_maxima(self):
        return self.cantidad_maxima
    
    def get_codigo(self): 
        return self.codigo 
    
    def get_nombre(self): 
        return sel.nombre
    
    def get_cantidad(self): 
        return self.cantidad
    
    def get_precio(self): 
        return self.precio
    
    def get_image_icon(self):
        return self.image_icon
    
    #---------------------------------------------------------------------
    #--------------------Setters------------------------------------------
    #---------------------------------------------------------------------
    
    def set_cantidad_maxima(self,valor):
        self.cantidad_maxima = valor
        
    def set_active_to_sell(self,valor):
        if(type(valor) != bool):
            print("Error, el tipo no es booleano")
        else: 
            self.active_to_sell = valor
            
    def set_active_to_eat(self,valor):
        if(type(valor)!= bool): 
            print("Error, el tipo no es booleano")
        else: 
            self.active_to_eat = valor
        
    def set_active_to_use(self,valor): 
        if(type(valor) != bool): 
            print("Error, el tipo no es booleano")
        else: 
            self.active_to_use = valor
            
    #---------------------------------------------------------------------
    #--------------------Funciones----------------------------------------
    #---------------------------------------------------------------------
    #Crea un operador para aumentar la cantidad con +=
    def __iadd__(self,valor): 
        self.cantidad += valor
        return self
    
    #Crea un operador para disminuir la cantidad con -=
    def __isub__(self,valor):
        if (self.cantidad <= 0): 
            self.cantidad = 0
        else: 
            self.cantidad -= valor
        return self
    
    #Realiza una conversión del dinero
    def particionar_cantidad(self,cantidad):
        #La conversión se hace desde los bronces, self.precio siempre tendrá su valor en bronces
        valor_oro = 10000
        valor_plata = 100
        oro = cantidad // valor_oro 
        residuo = cantidad % valor_oro 
        plata = residuo // valor_plata
        bronce = residuo % valor_plata
        return [oro,plata,bronce]
    
    '''
    #Muestra la imagen del objeto
    def mostrar(self):
        fig, ax = plt.subplots()
        ax.imshow(self.image_icon)
        ax.axis('off')
        plt.show()
        return self
    '''

    #Crea el operador para mostrar con print
    def __str__(self):
        #self.mostrar()  
        cadena = self.nombre + "\n"
        cadena += "Cantidad: " + str(self.cantidad) +"\n"
        precios = self.particionar_cantidad(self.precio)
        cadena += "Precio: " + str(precios[0]) + " oros " + str(precios[1]) + " platas " + str(precios[2]) + " bronces\n"
        return cadena

    def get_cadena(self): 
        cadena = self.nombre + "\n"
        cadena += "Cantidad: " + str(self.cantidad) +"\n"
        precios = self.particionar_cantidad(self.precio)
        cadena += "Precio: " + str(precios[0]) + " oros " + str(precios[1]) + " platas " + str(precios[2]) + " bronces\n"
        return cadena