import base64
import json
import os
from datetime import date

import requests
from dotenv import load_dotenv,dotenv_values,find_dotenv
from flask import Flask, redirect, render_template, request

###################3 Set up Spotify API authentication ###################
#print(load_dotenv(find_dotenv(),encoding=None))
SPOTIFY_ENDPOINT = "https://api.spotify.com/v1"
AUTH_URL="https://accounts.spotify.com/api/token"
CLIENT_ID = os.environ['CLIENT_ID']
CLIENT_SECRET = os.environ['CLIENT_SECRET']
REFRESH_TOKEN = os.environ['REFRESH_TOKEN']
############################################################################
app = Flask(__name__)

def refresh_user_token():
    ###encode the client secret and ID####
    string = CLIENT_ID + ":" + CLIENT_SECRET
    string_bytes = string.encode('ascii')
    b64_bytes = base64.b64encode(string_bytes)
    encoded_secret_key = b64_bytes.decode('ascii')
    
    refreshheaders = {
    'Authorization': 'Basic ' + encoded_secret_key,
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    
    refresh_params = {
    'grant_type': 'refresh_token','refresh_token': REFRESH_TOKEN
    }
    response = json.loads(requests.post(AUTH_URL, params=refresh_params, headers=refreshheaders).text)
    ACCESS_TOKEN = response['access_token']
    os.environ['ACCESS_TOKEN'] = ACCESS_TOKEN

def get_current_user():
    response = json.loads(requests.get(SPOTIFY_ENDPOINT+'/me', headers=headers).text)
    return response['display_name'], response['id']

def get_top_tracks():
    my_top_ten_tracks = []
    params = {
        'limit': 10,
        'time_range': 'short_term'
    }
    response = json.loads(requests.get(SPOTIFY_ENDPOINT+"/me/top/tracks", params=params, headers=headers).text)['items']
    for item in response:
        track_name = item['name']
        track_id = item['id']
        track_uri = item['uri']
        
        artist_id = []
        for artist in item['artists']:
            artist_id.append(artist['id'])
        artist_id = ','.join(artist_id)
        
        track_preview = item['preview_url']
        
        my_top_ten_tracks.append({'trackname':track_name, 'trackid':track_id, 'trackuri':track_uri, 'trackpreview':track_preview,'artistid':artist_id})
    
    return my_top_ten_tracks

def get_recommended_tracks(top_tracks_details):
    rec_songs = {}
    for track_details in top_tracks_details:
        params = {
            'market': 'IN',
            'seed_artists': track_details['artistid'],
            'seed_tracks' : track_details['trackid'],
            'limit':1
        }
        response = json.loads(requests.get(SPOTIFY_ENDPOINT+'/recommendations', headers=headers, params=params).text)['tracks']
        rec_track_uri, rec_track_name = response[0]['uri'], response[0]['name']
        if len(rec_songs) < 5:
            rec_songs[rec_track_name] = rec_track_uri
    return rec_songs

def get_missed_hits(top_five_tracks):
    top_missed_tracks = {}
    top_50_playlist_id = "/playlists/37i9dQZEVXbLZ52XmnySJg/tracks"
    params = {
        'market': 'IN',
        'limit': 5
    }
    response = json.loads(requests.get(SPOTIFY_ENDPOINT+top_50_playlist_id, headers=headers).text)['items']
    for item in response:
        if len(top_missed_tracks) == 5:
            break
        if item['track']['name'] not in top_five_tracks.keys():
            top_missed_tracks[item['track']['name']] = item['track']['uri']
    return top_missed_tracks

def get_top_five(top_tracks_details):
    top_five_tracks = {}
    for track_details in top_tracks_details:
        track_name = track_details['trackname']
        trackpreview = track_details['trackpreview']
        if track_name not in top_five_tracks.keys() and len(top_five_tracks)<5:
            top_five_tracks[track_name]=trackpreview
    return top_five_tracks
    

def add_songs_to_playlist(playlist_id):
    rec_uris = []
    for name,uri in top_rec_tracks.items():
        rec_uris.append(uri)

    for name,uri in top_missed_tracks.items():
        rec_uris.append(uri)
    print(rec_uris)
    data = json.dumps({
        'uris': rec_uris
    })
    response = requests.post(SPOTIFY_ENDPOINT+f"/playlists/{playlist_id}/tracks", data=data, headers=headers).text
    print(response)


@app.route("/")
def home_page():
    return render_template('home.html', 
                           user_name = current_user,
                           top_five_tracks = top_five_tracks,
                           top_rec_tracks = top_rec_tracks,
                           top_missed_tracks = top_missed_tracks
                           )

@app.route("/createplaylist", methods=["POST"])
def create_playlist():
    todays_date = str(date.today())
    playlist_name = f'Recommended songs-{todays_date}'
    data = json.dumps({
        'name': playlist_name,
        'description': 'Playlist created using Flask',

    })
    playlist_id = json.loads(requests.post(SPOTIFY_ENDPOINT+f"/users/{current_user_id}/playlists", headers=headers, data=data).text)['id']
    add_songs_to_playlist(playlist_id)
    playlist_href = json.loads(requests.get(SPOTIFY_ENDPOINT+f"/playlists/{playlist_id}", headers=headers).text)['external_urls']['spotify']
    return render_template('playlist.html',
                           playlist_name=playlist_name,
                           playlist_href=playlist_href)


if __name__ == '__main__':
    refresh_user_token()
    
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']
    
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
    }
    
    current_user, current_user_id = get_current_user()
    top_tracks_details = get_top_tracks()
    top_five_tracks = get_top_five(top_tracks_details)
    top_rec_tracks = get_recommended_tracks(top_tracks_details)
    top_missed_tracks = get_missed_hits(top_five_tracks)
    
    app.run(host='0.0.0.0', debug=True)