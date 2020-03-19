from urllib.request import urlopen
# from urllib.parse import quote_plus
from bs4 import BeautifulSoup

print('니트', '스웨터', '가디건', '원피스', '티셔츠', '블라우스', '셔츠', '점퍼', '재킷', '코트', '청바지', '스커트', '레깅스', '바지')

cg = input("원하는 옷의 카테고리가 무엇인가요?: ")  # 사용자로 부터 옷 종류 입력받기


categoty = 0

# 옷 종류에 따라 Url 성분 바꿔주기
if cg == '니트':
    category = '05'
elif cg == '스웨터':
    category = '05'
elif cg == '가디건':
    category = '06'
elif cg == '원피스':
    category = '07'
elif cg == '티셔츠':
    category = '03'
elif cg == '블라우스':
    category = '04'
elif cg == '셔츠':
    category = '04'
elif cg == '점퍼':
    category = '14'
elif cg == '재킷':
    category = '15'
elif cg == '코트':
    category = '13'
elif cg == '청바지':
    category = '09'
elif cg == '스커트':
    category = '08'
elif cg == '레깅스':
    category = '12'
elif cg == '바지':
    category = '10'

Url = f'https://search.shopping.naver.com/search/category.nhn?pagingIndex=1&pagingSize=40&viewType=list&sort=rel&cat_id=500008{category}&frm=NVSHCAT'

html = urlopen(Url).read()
soup = BeautifulSoup(html, 'html.parser')
img = soup.find_all(class_='_productLazyImg')
link = soup.find_all(class_='link')

n = 1
for i in img:
    imgUrl = i['data-original']
    with urlopen(imgUrl) as f:
        with open(cg + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n += 1

m = 1
for k in link:
    linkUrl = k['href']
    print(cg + str(m))
    print(linkUrl)
    m += 1

print('다운로드 완료')
