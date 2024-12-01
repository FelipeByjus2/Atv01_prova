
try: 
    base = float(input("Informe a base do retângulo (cm): "))
    altura = float(input("Informe a altura do retângulo (cm): "))
    
    area = round((base * altura),4)
    print(f'A área do retângulo é: {area}')
    
except ValueError:
    print("Por favor, informe somente números.")
    
