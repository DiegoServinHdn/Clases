
def operacion(monto:int, denominacion:list):

    for i in range(len(denominacion)):
        logica = monto / denominacion[i]
        if logica == 0:
            print(f"moneda" + logica)


if __name__ == '__main__':
    monto = 100
    denominacion = [10,5]
    operacion(monto, denominacion)


