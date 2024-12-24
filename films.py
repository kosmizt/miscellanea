import csv
import glob
from collections import Counter

def uniquefilms(folder_path):
    """for merging letterboxd exported data (the lists created by the user).
    it returns the titles alphabetically, counted only once.
    it still has an issue with films of the same name (albeit released in different years) on the same list"""
    film_counter = Counter()
    film_details = {}

    csv_files = glob.glob(f"{folder_path}/*.csv")
    if not csv_files:
        print("no CSV files found in the specified folder.")
        return []

    for file in csv_files:
        with open(file, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            
            for row in reader:
                if not row or len(row) < 1:
                    continue
                if row[0].strip() == "Position":
                    break
            
            for row in reader:
                if not row or len(row) < 4:
                    continue
                
                film_url = row[3].strip() 
                film_name = row[1].strip() 
                film_year = row[2].strip()

                if film_url:  
                    film_counter[film_url] += 1
                    film_details[film_url] = (film_name, film_year)

    unique_films = sorted(
    [(url, details[0], details[1]) for url, details in film_details.items() if film_counter[url] == 1],
    key=lambda film: (film[1].lower(), film[2]))
    
    return unique_films


folder_path = "C:/Users/.../lists" 
unique_films = uniquefilms(folder_path)

if unique_films:
    print("Film list:")
    for film_url, film_name, film_year in unique_films:
        print(f"{film_name} ({film_year}) - {film_url}")
else:
    print("No films found.")


print(f"Number of unique films: {len(unique_films)}")
