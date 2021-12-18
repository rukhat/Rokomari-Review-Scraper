from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.minimize_window()
driver.get('https://www.rokomari.com/book/8450/')

# x_path = '//*[@id="summary"]/div[9]/div[3]/div[3]/div[2]/div[2]/p[1]'

# reviews = driver.find_elements_by_xpath('/html/body/div[8]/section[1]/section[2]/div[9]/div[3]/div[3]/div[3]/div[2]/p[1]')

namesRaw = driver.find_elements_by_class_name('name')
reviewsRaw = driver.find_elements_by_class_name('review-text')

names = []
reviews = []

for n in namesRaw:
    if n.text != '':
        names.append(n.text.replace('By ', '').replace(',', ''))

for r in reviewsRaw:
    if r.text != '':
        reviews.append(r.text)

data = {names[i]: reviews[i] for i in range(len(names))}

frame = pd.DataFrame(data)

print(data)
print(frame)

driver.quit()