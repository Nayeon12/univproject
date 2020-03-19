from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

print('니트', '스웨터', '가디건', '원피스', '티셔츠', '블라우스', '셔츠', '점퍼', '재킷', '코트', '청바지', '스커트', '레깅스', '바지')
cg1, cg2, cg3 = input("코디하실 옷의 종류를 입력해주세요 : ").split(',')

if cg1 == '니트':
    category = '05'
elif cg1 == '스웨터':
    category = '05'
elif cg1 == '가디건':
    category = '06'
elif cg1 == '원피스':
    category = '07'
elif cg1 == '티셔츠':
    category = '03'
elif cg1 == '블라우스':
    category = '04'
elif cg1 == '셔츠':
    category = '04'
elif cg1 == '점퍼':
    category = '14'
elif cg1 == '재킷':
    category = '15'
elif cg1 == '코트':
    category = '13'
elif cg1 == '청바지':
    category = '09'
elif cg1 == '스커트':
    category = '08'
elif cg1 == '레깅스':
    category = '12'
elif cg1 == '바지':
    category = '10'

if cg2 == '니트':
    category2 = '05'
elif cg2 == '스웨터':
    category2 = '05'
elif cg2 == '가디건':
    category2 = '06'
elif cg2 == '원피스':
    category2 = '07'
elif cg2 == '티셔츠':
    category2 = '03'
elif cg2 == '블라우스':
    category2 = '04'
elif cg2 == '셔츠':
    category2 = '04'
elif cg2 == '점퍼':
    category2 = '14'
elif cg2 == '재킷':
    category2 = '15'
elif cg2 == '코트':
    category2 = '13'
elif cg2 == '청바지':
    category2 = '09'
elif cg2 == '스커트':
    category2 = '08'
elif cg2 == '레깅스':
    category2 = '12'
elif cg2 == '바지':
    category2 = '10'

if cg3 == '니트':
    category3 = '05'
elif cg3 == '스웨터':
    category3 = '05'
elif cg3 == '가디건':
    category3 = '06'
elif cg3 == '원피스':
    category3 = '07'
elif cg3 == '티셔츠':
    category3 = '03'
elif cg3 == '블라우스':
    category3 = '04'
elif cg3 == '셔츠':
    category3 = '04'
elif cg3 == '점퍼':
    category3 = '14'
elif cg3 == '재킷':
    category3 = '15'
elif cg3 == '코트':
    category3 = '13'
elif cg3 == '청바지':
    category3 = '09'
elif cg3 == '스커트':
    category3 = '08'
elif cg3 == '레깅스':
    category3 = '12'
elif cg3 == '바지':
    category3 = '10'

Url = f'https://search.shopping.naver.com/search/category.nhn?pagingIndex=1&pagingSize=40&viewType=list&sort=rel&cat_id=500008{category}&frm=NVSHCAT'
Url2 = f'https://search.shopping.naver.com/search/category.nhn?pagingIndex=1&pagingSize=40&viewType=list&sort=rel&cat_id=500008{category2}&frm=NVSHCAT'
Url3 = f'https://search.shopping.naver.com/search/category.nhn?pagingIndex=1&pagingSize=40&viewType=list&sort=rel&cat_id=500008{category3}&frm=NVSHCAT'

html = urlopen(Url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all(class_='_productLazyImg')
link = soup.find_all(class_='link')
priceSet = soup.find_all("span", class_="num _price_reload")

html2 = urlopen(Url2).read()
soup2 = BeautifulSoup(html2, 'html.parser')
img2 = soup2.find_all(class_='_productLazyImg')
link2 = soup2.find_all(class_='link')
priceSet2 = soup2.find_all("span", class_="num _price_reload")

html3 = urlopen(Url3).read()
soup3 = BeautifulSoup(html3, 'html.parser')
img3 = soup3.find_all(class_='_productLazyImg')
link3 = soup3.find_all(class_='link')
priceSet3 = soup3.find_all("span", class_="num _price_reload")

# 첫번째 옷

namelist1 = []
pricelist1 = []
linklist1 = []

a = 1
for g in img:
    imgUrl = g['data-original']
    with urlopen(imgUrl) as q:
        with open(cg1 + str(a) + '.jpg', 'wb') as x:
            img = q.read()
            x.write(img)
    a += 1

b = 1
for i, h in zip(priceSet, link):
    name = h.text
    price = i.text
    linkUrl = h['href']
    print(cg1 + str(b))
    print(price, "원")
    print(linkUrl)
    print(" ")
    namelist1.append(name)
    pricelist1.append(price)
    linklist1.append(linkUrl)

    b += 1

want1 = input("몇 번 상품이 마음에 드세요?: ")

# 두번째 옷

namelist2 = []
pricelist2 = []
linklist2 = []

c = 1
for j in img2:
    imgUrl2 = j['data-original']
    with urlopen(imgUrl2) as r:
        with open(cg2 + str(c) + '.jpg', 'wb') as y:
            img2 = r.read()
            y.write(img2)
    c += 1

d = 1
for l, k in zip(priceSet2, link2):
    name2 = k.text
    price2 = l.text
    linkUrl2 = k['href']
    print(cg2 + str(d))
    print(price2, "원")
    print(linkUrl2)
    print(" ")
    namelist2.append(name2)
    pricelist2.append(price2)
    linklist2.append(linkUrl2)

    d += 1

want2 = input("몇 번 상품이 마음에 드세요?: ")

# 세번째 옷

namelist3 = []
pricelist3 = []
linklist3 = []

e = 1
for m in img3:
    imgUrl3 = m['data-original']
    with urlopen(imgUrl3) as s:
        with open(cg3 + str(e) + '.jpg', 'wb') as z:
            img3 = s.read()
            z.write(img3)
    e += 1

f = 1
for o, n in zip(priceSet3, link3):
    name3 = n.text
    price3 = o.text
    linkUrl3 = n['href']
    print(cg3 + str(f))
    print(price3, "원")
    print(linkUrl3)
    print(" ")
    namelist3.append(name3)
    pricelist3.append(price3)
    linklist3.append(linkUrl3)

    f += 1

print('다운로드 완료')

want3 = input("몇 번 상품이 마음에 드세요? : ")

firstname = namelist1[int(want1) - 1]
secondname = namelist2[int(want2) - 1]
thirdname = namelist3[int(want3) - 1]

countprice1 = pricelist1[int(want1) - 1]
countprice2 = pricelist2[int(want2) - 1]
countprice3 = pricelist3[int(want3) - 1]

countprice1 = countprice1.replace(",", "")
countprice2 = countprice2.replace(",", "")
countprice3 = countprice3.replace(",", "")

firstlink = linklist1[int(want1) - 1]
secondlink = linklist2[int(want2) - 1]
thirdlink = linklist3[int(want3) - 1]

result = int(countprice1) + int(countprice2) + int(countprice3)

print(" ")
print("첫번째상품", ":", firstname, "/", countprice1, "원")
print(firstlink)
print(" ")
print("두번째상품", ":", secondname, "/", countprice2, "원")
print(secondlink)
print(" ")
print("세번째상품", ":", thirdname, "/", countprice3, "원")
print(thirdlink)
print(" ")

print("모두", result, "원에 구매하실 수 있어요 ! :)")
