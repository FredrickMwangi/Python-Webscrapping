from bs4 import BeautifulSoup


with open('home.html','r') as html_file:
    content = html_file.read()


    soup = BeautifulSoup(content, 'lxml')
    #courses_html_tags = soup.find_all('h5')
    #for course in courses_html_tags:
        #print(course.text)
    phone_cards = soup.find_all('div', class_='card')
    for phone in phone_cards:
        phone_name = phone.h5.text
        phone_price = phone.a.text.split()[-1]

        print(f'{phone_name} costs {phone_price}')
