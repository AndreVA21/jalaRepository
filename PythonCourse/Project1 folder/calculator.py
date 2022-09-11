"""
Andre Vladimir Arroyo Hinojosa
calculator
"""
try:
    age = int(input("ingresar edad: "))
except:
    print("debes ingresar un numero")

decades=age//10
years=age%10

display_text= f"age: {age}, decades: {decades}, years: {years}"
print(display_text)