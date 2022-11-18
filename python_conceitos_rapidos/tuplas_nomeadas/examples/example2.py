from collections import namedtuple

MyList = namedtuple("compra", "frutas local super extras")

def minha_lista():

    return MyList(
        frutas=["maça", "uva", "banana"],
        local="ruas das aves",
        super=2,
        extras={"doces": "chocolare", "sucos": "Morango"}
    )

def minha_lista2():

    return MyList(
        frutas=["pera", "laranja", "melancia"],
        local="avenida santos",
        super='São pedro',
        extras={"bolos": "morango", "sucos": "Uva"}
    )

lista = minha_lista()
lista2 = minha_lista2()

# print(lista)
print(lista)
print(lista2)
