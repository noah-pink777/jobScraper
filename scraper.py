import requests
from bs4 import BeautifulSoup
import csv

def get_skills_list():
    """Load the skills we care about from skills.txt"""
    try:
        with open('skills.txt', 'r') as f:
            return [line.strip().lower() for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: skills.txt not found.")
        return []

def scrape_and_find(url):
    skills_to_check = get_skills_list()
    if not skills_to_check: return

    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        page_text = soup.get_text(separator=' ', strip=True).lower()

        # Create an array of matches for THIS specific job
        found_in_this_job = [skill for skill in skills_to_check if skill in page_text]

        # Save the result as a new row in jobs.csv
        with open('jobs.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            # We store the array as a comma-separated string inside the CSV cell
            writer.writerow([url, ", ".join(found_in_this_job)])
        
        print(f"Done! Found {len(found_in_this_job)} skills. Added to jobs.csv")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    target = input("Enter Job URL: ")
    scrape_and_find(target)
