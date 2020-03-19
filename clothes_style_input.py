import random

# 사용자의 옷 조사하기

print("----- 고객님의 평소 옷 스타일을 조사하겠습니다! -----")
whtop = input("페미닌 스타일과 심플한 스타일 중 어떤 것을 선호하시나요?: ")
whbottom = input("스커트와 바지 중 어떤 것을 선호하시나요?: ")

print(" ")
print("----- 고객님이 가지고 계신 옷의 정보를 입력해주세요! -----")
print('니트', '가디건', '티셔츠', '블라우스', '셔츠', '점퍼', '재킷', '코트', '청바지', '스커트', '바지')
whkind = input("옷의 종류가 무엇인가요?: ")
print('빨강', '주황', '노랑', '연두', '초록', '하늘', '파랑', '남색', '흰색', '검정', '카키', '갈색', '보라', '자주', '분홍', '회색')
whcolor = input("옷의 색깔이 무엇인가요?: ")

print(" ")
print("----- 추천할 때 참고하겠습니다! -----")
print('봄', '여름', '가을', '겨울')
whseason = input("무슨 계절의 옷을 추천드릴까요?: ")

# 옷종류에 따른 추천 카테고리 설정

if whseason == '여름':
    if whkind == '티셔츠':
        if whbottom == '스커트':
            rckind = 'skirt'
        elif whbottom == '바지':
            rckind = 'pants'

    elif whkind == '블라우스' or whkind == '셔츠':
        if whbottom == '스커트':
            rckind = 'skirt'
        elif whbottom == '바지':
            rckind = 'pants'

    elif whkind == '바지' or whkind == '청바지':
        if whtop == '페미닌 스타일':
            rckind = 'blouse'
        elif whtop == '심플한 스타일':
            rckind = 'tshirts'


elif whseason == '겨울':
    if whkind == '니트' or whkind == '티셔츠' or whkind == '블라우스' or whkind == '셔츠':
        ob = input("겉옷과 하의 중 어떤 것을 추천해 드릴까요?: ")
        if ob == '겉옷':
            whouter = input("코트와 점퍼 중 어떤 것을 선호하시나요?: ")
            if whouter == '코트':
                rckind = 'cout'
            elif whouter == '점퍼':
                rckind = 'jumper'

        elif ob == '하의':
            if whbottom == '스커트':
                rckind = 'skirt'
            elif whbottom == '바지':
                rckind = 'pants'

    elif whkind == '스커트' or whkind == '바지':
        if whtop == '페미닌 스타일':
            rckind = 'blouse'
        elif whtop == '심플한 스타일':
            rckind = 'knit'

    elif whkind == '점퍼' or whkind == '코트':
        tb = input("상의와 하의 중 어떤 것을 추천해 드릴까요?: ")
        if ob == '상의':
            if whtop == '페미닌 스타일':
                rckind = 'blouse'
            elif whtop == '심플한 스타일':
                rckind = 'knit'

        elif ob == '하의':
            if whbottom == '스커트':
                rckind = 'skirt'
            elif whbottom == '바지':
                rckind = 'pants'

# 봄, 가을

