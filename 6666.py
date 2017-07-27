import requests
from bs4 import BeautifulSoup
import bs4
 
def getHTMLText(url):
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text


def fillUnivList (html):
    a1=[]
    a2=[]
    a3=[]
    a4=[]
    a5=[]
    soup = BeautifulSoup(html, "html.parser")
    for span in soup.select('.hangyespan'):
          a1.append(span.string)
    for span2 in soup.select('.guowaicityspan'):
          a2.append(span2.string)
    for span3 in soup.select('.guowaitime'):
          a3.append(span3.string)
    for A1 in soup.select('#sets_div01 a'):
           a4.append(A1.get('href'))
           a5.append(A1.text.strip())
    tplt = "{:^5}\t{:^5}\t{:^5}\t{:^5}\t{:^5}"      
    for i in range(len(a1)):
        print(tplt.format(a1[i],a2[i],a3[i],a4[i],a5[i],chr(12288)))
    n=len(a1)
    print("本月展会次数为：",n)   
    return n

def main():
     url1= 'http://www.eshow365.com/guonei/date-201701.html'
     url2= 'http://www.eshow365.com/guonei/date-201702.html'
     url3= 'http://www.eshow365.com/guonei/date-201703.html'
     url4= 'http://www.eshow365.com/guonei/date-201704.html'
     url5= 'http://www.eshow365.com/guonei/date-201705.html'
     url6= 'http://www.eshow365.com/guonei/date-201706.html'
     url7= 'http://www.eshow365.com/guonei/date-201707.html'
     url8= 'http://www.eshow365.com/guonei/date-201708.html'
     url9= 'http://www.eshow365.com/guonei/date-201709.html'
     url10= 'http://www.eshow365.com/guonei/date-201710.html'
     url11= 'http://www.eshow365.com/guonei/date-201711.html'
     url12= 'http://www.eshow365.com/guonei/date-201712.html'
     tplt = "{:^5}\t{:^5}\t{:^5}\t{:^10}\t{:^10}"
     print(tplt.format("所属行业","   地点","      时间","                事件链接                        ","                       展会名称",chr(12288)))
     html = getHTMLText(url1)
     fillUnivList(html)
     n=fillUnivList(html)
     html = getHTMLText(url2)
     fillUnivList(html)
     n+=fillUnivList(html)
     html = getHTMLText(url3)
     fillUnivList(html)
     n+=fillUnivList(html)
     html = getHTMLText(url4)
     fillUnivList(html)
     n+=fillUnivList(html)
     html = getHTMLText(url5)
     fillUnivList(html)
     n+=fillUnivList(html)
     html = getHTMLText(url6)
     fillUnivList(html)
     n+=fillUnivList(html)
     html = getHTMLText(url7)
     fillUnivList(html)
     n+=fillUnivList(html)
     html = getHTMLText(url8)
     fillUnivList(html)
     n+=fillUnivList(html)
     html = getHTMLText(url9)
     fillUnivList(html)
     n+=fillUnivList(html)
     html = getHTMLText(url10)
     fillUnivList(html)
     n+=fillUnivList(html)
     html = getHTMLText(url11)
     fillUnivList(html)
     n+=fillUnivList(html)
     html = getHTMLText(url12)
     fillUnivList(html)
     n+=fillUnivList(html)
     print("本年展会总次数为:",n)
  
    
main()
