import requests

def header_analyzer(url="https://google.com"):
    try:
        r = requests.get(url, timeout=5)

        print(f"\n{'='*40}")
        print(f"URL: {url}")
        print(f"Status: {r.status_code}")

        print("---- Headers ----")
        for key, val in r.headers.items():
            print(f"{key}: {val}")

        # Security Header Check
        print(f"\n---- Security Headers ----")
        security = [
            "Strict-Transport-Security",
            "Content-Security-Policy",
            "X-Frame-Options"
        ]

        for h in security:
            if h in r.headers:
                print(f"{h} is present")
            else:
                print(f"{h} is missing")

    except Exception as e:
        print(f"Error: {e}")