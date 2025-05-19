import requests

url = "http://localhost:5000/upload"
file_path = "sample_data.csv"

with open(file_path, "rb") as f:
    files = {"file": (file_path, f)}
    response = requests.post(url, files=files)

print("✅ Server Response:")
print(response.json())
