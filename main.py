import asyncio

from z7synx import summ_sync, test_array
from z7asynx import summ_async
from z7multiproc import summ_multiproc
from z7thread import summ_threads


if __name__ == '__main__':
    print(f'Синхронный: {summ_sync(test_array)}')

    print(f'Многопоточный: {summ_threads(test_array)}')

    print(f'Многопроцессорный: {summ_multiproc(test_array)}')

    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(summ_async(test_array))
    print(f'Асинхронный: {result}')
