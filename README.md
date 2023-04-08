# Python-Flask-Spotify

Connect to Spotify - 

'''
https://accounts.spotify.com/authorize?client_id=abc&response_type=code&redirect_uri=https://example.com&scope=user-library-read,user-library-modify,user-read-recently-played,user-top-read,playlist-read-private,playlist-read-collaborative,playlist-modify-private,playlist-modify-public
'''

Get the 'Code' value from hitting the above URL.
Sample response = "response = https://example.com/?code=ABC"

Get the values of CLIENT_ID and CLIENT_SECRET from the spotify app.
Set the headers, where encoded_secret_key is the encoded value of CLIENT_ID and CLIENT_SECRET - 

headers = {
    'Authorization': 'Basic ' + encoded_secret_key,
    'Content-Type': 'application/x-www-form-urlencoded'
}

Set the params,
params = {
    'grant_type': 'authorization_code','code': code ,'redirect_uri': REDIRECT_URI
}

response = requests.post(AUTH_URL, params=params, headers=headers)
print(response.text)

Sample response would be -
{"access_token":"ABC",
"token_type":"Bearer","expires_in":3600,"refresh_token":"XYZ",
"scope":"playlist-read-private playlist-read-collaborative user-library-read user-library-modify playlist-modify-private playlist-modify-public user-read-recently-played user-top-read"}

Set the env variables - CLIENT_ID,CLIENT_SECRET,REFRESH_TOKEN
The code gets a new token using REFRESH_TOKEN every time it is executed.

![python-spotify](https://user-images.githubusercontent.com/124445330/230706094-e81c4b42-64f5-4d44-9d0e-ced012a2f430.png)

- Top 5 user hits for the last month
- Recommended songs based on the top hits
- Missed hits from top-50 India playlist

Create playlist button, would create a playlist in the user account combining the recommended songs and the missed hits.
