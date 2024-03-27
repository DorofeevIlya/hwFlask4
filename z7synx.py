from random import randint
import time


test_array = [randint(1, 100) for _ in range(1000001)]


def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        print(f'Время выполнения {execution_time:.2f} ')
        return result
    return wrapper

@calculate_time
def summ_sync(user_array):
    summa = 0
    for num in user_array:
        summa += num
    return summa



if __name__ == '__main__':
    print(f'Сумма: {summ_sync(test_array)}')