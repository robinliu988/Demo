
import requests
import time
import os
import re\

'''请求网页'''
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}

response = requests.get('https://www.vmgirls.com/12985.html',headers = headers)

#response = requests.get('https://www.vmgirls.com/9384.html')

#print(response.request.headers)
#print(response.text)
html = response.text

''' 解析网页 '''
#urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">',html)

dir_name =  re.findall('<h1 class="post-title h3">(.*?)</h1>',html)[-1]
if not os.path.exists(dir_name):
    os.mkdir(dir_name)

urls = re.findall('<a href="(.*?)" alt=".*?" title=".*?">',html)
print(urls)

'''保存图片'''
for url in urls:
    time.sleep(1)
    file_name = url.split('/')[-1]
    print(file_name)
    response = requests.get(url,headers = headers)
    with open(dir_name + '/' + file_name,'wb') as f:
        f.write(response.content)


