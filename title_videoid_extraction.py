import requests
from bs4 import BeautifulSoup

def scrape_youtube(query, max_results=10):
    search_url = f"https://www.youtube.com/results?search_query={query}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    videos = []
    for script_tag in soup.find_all("script"):
        if "ytInitialData" in script_tag.text:
            # Extract JSON-like data embedded in JavaScript
            raw_data = script_tag.string
            start_index = raw_data.find("ytInitialData") + len("ytInitialData") + 3
            end_index = raw_data.find("};", start_index) + 1
            yt_data = raw_data[start_index:end_index]

            # Process the JSON
            import json
            data = json.loads(yt_data)
            video_items = data['contents']['twoColumnSearchResultsRenderer']['primaryContents'][
                'sectionListRenderer']['contents'][0]['itemSectionRenderer']['contents']
            for item in video_items:
                if 'videoRenderer' in item:
                    video_id = item['videoRenderer']['videoId']
                    title = item['videoRenderer']['title']['runs'][0]['text']
                    videos.append({'video_id': video_id, 'title': title})
                    if len(videos) >= max_results:
                        break
            break
    return videos

# Example usage
video_data = scrape_youtube("technology", max_results=5)
print(video_data)
