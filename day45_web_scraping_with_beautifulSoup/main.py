import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
web_page = response.text
# 
soup = BeautifulSoup(web_page, 'html.parser')
movie_lists = []
title_texts = [tag.getText() for tag in soup.find_all(name='h3', class_='title')]
# 另一種列表倒置方法: movie_lists = title_text[::-1] 
for movie in title_texts:
    movie_lists.insert(0,movie)


with open('movie.txt', mode='w', encoding='utf-8') as file:
    try:
        for line in movie_lists:
            file.write(f"{line}\n")
    except UnicodeEncodeError as e:
        print(f"錯誤：寫入檔案 {file} 時發生錯誤：{e}")
    except IOError as e:
        print(f"錯誤：寫入檔案 {file} 時發生IO錯誤：{e}")
    except Exception as e:
        print(f"錯誤：寫入檔案時發生錯誤：{e}")
    finally:
        file.close()

    