elif whseason == '봄' or whseason == '가을':
    if whkind == '니트' or whkind == '티셔츠' or whkind == '블라우스' or whkind == '셔츠':
        ob = input("겉옷과 하의 중 어떤 것을 추천해 드릴까요?: ")
        if ob == '겉옷':
            jk = input("재킷과 가디건 중 어떤 것을 추천해 드릴까요?: ")
            if jk == '재킷':
                rckind = 'jacket'
            elif jk == '가디건':
                rckind = 'cd'

        elif ob == '하의':
            if whbottom == '스커트':
                rckind = 'skirt'
            elif whbottom == '바지':
                rckind = 'pants'

    elif whkind == '스커트' or whkind == '바지':
        jt = input("상의와 겉옷 중 어떤 것을 추천해 드릴까요?: ")
        if jt == '상의':
            if whtop == '페미닌 스타일':
                rckind = 'blouse'
            elif whtop == '심플한 스타일':
                rckind = 'knit'

        elif jt == '겉옷':
            jk = input("재킷과 가디건 중 어떤 것을 추천해 드릴까요?: ")
            if jk == '재킷':
                rckind = 'jacket'
            elif jk == '가디건':
                rckind = 'cd'

    else:
        tb = input("상의와 하의 중 어떤 것을 추천해 드릴까요?: ")
        if tb == '상의':
            if whtop == '페미닌 스타일':
                rckind = 'blouse'
            elif whtop == '심플한 스타일':
                wc = input("따뜻하게 입으실래요? 시원하게 입으실래요?: ")
                if wc == '따뜻하게':
                    rckind = 'knit'
                elif wc == '시원하게':
                    rckind = 'tshirts'

        elif tb == '하의':
            if whbottom == '스커트':
                rckind = 'skirt'
            elif whbottom == '바지':
                rckind = 'pants'

# 추천 카테고리에 따른 세부분류

if rckind == 'knit':
    category = '05'
if rckind == 'cd':
    category = '06'
if rckind == 'op':
    category = '07'
if rckind == 'tshirts':
    category = '03'
if rckind == 'blouse':
    category = '04'
if rckind == 'shirts':
    category = '04'
if rckind == 'jumper':
    category = '14'
if rckind == 'jacket':
    category = '15'
if rckind == 'cout':
    category = '13'
if rckind == '청바지':
    category = '09'
if rckind == 'skirt':
    category = '08'
if rckind == 'pants':
    category = '10'

# 색깔 정하긔

if whcolor == '빨강':
    c = random.randrange(3)
    if c == 0:
        rccolor = 'black'
    elif c == 1:
        rccolor = 'white'
    else:
        rccolor = 'navy'
elif whcolor == '주황':
    c = random.randrange(2)
    if c == 0:
        rccolor = 'black'
    else:
        rccolor = 'white'
elif whcolor == '노랑':
    c = random.randrange(3)
    if c == 0:
        rccolor = 'white'
    elif c == 1:
        rccolor = 'brown'
    else:
        rccolor = 'black'
elif whcolor == '연두':
    c = random.randrange(2)
    if c == 0:
        rccolor = 'white'
    else:
        rccolor = 'black'
elif whcolor == '초록':
    c = random.randrange(3)
    if c == 0:
        rccolor = 'white'
    else:
        rccolor = 'black'
elif whcolor == '하늘':
    c = random.randrange(3)
    if c == 0:
        rccolor = 'blue'
    elif c == 1:
        rccolor = 'navy'
    else:
        rccolor = 'black'
elif whcolor == '파랑':
    c = random.randrange(3)
    if c == 0:
        rccolor = 'white'
    elif c == 1:
        rccolor = 'brown'
    else:
        rccolor = 'sky'
elif whcolor == '남색':
    c = random.randrange(4)
    if c == 0:
        rccolor = 'gray'
    elif c == 1:
        rccolor = 'sky'
    elif c == 2:
        rccolor = 'white'
    else:
        rccolor = 'pink'
elif whcolor == '흰색':
    c = random.randrange(4)
    if c == 0:
        rccolor = 'gray'
    elif c == 1:
        rccolor = 'sky'
    elif c == 2:
        rccolor = 'yellow'
    else:
        rccolor = 'black'
elif whcolor == '검정':
    c = random.randrange(3)
    if c == 0:
        rccolor = 'gray'
    elif c == 1:
        rccolor = 'white'
    else:
        rccolor = 'pink'
elif whcolor == '카키':
    c = random.randrange(3)
    if c == 0:
        rccolor = 'white'
    elif c == 1:
        rccolor = 'brown'
    else:
        rccolor = 'black'
elif whcolor == '갈색':
    c = random.randrange(3)
    if c == 0:
        rccolor = 'orange'
    elif c == 1:
        rccolor = 'gray'
    else:
        rccolor = 'khaki'
