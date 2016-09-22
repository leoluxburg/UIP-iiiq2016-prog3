"""
Autor: Leonardo Conte
Programa: Convertor Moterario Internacional

"""


print ("Convertor Moterario Internacional")
print ("""Ingrese un valor en centavos de moneda y se tranformara a:
    -USD
    -EUR
    -YEN
    -BP
    -MXN
""")

coin = int(input("Valor monetario:"))#monedas

usd = coin * 1/100
eur = usd * 0.90
yen = usd * 101.5744
bp = usd * 0.77
mxn = usd * 19.7843


print ("Dolares: %.2f USD" %usd)
print("Euros: %.2f EUR" %eur)
print("Yen: %.2f yen" %yen)
print("Libras: %.2f BP" %bp)
print ("Pesos Mexicanos: %.2f MX" %mxn)
