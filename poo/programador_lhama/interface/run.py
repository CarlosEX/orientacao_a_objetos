from terrenos.quadrado import TerrenoQuadrado
from terrenos.retangulo import TerrenoRetangular
from engenheiro import Engenheiro

engenheiro = Engenheiro('Carlos')
terrenoQuadrado = TerrenoQuadrado(4)
terrenoRetangular = TerrenoRetangular(2, 5)

engenheiro.medir_area(terrenoQuadrado)