elif whcolor == '보라':
    c = random.randrange(2)
    if c == 0:
        rccolor = 'black'
    else:
        rccolor = 'white'
elif whcolor == '자주':
    c = random.randrange(3)
    if c == 0:
        rccolor = 'black'
    elif c == 1:
        rccolor = 'white'
    else:
        rccolor = 'gray'
elif whcolor == '분홍':
    c = random.randrange(2)
    if c == 0:
        rccolor = 'black'
    else:
        rccolor = 'navy'
else:
    c = random.randrange(2)
    if c == 0:
        rccolor = 'black'
    else:
        rccolor = 'wine'

if rccolor == 'red':
    color = '16'
elif rccolor == 'orange':
    color = '64'
elif rccolor == 'yellow':
    color = '256'
elif rccolor == 'light green':
    color = '1024'
elif rccolor == 'green':
    color = '2048'
elif rccolor == 'sky':
    color = '4096'
elif rccolor == 'blue':
    color = '8192'
elif rccolor == 'navy':
    color = '16384'
elif rccolor == 'white':
    color = '8'
elif rccolor == 'black':
    color = '1'
elif rccolor == 'khaki':
    color = '512'
elif rccolor == 'brown':
    color = '32'
elif rccolor == 'purple':
    color = '131072'
elif rccolor == 'wine':
    color = '65536'
elif rccolor == 'pink':
    color = '32768'
else:
    color = '2'

sojae1 = 0
sojae2 = 0

# 계절별 소재 설정

if whseason == '여름' and rckind == 'pants':
    sojae1 = '765793'  # 리넨
    sojae2 = '574774'  # 면

if whseason == '여름' and rckind == 'skirt':
    sojae1 = '765793'  # 리넨
    sojae2 = '574774'  # 면

if whseason == '겨울' and rckind == 'pants':
    sojae1 = '574782'  # 모
    sojae2 = '258043'  # 기모

if whseason == '겨울' and rckind == 'skirt':
    sojae1 = '258043'  # 기모
    sojae2 = '669971'  # 울

# 크롤링 준비

from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

MbaseUrl = f'https://search.shopping.naver.com/search/category.nhn?spec=M10012483%7CM10{sojae1}%5EM10012483%7CM10{sojae2}&color={color}&pagingIndex=1&pagingSize=40&viewType=list&sort=rel&cat_id=500008{category}&frm=NVSHATT'
CbaseUrl = f'https://search.shopping.naver.com/search/category.nhn?color={color}&pagingIndex=1&pagingSize=40&viewType=list&sort=rel&cat_id=500008{category}&frm=NVSHCAT'
ptbaseUrl = f'https://search.shopping.naver.com/search/category.nhn?spec=M10013412%7CM10{sojae1}%5EM10013412%7CM10{sojae2}&color={color}&pagingIndex=1&pagingSize=40&viewType=list&sort=rel&cat_id=500008{category}&frm=NVSHATT'

if whkind == '재킷' and whseason == '가을':
    jkinner = random.randrange(2)
    if jkinner == 0:
        print('원피스는 어떠세요?')
        rckind = 'op'


elif whkind == '재킷' and whseason == '봄':
    jkinner = random.randrange(2)
    if jkinner == 0:
        print('원피스는 어떠세요?')
        rckind = 'op'

html = urlopen(ptbaseUrl).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all(class_='_productLazyImg')
link = soup.find_all(class_='link')

html1 = urlopen(MbaseUrl).read()
soup1 = BeautifulSoup(html1, 'html.parser')
img1 = soup1.find_all(class_='_productLazyImg')
link1 = soup1.find_all(class_='link')

html2 = urlopen(CbaseUrl).read()
soup2 = BeautifulSoup(html2, 'html.parser')
img2 = soup2.find_all(class_='_productLazyImg')
link2 = soup2.find_all(class_='link')

# 여름, 바지
# 린넨, 면


