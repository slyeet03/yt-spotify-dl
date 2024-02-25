import youtube_downloader
import spotify_to_youtube_link_converter

def menu():
	print("1)Youtube\n2)Spotify")
	input_platform = input("->")

	#for yt
	if input_platform == '1':
		url = input("Enter the Youtube video URL: ")
		file_type = input("1)mp3\n2)mp4\n->")
		file_type_choice(url, file_type)

	#for spotify
	if input_platform == '2':
		url = input("Enter the Spotify URL: ")
		url_converted = spotify_to_youtube_link_converter.spotify_to_youtube(url)
		file_type = input("1)mp3\n2)mp4\n->")
		file_type_choice(url_converted, file_type)

def file_type_choice(url, file_type_choice):
	# Output path where the video will be saved
	output_path_video = "" #put your desired output path
	output_path_audio = "" #put your desired output path

	if file_type_choice == '1':
		youtube_downloader.audio(url, output_path_audio)
	if file_type_choice == '2':
		youtube_downloader.video(url, output_path_video)

if __name__ == "__main__":
	menu()