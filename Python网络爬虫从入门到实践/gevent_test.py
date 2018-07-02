#coding:utf-8
#协程爬虫
'''
高并发 扩展性强， 不适合IO操作
'''
import gevent
from gevent.queue import Queue,Empty
import time,requests
from gevent import monkey#把下面有可能的IO操作单独做标记
monkey.patch_all()#将IO转为异步执行的函数
link_list = []
proxies = {'http': '10.167.157.112:8118', 'https': '10.167.157.112:8118'}
with open('alexa.txt', 'r') as f:
    file_list = f.readlines()
    for each in file_list:
        link = each.split('\t')[1]
        link = link.replace('\n', '')
        link_list.append(link)
start = time.time()
workQueue = Queue(1000)
def crawler(index):
    process_id = 'Process-'+str(index)
    while not workQueue.empty():
        url = workQueue.get(timeout=2)
        try:
            r = requests.get(url,timeout=20,proxies=proxies)
            # with open('info.txt','a+') as f:
            #     f.write(str(process_id +' '+ workQueue.qsize()+' '+r.status_code+' '+url+'\n'))
            print(process_id,workQueue.qsize(),r.status_code,url)
        except requests.ConnectionError as e:
            print(process_id,workQueue.qsize(),'Error:',e.args)
def boss():
    for url in link_list:
        workQueue.put_nowait(url)
def main():
    gevent.spawn(boss).join()
    jobs =[]
    for i in range(10):
        jobs.append(gevent.spawn(crawler,i))
    gevent.joinall(jobs)
    end = time.time()
    print('Time:',end -start)

if __name__ == '__main__':
    main()
