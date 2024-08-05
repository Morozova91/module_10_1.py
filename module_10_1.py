# Задача "Потоковая запись в файлы":
import time
from threading import Thread


def write_words(word_count, file_name):

    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(word_count):
            f.write(f'Какое-то слово № {i + 1}\n')
            time.sleep(0.1)

    print(f"Завершилась запись в файл {file_name}")



if __name__ == '__main__':
    start_time = time.time()
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')
    end_time = time.time()
    duration = end_time - start_time
    print("Время выполнения функций:", duration)
    start_time_2 = time.time()
    p1 = Thread(target=write_words, args=(10, 'example5.txt'))
    p2 = Thread(target=write_words, args=(30, 'example6.txt'))
    p3 = Thread(target=write_words, args=(200, 'example7.txt'))
    p4 = Thread(target=write_words, args=(100, 'example8.txt'))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()


    end_time_2 = time.time()
    duration_2 = end_time_2 - start_time_2
    print("Время выполнения функций:", duration_2)

