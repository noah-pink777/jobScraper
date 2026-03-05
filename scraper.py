import requests
from bs4 import BeautifulSoup

def scrape_job(url):
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    if response.status_status == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # We grab the body text; you can refine this to specific IDs or Classes
        job_text = soup.get_text(separator=' ', strip=True).lower()
        
        with open("job_description.txt", "w", encoding="utf-8") as f:
            f.write(job_text)
        print("Scrape successful! Content saved to job_description.txt")
    else:
        print(f"Failed to retrieve page. Status code: {response.status_code}")

if __name__ == "__main__":
    target_url = input("Enter the job listing URL: ")
    scrape_job(target_url)
