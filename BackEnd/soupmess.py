# Why did you choose BeautifulSoup?
# It's lightweight, fast, and simple
# Our main goal is to literally google and get the top results and print out their info
# That's simple shit. The harder part is putting some spin on it that'll impress

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

    # we're gonna use google as our main engine and search it with the requests library
    # Then we search it up and the response var has all of it
    url = "https://www.google.com/search"
    params = {    # HOW do we get rid of those "top 10" search results? That's the "engineering here". Put in AI
        "q" : search_query + " vendors",
        "num" : int(desired_results)
    }
    response = requests.get(url, params=params)


    # Now use beautsoup to parse through all the HTML of the search page (which is much easier to do this in BS)
    # DOESNT WORK. search_results turns out to be empty and i've been stuck on this for 3 hrs
    search_result_class = "g"
    soup = BeautifulSoup(response.content, "html.parser")
    search_results = soup.find_all("div", class_=search_result_class)

    top_urls = []
    for result in search_results:
        link = result.find("a")
        if link:
            href = link.get("href")
            if href.startswith("/url?q="):
                url = href[7:].split("&")[0]
                top_urls.append(url)

    for url in top_urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        company_name = soup.find("h1").text.strip()
        location = soup.find("div", class_="location").text.strip()
        products = [p.text.strip() for p in soup.find_all("li", class_="product")]
        # log the vendor info
        print(f"Company Name: {company_name}")
        print(f"Location: {location}")
        print(f"Products/Services: {', '.join(products)}")

def main():
    search(parse_args().query,
           parse_args().result_count)
    
if __name__ == "__main__":
    main()
