n = input('You are in the last forest\n***************\n  🙂\n***************\nGo left or right? ')
counter = 0
while n.lower() == 'right':
    counter +=1
   
    if counter < 2:
         n = input('You are in the last forest\n***************\n  🙂\n***************\nGo left or right? ')
    elif counter == 2:
          n = input('You are in the last forest\n***************\n  🙁\n***************\nGo left or right? ')
    else:
         n = input('You are in the last forest\n********    ***\n  (╯°□°）╯︵ ┻━┻\n***************\nGo left or right? ')
         
print('\nYou got out of the lost Forest!\n\o/')
