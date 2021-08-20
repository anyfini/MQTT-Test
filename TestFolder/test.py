import threading
import multiprocessing
import time


def run():
    print("schlafen für 1 s")
    time.sleep(1)
    print("fertig geschlafen")

# if __name__ == '__main__':
#     t_st = time.time()
#     threads = []
#     for _ in range(100):
#         t = threading.Thread(target=run)
#         t.start()
#         threads.append(t)
#     for thread in threads:
#         thread.join()
#     t_end = time.time()
#     diff = t_end - t_st
#     print(diff)

if __name__ == '__main__':
    t_st = time.time()
    processes = []
    for _ in range(100):
        p = multiprocessing.Process(target=run)
        p.start()
        processes.append(p)
    for process in processes:
        process.join()
    t_end = time.time()
    diff = t_end - t_st
    print(diff)