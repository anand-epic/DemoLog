import requests

def main():
    for i in range(1,40):
        requests.get("http://localhost:8000/demoLog")


if __name__ == "__main__":
    main()