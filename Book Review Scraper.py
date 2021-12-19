from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd

def main():
    # Installs Google Chrome Driver for Selenium    
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.minimize_window()
    

    # Book URL
    # url = 'https://www.rokomari.com/book/8450/'
    url = 'https://www.rokomari.com/book/206592/'
    driver.get(url)

    # Gets Book Title and Author in Both Bangla and English
    titles = driver.title.replace(' | Rokomari.com', '').split(' - ')
    Bangla_title = titles[0].split(': ')[0]
    Bangla_author = titles[0].split(': ')[1]
    English_title = titles[1].split(': ')[0]
    English_author = titles[0].split(': ')[1]

    # Reviwer Names and Reviews
    names_raw = driver.find_elements_by_class_name('name')
    reviews_raw = driver.find_elements_by_class_name('review-text')

    names = []
    reviews = []

    for n in names_raw:
        if n.text != '':
            names.append(n.text.replace('By ', '').replace(',', ''))

    for r in reviews_raw:
        if r.text != '':
            reviews.append(r.text)

    # Downlaod Cover Image
    cover_image = driver.find_elements_by_class_name('look-inside')
    image_src = cover_image[0].get_attribute('src')
    img = requests.get(image_src)

    image_file = open('Cover Image.jpg', 'wb')
    for chunk in img.iter_content(100000):
        image_file.write(chunk)
    image_file.close()


    # Save as CSV
    data = {'Name': names, 'Review': reviews}
    # print(data)

    frame = pd.DataFrame(data)
    file_name = 'Book Review.csv'
    frame.to_csv(file_name, header=True, index=False, encoding='utf-8')

    driver.quit()

if __name__ == '__main__':
    main()