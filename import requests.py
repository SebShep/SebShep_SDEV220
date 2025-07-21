import requests

# List all books
resp = requests.get("http://127.0.0.1:5000/books")
print("All books:", resp.json())

# Get book #1
resp = requests.get("http://127.0.0.1:5000/books/1")
print("Book 1:", resp.json())
