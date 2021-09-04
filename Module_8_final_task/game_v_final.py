"""Игра угадай число
Компьютер сам загадывает и сам угадывает число от 1 до 100. Цель угадать число менее чем за 20 попыток при 1000 выполнений программы
"""

import numpy as np #Импорт библиотеки "numpy"

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    a = 1 # а - изменяемая нижняя граница, будет использована для сужения диапазона чисел
    b = 100 # b - изменяемая нижняя граница, будет использована для сужения диапазона чисел
    
    while True:
        count += 1
        c = (b -a)//2 #сужение диапазона вдвое (деление на 2)
        if c == 0: 
            c=1
        ###predict_number = np.random.randint(int(a+c), int(b+1))  # предполагаемое число ## закладка на случай внедрения случайного угадывания - НЕ ЕСПОЛЬЗОВАЛ
        predict_number = a+c
           
        if predict_number > number:
            #print("Число должно быть меньше!") - ДЛЯ КОНТРОЛЯ
            b = predict_number #если число должно быть меньше чем текущее число -> верхняя граница становится числом указанным в данной попытке
            

        elif predict_number < number:
            #print("Число должно быть больше!") - ДЛЯ КОНТРОЛЯ
            a = predict_number #если число должно быть больше чем текущее число -> нижняя граница становится числом указанным в данной попытке
        
        else:
            #print(f"Вы угадали число! Это число = {number}, за {count} попыток") #- ДЛЯ КОНТРОЛЯ
            break #конец игры выход из цикла
            
    return count # возвращает за сколько попыток было угадано текущее число
    
def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict (function): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости - НЕ ИСПОЛЬЗОВАЛ
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    #print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток") #- ДЛЯ КОНТРОЛЯ, НЕ ИСПОЛЬЗОВАЛ
    return score
    
if __name__ == "__main__":
    #RUN
    print(f"Ваш алгоритм угадывает число в среднем за:{score_game(random_predict)} попыток")