import random

class GeraDocs:
    def generate_cpf():                                                        
        cpf = [random.randint(0, 9) for x in range(9)]                              

        for _ in range(2):                                                          
            val = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11      

            cpf.append(11 - val if val > 1 else 0)                                  

        return '%s%s%s.%s%s%s.%s%s%s-%s%s' % tuple(cpf)

    def generate_cnpj():                                                       
        def calculate_special_digit(l):                                             
            digit = 0                                                               

            for i, v in enumerate(l):                                               
                digit += v * (i % 8 + 2)                                            

            digit = 11 - digit % 11                                                 

            return digit if digit < 10 else 0                                       

        cnpj =  [1, 0, 0, 0] + [random.randint(0, 9) for x in range(8)]             

        for _ in range(2):                                                          
            cnpj = [calculate_special_digit(cnpj)] + cnpj                           

        return '%s%s.%s%s%s.%s%s%s/%s%s%s%s-%s%s' % tuple(cnpj[::-1])

def geradorDePisPasep(formatar):
    arNumeros = []
    for i in range(10):
        arNumeros.append(random.randint(0, 9))

    somaJ = (arNumeros[0] * 3) + (arNumeros[1] * 2) + (arNumeros[2] * 9) + (arNumeros[3] * 8) + \
            (arNumeros[4] * 7) + (arNumeros[5] * 6) + (arNumeros[6] * 5) + (arNumeros[7] * 4) + \
            (arNumeros[8] * 3) + (arNumeros[9] * 2)

    restoJ = somaJ % 11
    subtracao = 11 - restoJ

    if subtracao == 10 or subtracao == 11:
        j = 0
    else:
        j = subtracao

    arNumeros.append(j)

    pis = ''.join(str(x) for x in arNumeros)

    if formatar:
        return pis[:10] + '-' + pis[10:]
    else:
        return pis