if whseason == '여름' and rckind == 'pants':
    k = random.randrange(1, 41)
    n = 1
    for i in img:
        imgUrl = i['data-original']
        n += 1
        if n == k:
            with urlopen(imgUrl) as f:
                with open(rccolor + rckind + str(n) + '.jpg', 'wb') as h:
                    img = f.read()
                    h.write(img)
                    m = 1
                    for j in link:
                        linkUrl = j['href']
                        m += 1
                        if m == k:
                            print(" ")
                            print("이 옷 어떠세요?")
                            print(linkUrl)



# 여름, 치마
# 린넨, 면
elif whseason == '여름' and rckind == 'skirt':
    k = random.randrange(1, 41)
    n = 1
    for i in img1:
        imgUrl = i['data-original']
        n += 1
        if n == k:
            with urlopen(imgUrl) as f:
                with open(rccolor + rckind + str(n) + '.jpg', 'wb') as h:
                    img1 = f.read()
                    h.write(img1)
                    m = 1
                    for j in link1:
                        linkUrl = j['href']
                        m += 1
                        if m == k:
                            print(" ")
                            print("이 옷 어떠세요?")
                            print(linkUrl)



# 겨울, 바지, 모, 기모
elif whseason == '겨울' and rckind == 'pants':
    k = random.randrange(1, 41)
    n = 1
    for i in img:
        imgUrl = i['data-original']
        n += 1
        if n == k:
            with urlopen(imgUrl) as f:
                with open(rccolor + rckind + str(n) + '.jpg', 'wb') as h:
                    img = f.read()
                    h.write(img)
                    m = 1
                    for j in link:
                        linkUrl = j['href']
                        m += 1
                        if m == k:
                            print(" ")
                            print("이 옷 어떠세요?")
                            print(linkUrl)



# 겨울, 치마 , 기모, 울
elif whseason == '겨울' and rckind == 'skirt':
    k = random.randrange(1, 41)
    n = 1
    for i in img1:
        imgUrl = i['data-original']
        n += 1
        if n == k:
            with urlopen(imgUrl) as f:
                with open(rccolor + rckind + str(n) + '.jpg', 'wb') as h:
                    img1 = f.read()
                    h.write(img1)
                    m = 1
                    for j in link1:
                        linkUrl = j['href']
                        m += 1
                        if m == k:
                            print(" ")
                            print("이 옷 어떠세요?")
                            print(linkUrl)


elif rckind == 'jacket' and whseason == '가을':
    k = random.randrange(1, 41)
    n = 1
    for i in img2:
        imgUrl = i['data-original']
        n += 1
        if n == k:
            with urlopen(imgUrl) as f:
                with open(rccolor + rckind + str(n) + '.jpg', 'wb') as h:
                    img2 = f.read()
                    h.write(img2)
                    m = 1
                    for j in link2:
                        linkUrl = j['href']
                        m += 1
                        if m == k:
                            print(" ")
                            print("이 옷 어떠세요?")
                            print(linkUrl)



elif rckind == 'jacket' and whseason == '봄':
    k = random.randrange(1, 41)
    n = 1
    for i in img2:
        imgUrl = i['data-original']
        n += 1
        if n == k:
            with urlopen(imgUrl) as f:
                with open(rccolor + rckind + str(n) + '.jpg', 'wb') as h:
                    img2 = f.read()
                    h.write(img2)
                    m = 1
                    for j in link2:
                        linkUrl = j['href']
                        m += 1
                        if m == k:
                            print(" ")
                            print("이 옷 어떠세요?")
                            print(linkUrl)


else:  # 그 외 상황
    k = random.randrange(1, 41)
    n = 1
    for i in img2:
        imgUrl = i['data-original']
        n += 1
        if n == k:
            with urlopen(imgUrl) as f:
                with open(rccolor + rckind + str(n) + '.jpg', 'wb') as h:
                    img2 = f.read()
                    h.write(img2)
                    m = 1
                    for j in link2:
                        linkUrl = j['href']
                        m += 1
                        if m == k:
                            print(" ")
                            print("이 옷 어떠세요?")
                            print(linkUrl)