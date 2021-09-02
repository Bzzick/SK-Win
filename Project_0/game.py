"""Game to guess the number    """
import numpy as np

number = np.random.randint(1, 101)  # guessing the nubmer

#number of tries
count = 0

while True:
    count +=1
    predict_number = int (input("Guess the number from 1 to 100: "))
    
    if predict_number > number:
        print("The nubmer should be smaller")
    
    elif predict_number < number:
        print("The number should be bigger")
        
    else:
        print(f"You have guessed the nubmer! It is = {number} in {count} tries")
        break # the game is over
