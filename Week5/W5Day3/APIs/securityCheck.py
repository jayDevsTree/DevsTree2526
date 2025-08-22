
import requests
import time

def safe_request(url, max_attempts=3, delay=2, timeout=5):
    for attempt in range(1, max_attempts + 1):
        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()   # will raise HTTPError if not 200
            return response.json()
        
        except requests.HTTPError as e:
            print(f"[Attempt {attempt}] HTTP Error: {e}")
        
        except requests.ConnectionError as e:
            print(f"[Attempt {attempt}] Connection Error: {e}")
        
        except requests.Timeout as e:
            print(f"[Attempt {attempt}] Timeout Error: {e}")
        
        except requests.RequestException as e:
            print(f"[Attempt {attempt}] General Request Error: {e}")

        if attempt < max_attempts:
            time.sleep(delay)

    return None  # if all attempts fail