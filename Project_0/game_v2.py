"""Game to guess the number , computer will guess on its own   """
import numpy as np

def random_predict(number:int=1) -> int:
    """Trying to guess the number

    Args:
        number (int, optional): Guessed number. Defaults to 1.

    Returns:
        int: Number of tries
    """
    count = 0
    while True:
        count +=1
        predict_number = np.random.randint(1, 101) #generating  suggested number 
        if number == predict_number:
            break #exit if guessed right
    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для вопроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
#print (f"Number of tries:  {random_predict(10)}")
score_game(random_predict)
#changed


