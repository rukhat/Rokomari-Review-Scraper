from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.minimize_window()
    
    # url = 'https://www.rokomari.com/book/8450/'
    url = 'https://www.rokomari.com/book/206592/'
    
    driver.get(url)

    titles = driver.title.replace(' | Rokomari.com', '').split(' - ')
    Bangla_title = titles[0].split(': ')[0]
    Bangla_author = titles[0].split(': ')[1]
    English_title = titles[1].split(': ')[0]
    English_author = titles[0].split(': ')[1]

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

    data = {'Name': names, 'Review': reviews}
    print(data)

    frame = pd.DataFrame(data)
    file_name = 'Book Reviews.csv'
    frame.to_csv(file_name, header=True, index=False, encoding='utf-8')

    driver.quit()

if __name__ == '__main__':
    main()