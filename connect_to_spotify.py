import requests
import json
import base64


'''
https://accounts.spotify.com/authorize?client_id=55b477d8e1ae4325a6821ef6fc118ccc&response_type=code&redirect_uri=https://example.com/&scope=user-library-read,user-library-modify,user-read-recently-played,user-top-read,playlist-read-private,playlist-read-collaborative,playlist-modify-private,playlist-modify-public

https://example.com/?code=AQBRSrkkIY1gpA78iGWHqZ7tru8sd0vwoUDT_x9TuJ9U93aBRHgjCwZiXe9MJhx7u_aWKTyGCh1A65uBIwPXZ-t4eARRfuHVgWuupcN5qPXmo-_SwCaYAAqJ_h4b4bH1GRJv9HeE9D4wTR9FAViUsPgBlI6IutsT5IWbW7wSf_jOADXcRI60Wi7MS80AorPDBtyv6oAn2UYFB8DDPU79P1nlN3eGc1BaqcHpKf82ogXZOyPyApb6xjFA6nYzsdrTQqblFkXGyPX67PSvqE6t-DrfQsW6S7PMIY5Rx2_W4cFLsOqhMLKw7oOtCyIkiKKImXSJSmSQ6jejo5r_irMbRImahjjkoYlt5zrqrNiAM72x6vDDus0hK_9n3mFco2JOVSfcXipuKHmowlcbxbw

response = https://example.com/?code=AQDI-bYdLQMM4SocZ6Fc_6Nlbr7OIuVr_7YoAVbJUN-L-CD08VgAsqrE2cgNR7muLgc_P03Gm1a7m_k42iYmN1wwrz3y9tssTDdxtgaPSLDYIzOZVj1-wWt4YbD2soS0BYE6Xw3tykbmejDfyztW4XNRzOTON4Z2r9rD6oBTreQe2FbPb5g4_oAgRwF6D-Bw271ttGmIpsfmp1kEX152Ch3c7eVgpmj7zAhW5qGU6qc2TFxGODB_aR6yuyulA9NiRWNINS5ibKG1WN94Y_KU03LOxXsiyAmzmIFHmuzQEzoIbcp8uAm1SnvKsHH9Ij4pagzmnRlCM25l8_KdhjtZ_FDkhFvVA25F0bo5GP4U97xA68YSr9vUGrVAUlwdDRp8Vm8bX7KcVrNi3-y_E4g
'''

AUTH_URL="https://accounts.spotify.com/api/token"
CLIENT_ID = '55b477d8e1ae4325a6821ef6fc118ccc'
CLIENT_SECRET = 'e88836c059974cceb56f84ba15a5bbe1'
REDIRECT_URI = 'https://example.com'

params = {
    'grant_type': 'authorization_code','code': 'AQDI-bYdLQMM4SocZ6Fc_6Nlbr7OIuVr_7YoAVbJUN-L-CD08VgAsqrE2cgNR7muLgc_P03Gm1a7m_k42iYmN1wwrz3y9tssTDdxtgaPSLDYIzOZVj1-wWt4YbD2soS0BYE6Xw3tykbmejDfyztW4XNRzOTON4Z2r9rD6oBTreQe2FbPb5g4_oAgRwF6D-Bw271ttGmIpsfmp1kEX152Ch3c7eVgpmj7zAhW5qGU6qc2TFxGODB_aR6yuyulA9NiRWNINS5ibKG1WN94Y_KU03LOxXsiyAmzmIFHmuzQEzoIbcp8uAm1SnvKsHH9Ij4pagzmnRlCM25l8_KdhjtZ_FDkhFvVA25F0bo5GP4U97xA68YSr9vUGrVAUlwdDRp8Vm8bX7KcVrNi3-y_E4g','redirect_uri': REDIRECT_URI
}

###encode the client secret and ID####
string = CLIENT_ID + ":" + CLIENT_SECRET
string_bytes = string.encode('ascii')
b64_bytes = base64.b64encode(string_bytes)
encoded_secret_key = b64_bytes.decode('ascii')
##################################
headers = {
    'Authorization': 'Basic ' + encoded_secret_key,
    'Content-Type': 'application/x-www-form-urlencoded'
}

# response = requests.post(AUTH_URL, params=params, headers=headers)
# print(response.text)

'''
response is 
{"access_token":"BQBvUDLwtrjTL2QKdtbyomrIvQg4WZTjaDbSJVstt7cLI6pyZLylXmIWJ7K36SAcilPaKwWlLGo9VTitXOtoAgA-x-arezHpyuL05z1fLrPisSvzg6XdkSOYN_SlupA4ctoHu8pd897CEiE61y9yDduPnxP7yc0_pjgCOeOJfW0JPCa8AlDM8crQ_-o1WSKZVxK2GHvEiwQ_ytKXqHFOYtJ2jBDSyXAxIEIotc5feGCeGf9kSsVfnFtyMhzygEqnGzNKZhIZJ_kisgkGGt11XqgZ0mIqV_MzMtym7c8Qgak",
"token_type":"Bearer",
"expires_in":3600,"refresh_token":"AQA28M2HJOoEnljV2UH3cirg53cFOtIRKkzqE5RhJEP93_5bUhScuspT94v53Wldtz0ba9fldLhXq89zaRKaArVpp4tIdh3aWQEpF1s6Xrvrjoh-MmlC3Oj4vVhHw_1NLyg",
"scope":"playlist-read-private playlist-read-collaborative user-library-read user-library-modify playlist-modify-private playlist-modify-public user-read-recently-played user-top-read"}
'''

refresh_params = {
    'grant_type': 'refresh_token','refresh_token': 'AQA28M2HJOoEnljV2UH3cirg53cFOtIRKkzqE5RhJEP93_5bUhScuspT94v53Wldtz0ba9fldLhXq89zaRKaArVpp4tIdh3aWQEpF1s6Xrvrjoh-MmlC3Oj4vVhHw_1NLyg',
}

response = requests.post(AUTH_URL, params=refresh_params, headers=headers)

print(response.text)

'''
{"access_token":"BQDjmSP4E8FLwZBLNTMUCipeUSPIv1U_Ux7a7FfkiSmd_6mXjrhrPAQgZVmxZnkMdsnxQbM8jqMHvp_QbbRtuoetft9XJLBqXGKrFGJecZmPmXQY8XyjtrxipStvSb2X8mgL5zuZRaCDoTrPPYIjeTujxKHglIguw5FztZ6ZF-uF3D21JAJVml8wpT24y2Ws8Vx3bf7DY7PTNsFQhhttsbF0des5MOQxGXqu7bBLPTgHg2JUt0hmm6Vvjm-QhYNgAHkeVASRT-tVJnkeASmyWyPA6opemYaV77ZErWYvZoA","token_type":"Bearer","expires_in":3600,"scope":"playlist-read-private playlist-read-collaborative user-library-read user-library-modify playlist-modify-private playlist-modify-public user-read-recently-played user-top-read"}
'''