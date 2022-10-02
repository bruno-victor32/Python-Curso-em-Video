#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Digite uma cidade: ')).upper().strip().split()
print('Essa cidade começa com SANTO? {}'.format('SANTO' in cidade[0]))
