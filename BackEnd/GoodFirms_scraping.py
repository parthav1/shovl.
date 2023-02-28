import requests
from bs4 import BeautifulSoup
import csv
import time
import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("data", help="Path to datafile to append output", type=str)
    parser.add_argument("category", help="What category to scrape for (software, web-dev, cybersecurity, etc.)",
                        type=str)

    args = parser.parse_args()
    return args

def get_company_reviews(company_profile):

    url = "https://www.goodfirms.co" + str(company_profile) + "#reviews"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'lxml')
    div_target = soup.find_all('div', class_='entity-review-summary-wrapper', itemprop='description')

    company_reviews = []
    for item in div_target:
        company_reviews.append(item.text.strip())

    return [company_reviews]

def searchGoodFirms(category, data_path):
    companies = {}
    for page in range(1, 2):
        url = "https://www.goodfirms.co/" + category + "?sort_by=1"
        if page > 1:
            url = url + "&page=" + str(page)

        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'lxml')

        target = soup.find_all('li', class_= 'service-provider')
        count = 1
        for item in target:
            print(count)
            count += 1
            company_name = item.find('div', class_= 'entity-header-wrapper').find('h3').find('a').\
                find('span', itemprop='name').text
            print(company_name)
            companies[(company_name.strip())] = {
                'category': category,
                'profile': '',
                'reviews': '',
                'price': '',
                'date_founded': ''
            }

            try:
                profile = item.find('div', class_='profile-flex').find('p').find('a').attrs['href']
                companies[(company_name.strip())]['profile'] = profile
            except AttributeError:
                pass
            #print(profile)

            reviews = get_company_reviews(profile)
            #print(reviews)

            price = item.find('div', class_= 'firm-pricing').text
            #print(price)

            date_founded = item.find('div', class_= 'firm-founded')

            companies[(company_name.strip())]['profile'] = reviews
            companies[(company_name.strip())]['reviews'] = reviews
            companies[(company_name.strip())]['price'] = price
            companies[(company_name.strip())]['date_founded'] = date_founded

            time.sleep(8)

            with open(data_path, mode='a', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                for company_name, data in companies.items():
                    writer.writerow([
                        company_name.strip(),
                        data.get('category', ''),
                        data.get('price'),
                        data.get('date_founded'),
                        '; '.join(data.get('reviews', []))
                    ])


def main():
    searchGoodFirms("big-data-analytics", parse_args().data)
    #searchGoodFirms("artificial-intelligence", parse_args().data)
    #searchGoodFirms("it-services", parse_args().data)
    #searchGoodFirms("cloud-computing-companies", parse_args().data)
    #searchGoodFirms("augmented-virtual-reality", parse_args().data)
    #searchGoodFirms("internet-of-things", parse_args().data)
    #searchGoodFirms("ecommerce-development-companies", parse_args().data)

if __name__ == "__main__":
    main()