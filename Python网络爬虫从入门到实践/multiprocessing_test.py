#coding:utf-8
'''
multiprocessing 像线程一样管理进程
'''
# from multiprocessing import cpu_count
# print(cpu_count())
'''
使用进程
'''
from multiprocessing import Process,Queue
import time,requests
link_list = []
proxies = {'http': '10.167.157.112:8118', 'https': '10.167.157.112:8118'}
with open('alexa.txt', 'r') as f:
    file_list = f.readlines()
    for each in file_list:
        link = each.split('\t')[1]
        link = link.replace('\n', '')
        link_list.append(link)
start = time.time()

class MyProcess(Process):
    def __init__(self,q):
        Process.__init__(self)
        self.q = q
    def run (self):
        while not self.q.empty():
            crawler(self.q)
def crawler(q):
    url = q.get(timeout = 2)
    try:
        r = requests.get(url,timeout=20,proxies=proxies)
        print(q.qsize(),r.status_code,url)
    except requests.ConnectionError as e:
        print(q.qsize(),'Error:',e.args)
def main():
    ProcessNames = ['process-1', 'process-2', 'process-3']
    workqueue = Queue(100)
    for url in range(0,100):
        workqueue.put(link_list[url])
    for i in range(0,3) :
        p = MyProcess(workqueue)
        p.daemon = True
        p.start()
        p.join()
    end = time.time()
    print('Time:',end -start)
if __name__ == '__main__':
    main()
