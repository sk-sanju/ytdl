from django.shortcuts import render
from django.http import HttpResponse
from .forms import YouTubeForm
import yt_dlp
import os
import logging

logger = logging.getLogger(__name__)

def download(request):
    if request.method == 'POST':
        form = YouTubeForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            try:
                # Set yt-dlp options
                ydl_opts = {
                    'format': 'best',  # Download the best available quality
                    'outtmpl': 'downloaded_video.mp4',  # Save file as downloaded_video.mp4
                }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    video_title = info.get('title', 'downloaded_video')

                # Read the downloaded file and return it as an HTTP response
                with open("downloaded_video.mp4", "rb") as video_file:
                    response = HttpResponse(video_file.read(), content_type='video/mp4')
                    response['Content-Disposition'] = f'attachment; filename="{video_title}.mp4"'

                # Clean up the file after serving
                os.remove("downloaded_video.mp4")
                return response
            except Exception as e:
                logger.error(f"Error downloading video: {e}")
                return render(request, 'error.html', {'error': str(e)})
    else:
        form = YouTubeForm()
    return render(request, 'index.html', {'form': form})
