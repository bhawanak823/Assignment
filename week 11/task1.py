import requests

def fetch_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print("\nHere’s a random Chuck Norris joke:")
            print(data['value'])
    except requests.exceptions.RequestException as e:
        print("Sorry, couldn't fetch a joke right now. Please try again later.")
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_chuck_norris_joke()