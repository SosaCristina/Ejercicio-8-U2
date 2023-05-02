
class Conjunto:
    __listaNumero=[]

    def __init__(self):
        self.__listaNumero=[]

    def agregar (self,num):
        self.__listaNumero.append(num)

    def obtenerLista (self):
        return self.__listaNumero
    
    def __add__(self, otro):
        nueva=self.__listaNumero.copy()
       
        for i in range (len(otro.obtenerLista())):
            j=0
            while(j<len(self.__listaNumero) and (self.__listaNumero[j]!=otro.obtenerLista()[i])):
                j+=1
            if(j>=len(self.__listaNumero)):
                nueva.append(otro.obtenerLista()[i])
        print("UNION",nueva)        
                

    def __sub__(self, otro):
        nueva=self.__listaNumero.copy()

        for i in range (len(otro.obtenerLista())):
            j=0
            while(j<len(otro.obtenerLista()))and (self.__listaNumero[j]!=otro.obtenerLista()[i]):
                j+=1
            if (j<len(otro.obtenerLista())):
                nueva.pop(j)
        print("DIFERENCIA",nueva) 

    def __eq__(self,otro):

        if (len(self.__listaNumero)!=(len(otro.obtenerLista()))):
            print("Los conjuntos son distintos")
        else:
            i=0
            bandera=True
            while (i< (len(otro.obtenerLista())) and (bandera==True)):
                j=0
                while (j<len(otro.obtenerLista()) and (self.__listaNumero[j]!=otro.obtenerLista()[i])):
                    j+=1
                if (j>=(len(otro.obtenerLista()))):
                    print("Los conjuntos no son iguales")
                    bandera=False
            
                else:
                    i+=1
            if bandera==True:
                print("Los conjuntos son iguales")



