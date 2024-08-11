import requests
from bs4 import BeautifulSoup
import json

def crawl_techcrunch_ai_news():
    base_url = "https://techcrunch.com/category/artificial-intelligence/"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.content, "html.parser")

    news_items = soup.find_all("a", {"class": "post-block__title__link"})

    news_data = []
    urls = []  # Separate list to store just the URLs

    for item in news_items:
        title = item.text.strip()
        url = item["href"]
        urls.append(url)  # Save the URL to the separate list

        author, published_date = extract_details(url)
        news_data.append({
            "title": title,
            "url": url,
            "author": author,
            "published_date": published_date
        })

    return news_data, urls

def extract_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    author = soup.find("div", {"class": "article__byline"})
    author = author.find("a")
    author = author.text.strip() if author else "N/A"

    tt = soup.find("span", class_="article__byline__meta")
    time_tag = tt.find("time", class_="full-date-time")
    separator_tag = time_tag.find("span", class_="full-date-time__separator")

    published_date = separator_tag.text.strip() if published_date else "N/A"

    return author, published_date

def save_to_json(news_data, urls):
    # Saving the scraped data to a JSON file
    with open("ai_news.json", "w") as json_file:
        json.dump(news_data, json_file, indent=2)

    # Saving the URLs to a separate JSON file
    with open("ai_news_urls.json", "w") as json_file:
        json.dump(urls, json_file, indent=2)

if __name__ == "__main__":
    # Crawl and scrape the AI news from TechCrunch
    news_data, urls = crawl_techcrunch_ai_news()
    
    # Save the scraped data and URLs to separate JSON files
    save_to_json(news_data, urls)
