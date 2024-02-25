import youtube_downloader
import spotify_to_youtube_link_converter

def menu():
	print("1)Youtube\n2)Spotify")
	input_platform = input("->")

	#for yt
	if input_platform == '1':
		url = input("Enter the Youtube video URL: ")
		file_type_choice(url)

	#for spotify
	if input_platform == '2':
		url = input("Enter the Spotify URL: ")
		url_converted = spotify_to_youtube_link_converter.spotify_to_youtube(url)
		file_type_choice(url_converted)

def file_type_choice(url):
	# Output path where the video will be saved
	output_path_video = "" # put your desired output direcotry between the quotes
	output_path_audio = "" # put your desired output direcotry between the quotes
	file_type = input("1)mp3\n2)mp4\n->")

	if file_type == '1':
		youtube_downloader.audio(url, output_path_audio)
	if file_type == '2':
		youtube_downloader.video(url, output_path_video)

if __name__ == "__main__":
	menu()
