import random

mano = ["Piedra", "Papel", "Tijeras"]
compu = random.choice(mano)
humano = (input('¿Piedra, Papel o Tijeras?\n'))

if humano.capitalize() not in(mano):
    print('Argumento inválido: Debe ser piedra, papel o tijera.')

else: 
        print(f'\n Tú jugaste {humano}...\n')
        print(f'\n Computador jugó {compu}...\n')
        if (compu == humano):
            print('Empatados....\n') 
        else:
                if (humano =='Piedra' and compu =='Tijeras') or ( humano =='Papel' and compu=='Piedra') or ( humano =='Tijeras' and compu=='Papel'):
                    print('Ganaste!!! \n') 
                else: 
                    print('El computador Ganó \n') 
            

#Alumna Karen Cabrera 28-02-2024 (compu =='Piedra' and humano =='Tijeras') or ( compu =='Papel' and humano=='Piedra') or ( compu =='Tijeras' and humano=='Papel'):
    