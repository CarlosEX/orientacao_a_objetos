
def minha_lista():

    return {
        'frutas': ['maça', 'uva', 'banana'],
        'local': ['ruas das aves'],
        'supermercado': 2,
        'extras': {'doces': 'chocolare', 'sucos': 'Morango'}
    }

lista = minha_lista()
lista['frutas'] = 'qualquer coisa' # tipagem dinâmica


print(lista)