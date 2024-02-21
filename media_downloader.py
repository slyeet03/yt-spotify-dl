from pytube import YouTube
import os
import re
from youtubesearchpython import VideosSearch

# It won't work with age restriced videos 

# Youtube Video download
def download_video(url, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)
        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()
        # Download the video
        stream.download(output_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Youtube Audio download
def download_audio(url, output_path):
    try:
        # Create a YouTube object
        yt = YouTube(url)
        # Get the audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        # Download the audio stream
        audio_file = audio_stream.download(output_path)
        # Rename the audio file to have an mp3 extension
        audio_path = f"{output_path}/{yt.title}.mp3"
        os.rename(audio_file, audio_path)
        print("Audio downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Converting Spotiy link to Youtube link
def spotify_to_youtube(spotify_link):
    # Extract the song title and artist from the Spotify link
    match = re.search(r'/track/(\w+)', spotify_link)
    if match:
        track_id = match.group(1)
        # Replace the track_id with the corresponding YouTube link search query
        search_query = f"spotify {track_id} -topic"
        videos_search = VideosSearch(search_query, limit=1)
        results = videos_search.result()['result']
        if results:
            youtube_link = results[0]['link']
            print("Youtube link found")
            return youtube_link
        else:
            print("No YouTube link found for the song.")
    else:
        print("Invalid Spotify link format.")

if __name__ == "__main__":

    # Output path where the video will be saved
    output_path_video = "yt vids"
    output_path_audio = "yt audios"

    print("1)Youtube\n2)Spotify")
    input_for_platform = input("-> ")

    # for Youtube
    if input_for_platform == "1":
        # YouTube video URL
        video_url = input("Enter the YouTube video URL: ")
        input_for_file_format = input("mp3 or mp4?: ")
        if input_for_file_format == "mp3":
            download_audio(video_url, output_path_audio)
        if input_for_file_format == "mp4":
            download_video(video_url, output_path_video)
    
    # for Spotify
    if input_for_platform == "2":
        spotify_link = input("Enter the Spotify song link: ")
        yt_link = spotify_to_youtube(spotify_link)
        input_for_file_format = input("mp3 or mp4?: ")
        if input_for_file_format == "mp3":
            download_audio(yt_link, output_path_audio)
        if input_for_file_format == "mp4":
            download_video(yt_link, output_path_video)