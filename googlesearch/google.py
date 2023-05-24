import webbrowser
from googlesearch import search

# 구글 검색창에 검색했을 때 몇번째로 나오는 창 열기 프로그램
def search_and_open(keyword, position):
    query = keyword
    count = 0

    for url in search(query, num_results=10):
        count += 1
        if count == position:
            webbrowser.open_new_tab(url)
            break

search_and_open("loskd", 5)
