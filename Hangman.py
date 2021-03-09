from random import choice
fruits = ['apple', 'bannana', 'cherry', 'orange', 'lemon', 'blueberry', 'peach']
#a = randint(0, len(fruits)-1)
fruit = choice(fruits)

fruit_list = []
for i in fruit:
    fruit_list.append(i)

odp = ['_ '] * len(fruit_list)

used = []

print(fruit)
print("".join(odp))

pictures = [
    '''
    --------------
    |/      |
    |     \\ o /
    |       |
    |      / \\
    |
    ''',
    '''
    --------------
    |/      |
    |     \\ o /
    |       |
    |      / 
    |
    ''',
    '''
    --------------
    |/      |
    |     \\ o /
    |       |
    |       
    |
    ''',
    '''
    --------------
    |/      |
    |     \\ o 
    |       |
    |       
    |
    ''',
    '''
    --------------
    |/      |
    |       o 
    |       |
    |       
    |
    ''',
    '''
    --------------
    |/      |
    |       o 
    |       
    |       
    |
    ''',
    '''
    --------------
    |/      |
    |        
    |       
    |       
    |
    ''',
    '''
    --------------
    |/      
    |        
    |       
    |       
    |
    ''',
    '''
    
    |      
    |        
    |       
    |       
    |
    ''',]

slides = len(pictures) - 1
status = True
while status:
    x = input('Type letter ')
    if x in used:
        print(f'Letter "{x}" is already typed \n')
    else:
        used.append(x)
        if x in fruit_list:
            for i in range(len(fruit_list)):
                if fruit_list[i] == x:
                    odp[i] = x + ' '
        else:
            print(pictures[slides])
            slides -= 1

        print("".join(odp) + '\n')

    if '_ ' not in odp:
        print('VICTORY')
        status = False

    if slides == -1:
        print('GAME OVER')
        status = False

