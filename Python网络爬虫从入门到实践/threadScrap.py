#coding:utf-8
#简单的多线程爬虫

'''
单线程方式抓取1000个网页
'''
# import requests,time
# link_list = []
# with open('alexa.txt','r') as f:
#     file_list = f.readlines()
#     for each in file_list:
#         link =each.split('\t')[1]
#         link = link.replace('\n','')
#         link_list.append(link)
# start  = time.time()
# for link in range(0,20):
#     try:
#         res = requests.get(link_list[link])
#         print(res.status_code, link_list[link])
#     except requests.ConnectionError as e:
#         print('Error:'+e.args)
# end = time.time()
# print('单线程下载耗时:',end - start)
# #8.63s
'''
threading 多线程方式
'''
# import requests,time,threading
# link_list = []
# proxies = {'http':'10.167.157.112:8118','https':'10.167.157.112:8118'}
# with open('alexa.txt', 'r') as f:
#     file_list = f.readlines()
#     for each in file_list:
#         link = each.split('\t')[1]
#         link = link.replace('\n', '')
#         link_list.append(link)
# start = time.time()
# class downloader(threading.Thread):
#     def __init__(self,url,name):
#         threading.Thread.__init__(self)
#         self.url = url
#         self.name = name
#     def run(self):
#         crawler(self.url, self.name)
# def crawler(url, threadName):
#     try:
#         res = requests.get(url=url, timeout=20, proxies=proxies)
#         print(threadName,res.status_code,url)
#     except requests.ConnectionError as e:
#         print(threadName,'Error:',e.args)
# thread_list = []
# for i in range(1,20):
#     loader = downloader(link_list[i], 'Downloader-'+str(i))
#     loader.start()
#     thread_list.append(loader)
# for _ in thread_list:
#     _.join()
# end = time.time()
# print('Time:',end - start)
'''
使用queue 多线程爬虫
'''
import requests,time,queue,threading
link_list = []
proxies = {'http':'10.167.157.112:8118','https':'10.167.157.112:8118'}
with open('alexa.txt', 'r') as f:
    file_list = f.readlines()
    for each in file_list:
        link = each.split('\t')[1]
        link = link.replace('\n', '')
        link_list.append(link)
start =time.time()
class downloader(threading.Thread):
    def __init__(self,name,q):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
    def run(self):
        while True:
            try:
                crawler(self.name, self.q)
            except:
                break
def crawler(threadName,q):
        url = q.get(timeout=2)
        try:
            r = requests.get(url,timeout=20)
            print(q.qsize(),threadName,r.status_code,url)
        except requests.ConnectionError as e:
            print(threadName,'Error',e.args)

thread_list = ['loader-1','loader-2','loader-3','loader-4','loader-5']
workQueue = queue.Queue(100)
threads =[]
for url in range(0, 100):
    workQueue.put(link_list[url])
for tName in thread_list:
    loader = downloader(tName,workQueue)
    loader.start()
    threads.append(loader)
for t in threads :
    t.join()
end = time.time()
print('Time:',end-start)
