from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.minimize_window()
driver.get('https://www.rokomari.com/book/8450/')

# x_path = '//*[@id="summary"]/div[9]/div[3]/div[3]/div[2]/div[2]/p[1]'


driver.execute_script("document.getElementsByClassName('review-text').style.display = 'none';")
# namesRaw = driver.find_elements_by_class_name('name')
reviewsRaw = driver.find_elements_by_class_name('review-text')
names = []
reviews = []

# for n in namesRaw:
#     if n.text != '':
#         names.append(n.text.replace('By ', '').replace(',', ''))

for r in reviewsRaw:
    if r.text != '':
        reviews.append(r.text)
print(reviews)

# data = {'Name': names, 'Review': reviews}

# frame = pd.DataFrame(data)
# print(frame)
# frame.to_csv('Book Reviews.csv', header=True, index=False, encoding='utf-8')


driver.quit()