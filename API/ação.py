import requests
 
url = "https://brapi.dev/api/available"
params = {
    'search': 'TR',
    'token': 'eJGEyu8vVHctULdVdHYzQd',
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Request failed with status code {response.status_code}")