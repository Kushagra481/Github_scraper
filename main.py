import requests
from bs4 import BeautifulSoup
import pandas as pd

# List of hackathon URLs
hackathon_urls = [
    "https://duhacks4.devfolio.co/projects",
    "https://zk-online-hackathon-for-web3-builders.devfolio.co/projects",
    "https://formidium-devfest-goa.devfolio.co/projects",
    "https://hackthisfall-virtual.devfolio.co/projects",
    "https://based-africa.devfolio.co/projects",
    "https://based-india.devfolio.coprojects",
    "https://based-sea.devfolio.co/projects",
    "https://based-latam.devfolio.co/projects"
]

def fetch_project_names(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
    response = requests.get(url + "projects", headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        # Modify selector based on actual project title structure
        project_elements = soup.find_all("h3")
        return [project.get_text(strip=True) for project in project_elements]
    else:
        print(f"Failed to retrieve {url}, status code: {response.status_code}")
        return []

all_projects = []
for url in hackathon_urls:
    projects = fetch_project_names(url)
    for project in projects:
        all_projects.append([project])

# Save to CSV
df = pd.DataFrame(all_projects, columns=["Project Name"])
df.to_csv("hackathon_projects.csv", index=False)

print("Dataset saved as hackathon_projects.csv")
