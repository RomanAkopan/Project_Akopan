#В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –мясо, молоко, сыр. Определить:
#1. какие товары из Магнита, отсутствуют в Пятерочке.
#2. какие товары из Пятерочки, отсутствуют в Магните
#3. полный перечень всех товаров.
#4. равны ли перечни товаров

magnit = {"молоко", "соль", "сахар"}
pyaterochka = {"мясо", "молоко", "сыр"}

magnit_only = magnit - pyaterochka
print("1. В Магните, но нет в Пятерочке:", magnit_only)

pyaterochka_only = pyaterochka - magnit
print("2. В Пятерочке, но нет в Магните:", pyaterochka_only)

all_goods = magnit | pyaterochka
print("3. Полный перечень товаров:", all_goods)

are_equal = magnit == pyaterochka
print("4. Перечни товаров равны:", are_equal)