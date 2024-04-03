#!/bin/python3
import argparse
import requests
import concurrent.futures

def check_subdomain(subdomain, only_200):
    url = f"http://{subdomain.strip()}"

    try:
        response = requests.get(url, timeout=10)
        if only_200:
            if response.status_code == 200:
                return f"{subdomain.strip()} : {response.status_code}"
            else:
                return None
        else:
            return f"{subdomain.strip()} : {response.status_code}"
    except requests.ConnectionError:
        if only_200:
            return None
        else:
            return f"{subdomain.strip()} : Connection Error"
    except requests.Timeout:
        if only_200:
            return None
        else:
            return f"{subdomain.strip()} : Could not connect (timeout)"
    except requests.RequestException as e:
        if only_200:
            return None
        else:
            return f"{subdomain.strip()} : {str(e)}"


def check_subdomains(file_path, num_threads=50, only_200=False):
    try:
        with open(file_path, 'r') as file:
            subdomains = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = executor.map(lambda subdomain: check_subdomain(subdomain, only_200), subdomains)

    # Filter out None values
    results = [result for result in results if result is not None]

    for result in results:
        print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Check subdomains for HTTP status codes.")
    parser.add_argument("-F", "--file", help="Path to the text file containing subdomains", required=True)
    parser.add_argument("-T", "--threads", type=int, default=50, help="Number of threads (default: 50)")
    parser.add_argument("-O", "--only_200", action="store_true", help="Only output subdomains with status code 200")

    args = parser.parse_args()
    check_subdomains(args.file, args.threads, args.only_200)