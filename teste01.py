import requests

def test_requests():
    try:
        response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()  # Parse the JSON response
        print("Request successful!")
        print("Status code:", response.status_code)
        print("Response data:", data)
    except requests.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    test_requests()
