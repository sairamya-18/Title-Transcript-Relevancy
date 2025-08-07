def combine_metadata_and_transcripts(video_data, transcripts):
    combined_data = []

    for video in video_data:
        video_id = video["video_id"]
        video_title = video["title"]
        transcript = transcripts.get(video_id, "No transcript available.")
        combined_data.append({
            "video_id": video_id,
            "title": video_title,
            "transcript": transcript
        })

    return combined_data

# Example usage
combined_data = combine_metadata_and_transcripts(video_data, transcripts)

# Save to a JSON file
with open("combined_data.json", "w") as file:
    json.dump(combined_data, file, indent=4)
import csv

def save_to_csv(combined_data, output_file):
    # Open the CSV file for writing
    with open(output_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(["Video ID", "Title", "Transcript"])

        # Write each video's data
        for video in combined_data:
            video_id = video["video_id"]
            title = video["title"]

            # Format the transcript as plain text (if available)
            if isinstance(video["transcript"], list):
                transcript_text = "\n".join([entry["text"] for entry in video["transcript"]])
            else:
                transcript_text = video["transcript"]

            writer.writerow([video_id, title, transcript_text])

# Example usage
save_to_csv(combined_data, "video_transcripts.csv")
print("Data saved to video_transcripts.csv")
