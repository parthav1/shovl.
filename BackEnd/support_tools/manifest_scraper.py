from bs4 import BeautifulSoup
import csv
import requests
import argparse
from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("data", help="Path to datafile to append output", type=str)
    parser.add_argument("category", help="What category to scrape for (software, web-dev, cybersecurity, etc.)", type=str)
    parser.add_argument("-p", "--pages", help="How many pages to scrape. WARNING: out of bounds will cause scraped data loss.", type=int, default=-1)

    args = parser.parse_args()
    return args

def search_manifest(data_path, category, pages=int):
    companies = {}
    url = f'https://themanifest.com/{category}/companies'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    total_pages = pages
    if pages == -1:
        pagination = soup.find('nav', {'aria-label': 'Page navigation'})
        pages = pagination.find('li', {'class': 'page-item last'})
        total_pages = int(pages.find('a')['data-page']) 
    
    for page in tqdm(range(0, total_pages + 1)):

        url = f'https://themanifest.com/{category}/companies?page={page}'
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'html.parser')
        target = soup.select('li.provider-card.sponsored, li.provider-card')
        for item in target:
            company_name = item.find('div', class_='provider-card__intro').find('div', class_='provider-card__header provider-header').find('h3').find('a').text
            rating_target = item.find('div', class_='provider-card__intro').find('div', class_='provider-rating')
            companies[(company_name.strip())] = {
                'category' : category,
                'description' : '',
                'overall_rating' : '',
                'review_count' : '',
                'clients' : [],
                'notable_project' : '',
                'industries' : '',
                'min_project_size' : '',
                'location' : '',
                'company_size' : ''
            }
            try:
                description = item.find('div', class_='provider-card__body').find('div', class_='provider-summary').find('p').text
                companies[(company_name.strip())]['description'] = description
            except AttributeError:
                pass

            try:
                overall_rating = rating_target.find('div', class_='provider-rating__overall').find('span').text
                companies[(company_name.strip())]['overall_rating'] = overall_rating
            except AttributeError:
                pass

            try:
                review_count = rating_target.find('div', class_='provider-rating__overall').find('div', class_='provider-rating__overall-heading').find('p').text
                companies[(company_name.strip())]['review_count'] = review_count
            except AttributeError:
                pass

            try:
                clients = [client.text for client in (item.find('div', class_='provider-card__body').find('div', class_='provider-card__columns').find('div', class_='provider-card__columns-item provider-clients').find('ul', class_='provider-clients__list').find_all('li'))]
                companies[(company_name.strip())]['clients'] = clients
            except AttributeError:
                pass

            try:
                notable_project = item.find('div', class_='provider-card__body').find('div', class_='provider-notable').find('div', class_='provider-notable__text').find('p').text
                companies[(company_name.strip())]['notable_project'] = notable_project
            except AttributeError:
                pass

            try:
                industries = [industry.get('aria-label') for industry in  (item.find('div', class_='provider-card__body').find('div', class_='provider-card__columns').find('div', class_='provider-card__columns-item provider-card__industries provider-industries').find('ul', class_='provider-industries__list').find_all('li'))]
                companies[(company_name.strip())]['industries'] = industries
            except AttributeError:
                pass

            try: 
                details = item.find('div', class_='provider-card__body').find('ul', class_='provider-card__details provider-details').find_all('li')

                for detail in details:
                    label = detail['aria-label']
                    if label == 'Budget':
                        budget = detail.find('span').text
                        companies[(company_name.strip())]['min_project_size'] = budget
                    if label == 'Employees':
                        employees = detail.find('span').text
                        companies[(company_name.strip())]['company_size'] = employees
                    if label == 'Location':
                        location = detail.find('span').find('span', class_='locality').text
                        companies[(company_name.strip())]['location'] = location
            except AttributeError:
                pass

    with open(data_path, mode='a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)

        for company_name, data in companies.items():
            writer.writerow([
                company_name.strip(),
                data.get('category', ''),
                data.get('description', ''),
                data.get('overall_rating', ''),
                data.get('review_count', ''),
                '; '.join(data.get('clients', [])),
                data.get('notable_project', ''),
                data.get('industries', ''),
                data.get('location', ''),
                data.get('company_size', ''),
                data.get('min_project_size', '')
            ])

def main():
    search_manifest(parse_args().data,
                    parse_args().category,
                    parse_args().pages)
    
if __name__ == "__main__":
    main()