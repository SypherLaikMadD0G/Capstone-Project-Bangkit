import requests

url = 'https://imgapi-66o65w2gbq-et.a.run.app/upload'  # Replace with your server URL

# ID token obtained from authentication
id_token = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjJkM2E0YTllYjY0OTk0YzUxM2YyYzhlMGMwMTY1MzEzN2U5NTg3Y2EiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vY2Fwc3RvbmUtbnV0cmlzZWUiLCJhdWQiOiJjYXBzdG9uZS1udXRyaXNlZSIsImF1dGhfdGltZSI6MTY4NTI4NTAwOCwidXNlcl9pZCI6IkZUOUswRzJSV0FXcjlZOVZtc3VCMGpiUWsxYTIiLCJzdWIiOiJGVDlLMEcyUldBV3I5WTlWbXN1QjBqYlFrMWEyIiwiaWF0IjoxNjg1Mjg1MDA4LCJleHAiOjE2ODUyODg2MDgsImVtYWlsIjoiZXhhbXBsZUBleGFtcGxlLmNvbSIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJleGFtcGxlQGV4YW1wbGUuY29tIl19LCJzaWduX2luX3Byb3ZpZGVyIjoiY3VzdG9tIn19.HuwXXDUF4rltZXqou5f0_tTsTy_IxI9Y_AP4S3L4qeiXXiLSuOleIx66KKISLGfPUhJjfvU7MsMsfonEj2Yyo3F6a6B8FQnip1ZeGa4JhhW3Fr1fiJlNqmfJ5x3GPhPmRz2E0cEZpHV-58AwL2wjHU2wm1ICO18QEc4s9eXAA3fsm9EJGuSpu5VCRyHLxNSEU3QqRk6rSXW9ztGG22dLVQ1fF5frB_1Ujw3oHcklCHI45uPQLVVGT89PJ9N1wNJoAVP1_ZUz-a7a9tFUqk7y8QQn3rXbjVHUe_iAbur4TjvNWmtG5NJypeIAInEtYo3Y-cQXqNeLm1pLjeOuEoUybg'

# Upload image to user UID folder
image_url = 'img1.jpg'  # Replace with the path to the image file
headers = {'Authorization': id_token}
files = {'photo': open(image_url, 'rb')}
response = requests.post(url, headers=headers, files=files)

if response.status_code == 200:
    response_data = response.json()
    if 'error' in response_data:
        print('Image upload error:', response_data['error'])
    else:
        print('Image uploaded successfully')
else:
    print('Image upload error:', response.text)
