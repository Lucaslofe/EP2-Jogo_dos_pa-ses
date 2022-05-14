from dados import *
from funcoes import *
lista_de_paises = normaliza(DADOS)


def milhar(s, sep): # s = string, sep pode ser '.' ou ','
     return s if len(s) <= 3 else milhar(s[:-3], sep) + sep + s[-3:]

print(milhar('545434343534332', '.'))



 


