import csv

def normalize_url(url):
    segments = url.strip('/').split('/')
    normalized_segments = []
    for segment in segments:
        sub_segments = segment.replace('-', '_').split('_')
        sub_segments.sort()
        normalized_segments.append('_'.join(sub_segments))
    normalized_segments.sort()
    return '/'.join(normalized_segments)

def find_duplicate_urls(csv_file):
    url_dict = {}
    with open(csv_file, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            url = row[2]
            normalized_url = normalize_url(url)
            if normalized_url in url_dict:
                print(f"Duplicate found: {url} and {url_dict[normalized_url]}")
            else:
                url_dict[normalized_url] = url

find_duplicate_urls('csvs/custom_urls_amasty.csv')