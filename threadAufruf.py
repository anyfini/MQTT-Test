import threading
import os
import time
import multiprocessing
import concurrent.futures

zahl = 0


def aufruf():
    os.system("py C:\\Users\Fin\PycharmProjects\mqtt-Test\\threadTest.py " + str(zahl))


def zahlBst():
    global zahl
    print(zahl)
    zahl = 1
    return zahl

def run():
    y1 = threading.Thread(target=zahlBst)
    y2 = threading.Thread(target=aufruf)

    y1.start()
    # time.sleep(0.1)                # falls die Funktion der zahlBst zu lange dauert um eine Zahl zu returnen
    y2.start()
    return 'run Complete'

if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executer:
        # f1 = executer.submit(run)
        # f2 = executer.submit(run)
        # print(f1.result())
        # print(f2.result())
        #mit einer List-Comprehension
        results = [executer.submit(run) for _ in range(10)]    # Submit übergibt eine Funktion zur Zeit
        for f in concurrent.futures.as_completed(results):
            print(f.result()) # Ausgabe des Return Values der Funktion run

    # processes = []
    # for _ in range(10):
    #     p = multiprocessing.Process(target=run)
    #     p.start()
    #     processes.append(p)
    #
    # for process in processes:
    #     process.join()
    # print("finish")
