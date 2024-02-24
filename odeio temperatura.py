def fahrenheit_para_celsius(fahrenheit):
    
    celsius = (fahrenheit - 32) * 5/9
    return celsius

temperatura_em_fahrenheit = eval(input('Digite uma temperatura:'))
temperatura_em_celsius = fahrenheit_para_celsius(temperatura_em_fahrenheit)

print(f"{temperatura_em_fahrenheit} graus Fahrenheit é igual a {temperatura_em_celsius:.2f} graus Celsius.")

def fahrenheit_para_celsius(fahrenheit):
    celsius=(fahrenheit-32)/1.8
    return celsius

temperatura_em_fahrenheit=eval(input('Digite uma temperatura:'))
temperatura_em_celsius=fahrenheit_para_celsius(temperatura_em_fahrenheit)

print(f'{temperatura_em_fahrenheit} graus fahrenheit é igual a {temperatura_em_celsius:.2f}  graus celcius.')
