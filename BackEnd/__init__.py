from bs4 import BeautifulSoup
import requests
import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("query", help="Name of the technology", type=str)
    parser.add_argument("-r", "--result-count", help="How many results to output. Default is 10", type=int, default=10)

    args = parser.parse_args()
    return args

def search(search_query,
           desired_results):
    
    search_query.replace(' ', '+')
    url = "https://clutch.co/"
    

def main():
    search(parse_args().query,
           parse_args().result_count)
    
if __name__ == "__main__":
    main()


# def search__depreciated__(search_query, 
#            desired_results):

#     search_query.replace(' ', '+')
#     url = "https://www.goodfirms.co/search?query=" + search_query
#     response = requests.get(url)

#     soup = BeautifulSoup(response.content, 'html.parser')
#     div_target = soup.find_all('div', class_= 'company-info-title pull-left')

#     company_names = []
#     for item in div_target:
#         company_name = item.find('h3').find('a')['title']
#         company_names.append(company_name.strip())

#     print(company_names)
