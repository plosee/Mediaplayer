# Mediaplayer
This code uses several libraries (Tkinter, Pygame, pytube, etc.) to create a jukebox-like program that allows the user to select a song from a list of songs specified in a .txt file. The program then searches for the song on YouTube, downloads the audio from the first result, and plays it using Pygame.
  
**THIS IS NOT THE FULL RELEASE, IT WILL IN NO WAY REPRESENT THE FINAL BUILD**

# Features
Simple GUI
Download music through YouTube  
Now Playing text  
  
# How to use Mediaplayer
Have a text file with music titles inside of it seperated by \n
  
Install ffmpeg through [the official ffmpeg downdload site](https://www.ffmpeg.org/download.html) and include the ffmpeg.exe directory (*your ffmpeg installation*/bin) in your [Path](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/) under user variables
  
Run Mediaplayer.exe  
  
To compile, [use pyinstaller](https://pyinstaller.org/en/stable/)  
# Modules that mediaplayer uses

subprocess  
os  
sys  
shutil  
tkinter   
atexit  
pygame  
youtube-search-python    
pytube  
pathlib  
pydub  

  
# Will update it with the following soon...
bug fixes  
easier on the eyes GUI  
able to use links directly for music  
graphical progress bar w/ minutes  
hide debug window  
have spotify and soundcloud implemented  
playlists  
more configuration options  
fix variable names  
optimize the code  
make offline listening available  
if config implemented show offline mp3 files from path you provide and option to not remove cache file upon exit  
  
more of a bucket list  
