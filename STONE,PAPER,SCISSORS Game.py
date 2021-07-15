import random




while True:
    try:
        print('enter 1 for stone, 2 for paper, 3 for scissors and 0 for quit')
        player = int(input()) 
    except ValueError:
        print('Oops!!! letters not allowed...\n\n')
        continue

     
   
    computer = random.randint(1,3)
     
    if player == 0:
        break    
        
    elif player == computer:
        print(computer)
        print('match tie...\n')
    elif player == 1 and computer == 2:
        print(computer)
        print('computer wins!!\n')
    elif player == 1 and computer == 3:
        print(computer)
        print('player wins!!\n')
    elif player == 2 and computer == 1:
        print(computer)
        print('player wins!!\n')
        
    elif player == 2 and computer == 3:
        print(computer)
        print('computer wins.. \n')
        
    elif player == 3 and computer == 1:
        print(computer)
        print('computer wins..\n')
    elif player == 3 and computer == 2:
        print(computer)
        print('player wins!!\n')
    else:
        print('\n enter the correct number.....\n \n  ')
        continue
        
        
    

        

    
           


    




   