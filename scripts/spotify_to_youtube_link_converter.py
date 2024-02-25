import os
import re
from youtubesearchpython import VideosSearch

def spotify_to_youtube(spotify_link):
	# extracting the song title and artist from the spotify link
	try:
		match = re.search(r'/track/(\w+)', spotify_link)
		if match:
			track_id = match.group(1)
			# replacing the track_id with corresponding yt link search query
			search_query = f"spotify {track_id} -topic"
			videos_search = VideosSearch(search_query, limit=1)
			results = videos_search.result()['result']
			if results:
				youtube_link = results[0]['link']
				print("Youtube link found")
				return youtube_link
			else:
				print("No Youtube link found for the song.")
		else:
			print("Invalid Spotify link format.")

	except Exception as e:
		print(f'An unexpected error occured: {str(e)}')

