import requests
import os
import time

WORDS = ["cat", "dog", "sun", "car", "bus", "bag", "cup", "bed"]
BASE_DIR = "word-builder-game"
IMG_DIR = os.path.join(BASE_DIR, "images")
os.makedirs(IMG_DIR, exist_ok=True)

def fetch_openclipart_image(keyword):
    url = f"https://openclipart.org/search/json/?query={keyword}&amount=5"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['payload']:
            # get first clipart's png URL (usually 512px transparent PNG)
            return data['payload'][0]['svg']['png_thumb']
    return None

print("Fetching clipart images from OpenClipart...")
for word in WORDS:
    print(f" → {word}")
    time.sleep(1)
    img_url = fetch_openclipart_image(word)
    if img_url:
        filename = os.path.join(IMG_DIR, f"{word.upper()}.png")
        try:
            img_data = requests.get(img_url).content
            with open(filename, "wb") as f:
                f.write(img_data)
            print("   ✓ saved")
        except Exception as e:
            print(f"   × failed to save: {e}")
    else:
        print("   × not found")

print("Done!")
