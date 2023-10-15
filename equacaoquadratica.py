
def introducao():
    print("""
        Programa para encontrar as raízes de uma equação quadrática,
        se houver alguma.
        
        Uma equação quadrática é uma equação do tipo: ax² + bx + c = 0,
        onde a, b e c são os coeficientes e x é a variável, sendo que a =/= 0.
        a é o coeficiente quadrático, b é o coef. linear e c é o coef. constante.
        
        Raiz de uma equação é o valor que faz com que o valor da eq. seja igual a 0.
        Uma eq. quadr. pode ter ou uma ou duas ou nenhuma raiz.
        
        """)

#Identificando os coeficientes
def coeficientes():
    a = float(input("\nDigite o valor do coeficiente quadrático 'a': "))
    while a == 0:
        print("O valor de a deve ser diferente de 0!")
        a = float(input("\nDigite o valor do coeficiente quadrático: "))
            
    b = float(input("\nDigite o valor do coeficiente linear 'b': "))

    c = float(input("\nDigite o valor do coeficiente constante 'c': "))
    
    return a, b, c

# Calculando o valor de delta para usá-lo na fórmula de Bhaskara
def calculando_delta(a, b, c):
    delta = (pow(b, 2)) - (4 * a * c)
    
    return delta
    
# Calculando as raizes
def calculando_raizes(a, b, c, delta):
    if delta < 0:
        print("\nA equação quadrática ", a, "x² + ", b, "x + ", c, " = 0 não tem raiz.")
    elif delta == 0:
        primeira_raiz = ((-1 * b) + pow(delta, 0.5)) / (2 * a)
        print("\nA equação quadrática ", a, "x² + ", b, "x + ", c, " = 0 tem apenas uma raiz que é ", primeira_raiz, ".")
    else:
        primeira_raiz = ((-1 * b) + pow(delta, 0.5)) / (2 * a)
        segunda_raiz = ((-1 * b) - pow(delta, 0.5)) / (2 * a)
        print("\nA equação quadrática ", a, "x² + ", b, "x + ", c, " = 0 tem duas raízes que são ", primeira_raiz, " e "
              , segunda_raiz, ".")
        

introducao()
a, b, c = coeficientes()
delta = calculando_delta(a, b, c)
calculando_raizes(a, b, c, delta)
