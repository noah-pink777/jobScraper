import csv

def analyze_jobs():
    print(f"{'URL':<50} | {'Match Count':<12} | {'Skills Found'}")
    print("-" * 100)

    try:
        with open('jobs.csv', 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row: continue
                url, skills_string = row[0], row[1]
                
                # Turn the string back into a Python array/list
                skills_array = [s.strip() for s in skills_string.split(',') if s.strip()]
                
                # Truncate URL for cleaner printing
                display_url = (url[:47] + '..') if len(url) > 50 else url
                print(f"{display_url:<50} | {len(skills_array):<12} | {', '.join(skills_array)}")
                
    except FileNotFoundError:
        print("jobs.csv is empty. Run the scraper first!")

if __name__ == "__main__":
    analyze_jobs()
