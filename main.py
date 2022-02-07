from bs4 import BeautifulSoup
with open('home.html', 'r') as html_file
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    content_reviews = soup.find_all('desired_link', '')
    for review in content_reviews
        review_site = review.text