
def operacion(monto:int, denominaciones:list):
    monedas = {}

    for denominacion in denominaciones:
        monedas[denominacion] = monto // denominacion
        monto = monto % denominacion

    monedas["sobrante"] = monto

    return monedas

    # for i in range(len(denominacion)):
    #     logica = monto / denominacion[i]
    #     if logica == 0:
    #         print(f"moneda" + logica)


if __name__ == '__main__':
    monto = 111
    denominaciones = [10,5,2]
    monedas =operacion(monto, denominaciones)

    print(monedas)


