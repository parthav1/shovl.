import requests
from bs4 import BeautifulSoup

ai_profiles = []
ai_company_names = []
ai_company_ratings = []
ai_company_num_reviews = []
ai_company_prices = []
ai_company_employees = []
ai_company_founded = []
ai_company_locations = []
ai_companies = []

def search_ai():
    # scrapes first 10 pages (most companies after this point have no reviews
    for page_num in range(1, 2):
        #print("page number: " + str(page_num))
        url = "https://www.goodfirms.co/artificial-intelligence?sort_by=1"
        #need to change url slightly for each page past 1
        if page_num > 1:
            url = url + "&page=" + str(page_num)
        response = requests.get(url)

        soup = BeautifulSoup(response.content, 'lxml')
        div_target = soup.find_all('div', class_= 'entity-header-wrapper')

        company_logo_urls = [] # this don't work yet idk to fix lol
        # scrapes for names and profiles
        for item in div_target:
            company_name = item.find('h3').find('a').find('span', itemprop='name')
            # appends actual company name list
            ai_company_names.append(company_name.text)

            company_profile = item.find('h3').find('a')
            # appends list of company profiles
            ai_profiles.append(company_profile.attrs['href'])

            #company_logo_url = item.find('a',class_="company-logo company-image-ling detail_page list-service-profile-visit").find('img')
            #company_logo_urls.append(company_logo_url['src'])

        #print(company_logo_urls)

        # change class for div target
        div_target = soup.find_all('div', class_= 'profile-star-link')

        # scrapes for ratings and number of reviews
        for item in div_target:
            company_rating = item.find('a').find('span', class_='star-container').find('span', class_='fstar')
            # append rating list
            ai_company_ratings.append(company_rating['style'])

            num_reviews = item.find('a').find('span', class_='listinv_review_label')
            # append actual number of reviews list
            ai_company_num_reviews.append(num_reviews.text)

        # change class for div target
        #div_target = soup.find_all('div', class_='firms-services clearfix')
        # scrapes for pricing, employees, date founded, and location
        #for item in div_target:
            #pricing = item.find('div', class_='firm-pricing')
            #ai_company_prices.append(pricing.text)

# an object that will hold the properties of a company
class Company:
    def __init__(self, name, category, rating, num_reviews, review_list):
        print("constructing")
        self.name = name
        self.category = category
        self.rating = rating[6 : len(rating)]
        self.num_reviews = num_reviews
        self.review_list = review_list

# will get the review for any company on the site (not just for ai)
def get_company_reviews(company_profile):

    url = "https://www.goodfirms.co" + str(company_profile) + "#reviews"
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'lxml')
    div_target = soup.find_all('div', class_='entity-review-summary-wrapper', itemprop='description')

    company_reviews = []
    for item in div_target:
        company_reviews.append(item.text.strip())

    return [company_reviews]

search_ai()
for i in range(5):
    company = Company(ai_company_names[i], "AI", ai_company_ratings[i],
                        ai_company_num_reviews[i], get_company_reviews(ai_profiles[i]))
    ai_companies.append(company)

print(ai_companies[0].name)
print(ai_companies[0].rating)
print(ai_companies[0].category)
print(ai_companies[0].review_list[0])