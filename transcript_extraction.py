pip install youtube-transcript-api

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, VideoUnavailable

def fetch_transcripts(video_ids):
    transcripts = {}

    for video_id in video_ids:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            transcripts[video_id] = transcript
            print(f"Transcript fetched for video ID: {video_id}")
        except TranscriptsDisabled:
            print(f"Transcripts are disabled for video ID: {video_id}")
            transcripts[video_id] = None
        except VideoUnavailable:
            print(f"Video unavailable for video ID: {video_id}")
            transcripts[video_id] = None
        except Exception as e:
            print(f"Error fetching transcript for video ID: {video_id}: {e}")
            transcripts[video_id] = None

    return transcripts

# Example usage
video_ids = [video["video_id"] for video in video_data]  # Extracted video IDs from BeautifulSoup scraping
transcripts = fetch_transcripts(video_ids)

# Save transcripts to a JSON file
import json
with open("transcripts.json", "w") as file:
    json.dump(transcripts, file, indent=4)
