# -*- encoding: utf-8 -*-

import multiprocessing as mp
import time
from pudb.remote import set_trace


def worker(worker_id):
    """ Simple worker process"""
    i = 0
    while i < 10:
        if worker_id == 1:  # debug process with id 1
            set_trace(term_size=(80, 24))
        time.sleep(1)  # represents some work
        print('In Process {}, i:{}'.format(worker_id, i))
        i = i + 1


if __name__ == '__main__':
    processes = []
    for p_id in range(2):  # 2 worker processes
        p = mp.Process(target=worker, args=(p_id,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()
