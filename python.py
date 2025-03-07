import requests
import json
import random

def fetch_all_vacancies():
    url = "https://api-rbb.fhcibumn.id/general/career/list-vacancy"
    headers = {"Content-Type": "application/json"}  # Modify if authentication is required

    page = 1
    size = 10
    all_data = []

    while True:
        payload = {
            "page": page,
            "size": size,
            "job_title": "",
            "stream_id": [],
            "company_id": [],
            "experience_level": ["fresh_graduate"],
            "education_level": [],
            "major_id": ["a1981247-4e50-42b0-aa2a-afdb65638ceb"],
            "search": ""
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 201:
            data = response.json()
            if "data" in data and isinstance(data["data"], list):
                all_data.extend(data["data"])
                if len(data["data"]) < size:
                    break  # Stop if this is the last page
                page += 1
            else:
                break  # Stop if no more data is available
        else:
            print(f"Error: {response.status_code}, {response.text}")
            break

    return all_data

def save_to_file(vacancies, filename="vacancies.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(vacancies, file, indent=4, ensure_ascii=False)
    print(f"Data saved to {filename}")

def display_vacancies(vacancies):
    print(f"Total Vacancies Fetched: {len(vacancies)}\n")
    for job in vacancies:
        print(f"Title: {job['title']}")
        print(f"Company: {job['company_name']}")
        print(f"Employment Status: {job['employment_status']}")
        print(f"Experience Level: {job['experience_level']}")
        print(f"Stream: {job['stream_name']}")
        print(f"Total Quota: {job['total_quota']}")
        print("-" * 50)

if __name__ == "__main__":
    vacancies = fetch_all_vacancies()
    filename = f"vacancies_{len(vacancies)}_{random.randint(1, 10)}.json"  # Includes length and random number
    save_to_file(vacancies, filename)
    display_vacancies(vacancies)

