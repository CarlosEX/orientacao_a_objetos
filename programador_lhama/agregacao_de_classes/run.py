from produto import Produto
from carrinho_de_compra import CarrinhoDeCompras

car = CarrinhoDeCompras()
monitor = Produto('Dell Expirion', 1000.54)
cerveja = Produto('Brahama', 34.51)
teclaso = Produto('Sansung', 64.92)

car.adicionar_produto(monitor)
car.adicionar_produto(cerveja)
car.adicionar_produto(teclaso)
car.finalizar_compra()