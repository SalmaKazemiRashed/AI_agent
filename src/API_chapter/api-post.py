import requests

url = "https://jsonplaceholder.typicode.com/posts"

order = {
    "customer": "Ayne",
    "Product" : "laptop",
    "quantity": 2,
    "price": 3500
}

response = requests.post(url, json=order)

if response.status_code == 201: ## success
    data = response.json()
    print("Order has been registered")
    print("Server response")
    print(data)
else:
    print('Error:',response.status_code)