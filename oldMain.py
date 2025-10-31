
# funciones en python con sobrecarga de funciones
#Serie de Taylor para calcular ln (logaritmo natural)
def mostrarSerieTaylor(x,n):
    ac=0;
    apagador=False;
    for i in range(1,n+1):
        if apagador==False:
            ac=ac+ 1/i* (x-1)**i
            apagador=True
        elif apagador==True:
            ac = ac - 1 / i * (x - 1) ** i
            apagador=False
        print(f'{ac}, ')

def mostrarSerieTaylor(h):
    print("funcion dummy no hacenada aqui esta tu parametro",h)

def solictarParametros():
    n = int(input("Potencia?: "))
    x= int(input("x?: "))
    return x,n


def print_hi(name):
    print(f'Hi, {name}')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('ejercicio fucniones')
    xx,p=solictarParametros()
    mostrarSerieTaylor(xx)



