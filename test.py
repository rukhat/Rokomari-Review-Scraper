import requests
import re

def main():    
    # page = requests.get('https://www.rokomari.com/book/8450/')
    # page.raise_for_status()

    # raw = page.text

    # print(len(raw))

    book_file = open('test_file.html', 'r')

    print(book_file.read())
    
    # for chunk in page.iter_content(10000):
    #     book_file.write(chunk)
    # book_file.close()
    
    # pattern = re.compile(r'(?<=review-text review-text--full js--review-full)(.*)(?=</p>)')
    
    # for line in open('Test File.txt'):
    #     for match in re.finditer(pattern, line):
    #         print(match.group())

    # reviews = pattern.search(raw)

    # print(reviews)

    
if __name__ == '__main__':
    main()
