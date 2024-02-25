from pytube import YouTube
import os
import time

# video download
def video(url, output_path):
	try:
		yt = YouTube(url)
		# getting the highest resolution stream
		stream = yt.streams.get_highest_resolution()
		# downloading the video
		time.sleep(3)
		stream.download(output_path)
		print("Video downloaded succesfully")

	except Exception as e:
		print(f'An error occurred: {str(e)}')

# audio download
def audio(url, output_path):
	try:
		yt = YouTube(url)
		# getting the audio stream
		audio_stream = yt.streams.filter(only_audio=True).first()
		# downloading the audio
		time.sleep(3)
		audio_file = audio_stream.download(output_path)
		# renaming the file to have a mp3 extension
		audio_path = f"{output_path}/{yt.title}.mp3"
		os.rename(audio_file, audio_path)
		print("Audio downloaded succesfully")

	except Exception as e:
		print(f"An error occured: {str(e)}")
