import random 

def dis(a,b):
    if a==0:
        print(b,'= rock')
        
    elif a==1:
        print(b,'= paper')
        
    else:
        print(b,'= scisser')
  
  
while True:
            
    bot =random.randint(0,2)

    print('enter 0 for rock ,1 for paper and 2 for scisser and enter no to end the game ')
    player =input('entet :')
    
    if player=='no':
        break

    elif bot ==player :
        dis(player,'player')
        dis(bot,'bot')
        print('DRAW ')
    
    elif bot =='0' and player=='2' or bot=='1' and player=='0' or bot=='2' and player=='1' :
        dis(player,'player')
        dis(bot,'bot')
        print('YOU LOSE ')
    
    else:
        dis(player,'player')
        dis(bot,'bot')
        print('YOU WIN\n')
