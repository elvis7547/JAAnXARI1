from flask import Flask, request, render_template
import os
import pytube
from instaloader import Instaloader
import twint
from facebook_scraper import get_video_download_url
from AarohiX import app

def download_youtube_video(url, output_path="."):
    try:
        youtube = pytube.YouTube(url)
        video_stream = youtube.streams.filter(file_extension="mp4").first()
        print(f"Downloading YouTube Video: {youtube.title}...")
        video_stream.download(output_path)
        print("Download complete!")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def download_instagram_video(url, output_path="."):
    try:
        loader = Instaloader()
        post = loader.load_post_from_url(url)
        video_url = post.url
        youtube = pytube.YouTube(video_url)
        video_stream = youtube.streams.filter(file_extension="mp4").first()
        print(f"Downloading Instagram Video: {post.caption}...")
        video_stream.download(output_path)
        print("Download complete!")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def download_twitter_video(url, output_path="."):
    try:
        tweet_id = url.split("/")[-1]
        c = twint.Config()
        c.DownloadPath = output_path
        c.Retweets = False
        c.Username = "placeholder"  # Replace with the actual Twitter handle
        c.Since = "2022-01-01"  # Choose a starting date for your search
        c.Store_object = True
        c.Store_json = True
        c.Format = "{id}"
        twint.run.Lookup(c)

        video_url = f"https://twitter.com/i/status/{tweet_id}"
        youtube = pytube.YouTube(video_url)
        video_stream = youtube.streams.filter(file_extension="mp4").first()
        print(f"Downloading Twitter Video: {tweet_id}...")
        video_stream.download(output_path)
        print("Download complete!")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

def download_facebook_video(url, output_path="."):
    try:
        video_url = get_video_download_url(url)
        if video_url:
            facebook = pytube.YouTube(video_url)
            video_stream = facebook.streams.filter(file_extension="mp4").first()
            print(f"Downloading Facebook Video...")
            video_stream.download(output_path)
            print("Download complete!")
            return True
        else:
            print("Error: Unable to fetch Facebook video download URL.")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def process_link_and_download(link):
    download_output_path = "downloads"

    if "youtube.com" in link:
        return download_youtube_video(link, download_output_path)
    elif "instagram.com" in link:
        return download_instagram_video(link, download_output_path)
    elif "twitter.com" in link:
        return download_twitter_video(link, download_output_path)
    elif "facebook.com" in link:
        return download_facebook_video(link, download_output_path)
    else:
        return False

@app.route('/', methods=['POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']
        download_success = process_link_and_download(video_url)

        return render_template('index.html', download_success=download_success)
    return render_template('index.html', download_success=None)
