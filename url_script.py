from bs4 import BeautifulSoup
html="""
<html><body>
<h1>스크래핑</h1>
<p>웹 페이지 분석</p>
<p>부분 추출</p>
</body></html>
"""
soup=BeautifulSoup(html,'html.parser')
print(soup)

v1=soup.html.body.h1
print(soup.html.body.h1.string)

print(soup.html.body.p.string)

v2=soup.html.body.p
v3=v2.next_sibling.next_sibling
print(v3.string)

v4=soup.h1
print(v4.string)
v5=soup.p
print(v5.string)

print("="*50)

html="""
<html><body>
<h1 id="title">스크래핑</h1>
<p id="mybody>웹 페이지 분석</p>
<p id="mybody2>부분 추출</p>
</body></html>
"""

soup=BeautifulSoup(html,'html.parser')
res=soup.find(id="title")
print(res.string)

print("="*50)

html="""
<html><body>
<ul>
<li><a href="http://naver.com">naver</a></li>
<li><a href="http://daum.net">daum</a></li>
</ul>
</body></html>
"""
soup=BeautifulSoup(html,'html.parser')
links=soup.find_all("a")
print(links)

for a in links:
    href=a.attrs['href']
    text=a.string
    print(text,"=====>",href)

#mw-content-text > div > ul:nth-child(6) > li

url="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
import urllib.request as req
res=req.urlopen(url)
print(res)

soup=BeautifulSoup(res,"html.parser")
print(soup)

title=soup.find("title")
print(title.string)

######################################################################

import requests
from bs4 import BeautifulSoup
USER="dabinii"
PASS="asdf1234@@"

session=requests.session() #세션객체:웹서버에 접속할 수 있도록 해주는것

login_info={
    "m_id":USER,
    "m_passwd":PASS
}
url_login="http://www.hanbit.co.kr/member/login_proc.php"
res=session.post(url_login,login_info)

url_mypage="http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res=session.get(url_mypage)
print(res) #<Response [200]>

soup=BeautifulSoup(res.text,'html.parser')
print(soup)

mileage=soup.select_one("#container > div > div.sm_mymileage > dl.mileage_section1 > dd > span")
print(mileage)

ecoin=soup.select_one("#container > div > div.sm_mymileage > dl.mileage_section2 > dd > span").string
print("이코인:",ecoin)