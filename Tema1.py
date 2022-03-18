lista = [7,8,9,2,3,1,4,10,5,6]
print(lista,'\n')

lista_ordonata_ascendent = sorted(lista)
print(lista)
print('lista_ordonata_ascendent =', lista_ordonata_ascendent, '\n')

lista_ordonata_descendent = sorted(lista, reverse=True)
print(lista)
print('lista_ordonata_descendent =', lista_ordonata_descendent, '\n')

lista_para_ordonata_ascendent = lista_ordonata_ascendent[1::2]
print(lista_ordonata_ascendent)
print('lista_para_ordonata_ascendent =', lista_para_ordonata_ascendent, '\n')

lista_impara_ordonata_ascendent = lista_ordonata_ascendent[::2]
print(lista_ordonata_ascendent)
print('lista_impara_ordonata_ascendent =', lista_impara_ordonata_ascendent, '\n')

lista_multipli_de_3 = lista_ordonata_ascendent[2::3]
print('lista_multipli_de_3 =', lista_multipli_de_3)
