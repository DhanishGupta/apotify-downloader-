import os
import spotdl
import rich
from rich.console import Console
import sys
import time
import pyfiglet

#colored text function
console = Console()
def print_text(text, colour="green", delay=0.01):
    for char in text:
        console.print(f"[{colour}]{char}[/]", end="")
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ASCII art for the title
ascii_banner = pyfiglet.figlet_format("Music Downloader")
console.print(f"[green]{ascii_banner}[/green]")

# Function 
playlist_url=""
output_folder=""
def download_spotify_playlist(playlist_url, output_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Construct the command to download the playlist and save it to the specified folder
    command = f'spotdl {playlist_url} --output "{output_folder}" --bitrate 320k'
    
    # Execute the command
    os.system(command)

#download songs
print_text("download music from spotify easily no ads, no hustle :) ")
print("")
print_text("Do you want to download in a music_folder or create new? (d/n): ")
choice=input(">>>")
if choice=='n':
    print_text("Enter the name of the song: ")
    name = input()
    output_folder = os.path.normpath(rf"D:\xyz\Music\{name}") #enter your music folder path here
    print("")
    print_text("Enter the Spotify song URL: ")
    playlist_url = input(">>>")

elif choice=='d':
    print_text("Enter the name of the song/playlist: ")
    name = input()
    output_folder = os.path.normpath(rf"D:\xyz\Music\downloaded_songs") #enter your default music folder path here
    print("")
    print_text("Enter the Spotify playlist URL: ")
    playlist_url = input(">>>")
else:
    print_text("some error occured  :(")
    sys.exit()

# Download function call
try:

    download_spotify_playlist(playlist_url, output_folder)
    time.sleep(1)
    print("")
    print_text("songs downloader successfully :)")

except Exception as e:
    print_text(f"An error occurred: {e}", colour="red")

n=input("").strip().lower()
while(1):
    if n=="leave" or n=="exit":
        break
    else:
        continue
    

