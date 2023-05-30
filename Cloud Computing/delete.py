import requests

API_URL = "https://imgapi-66o65w2gbq-et.a.run.app"  # Update with your local server URL

filename = "img1.jpg"  # Specify the filename of the image to delete

data = {"filename": filename}
response = requests.post(f"{API_URL}/delete", data=data)

print(response.json())

