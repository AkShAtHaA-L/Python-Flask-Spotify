import requests
import json
import base64


'''
https://accounts.spotify.com/authorize?client_id=55b477d8e1ae4325a6821ef6fc118ccc&response_type=code&redirect_uri=https://example.com/&scope=user-library-read,user-library-modify,user-read-recently-played,user-top-read,playlist-read-private,playlist-read-collaborative,playlist-modify-private,playlist-modify-public

response = https://example.com/?code=AQC8w0G_5eFucDlU2T3xsQlVm7p6wWS_s7sLenclClSyb_g-jaSyGQLKkNBGARB_URFcQK3B4yi2BCfrzdUjmS71s51VKbHCHATG72KKHIHBWN5R75v7PmvE7Dvqcl4qSWtH4d2Hf9k-un9NA-cSCeTePq3umMB_Q1grz_7QzY23qwFovmxgE7KWlAsReSLO6Rt8HMmNJRpz2PO0hAhlIIj8v0tMXjec7BGzGI8MMULMaZaQiJLzX0vmbc6epRNrNvEThLqeR_qujSEAMot4oL1lO6IcEU7EGJqTQwMsWy-m4ZYSqdlj6SfaRUj_fbmRb3vU81ql0G9lh-ddDWGDkgAgwVMUuhS4NYKcIczfNp268IJlvQTpiJHSvnx0WLlce7ocAeZkuuQZffprLek
'''

AUTH_URL="https://accounts.spotify.com/api/token"
CLIENT_ID = '55b477d8e1ae4325a6821ef6fc118ccc'
CLIENT_SECRET = 'e88836c059974cceb56f84ba15a5bbe1'
REDIRECT_URI = 'https://example.com'

params = {
    'grant_type': 'authorization_code','code': 'AQC8w0G_5eFucDlU2T3xsQlVm7p6wWS_s7sLenclClSyb_g-jaSyGQLKkNBGARB_URFcQK3B4yi2BCfrzdUjmS71s51VKbHCHATG72KKHIHBWN5R75v7PmvE7Dvqcl4qSWtH4d2Hf9k-un9NA-cSCeTePq3umMB_Q1grz_7QzY23qwFovmxgE7KWlAsReSLO6Rt8HMmNJRpz2PO0hAhlIIj8v0tMXjec7BGzGI8MMULMaZaQiJLzX0vmbc6epRNrNvEThLqeR_qujSEAMot4oL1lO6IcEU7EGJqTQwMsWy-m4ZYSqdlj6SfaRUj_fbmRb3vU81ql0G9lh-ddDWGDkgAgwVMUuhS4NYKcIczfNp268IJlvQTpiJHSvnx0WLlce7ocAeZkuuQZffprLek','redirect_uri': REDIRECT_URI
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

response = requests.post(AUTH_URL, params=params, headers=headers)
print(response.text)

'''
response is 
{"access_token":"BQA_fertTzVoGwbukIttY6HCaLTK9yH-fHaXTmLpAsy8l_M5-mRo74ur6civdMGdjnfhvm4dZ6u8A_2U8dYtZ4NyeAMeeEUS_IwoG5mNjBIcEiQjmWszEIICdZ9u0uT7Hc0omlTbrrFJS3Uby6kWZ2V_VZ2R33tNOw_aGx8hnkOwFYMhzzehR0fmb0zssLa4UvBCMsrIyGgE6yaRlEcvLHPZcAtM0w-SsM8XG8MLzT5OQ-kaNpCTqbWnrdCPHWWo9BeWci8xTldsd58P5z-N4XLesXslyTwvj2rDqMj8g9U",
"token_type":"Bearer","expires_in":3600,"refresh_token":"AQDMFLPU67oS1HP6DL6s1nJjXBjDGhWHF1joKC8pw6-nkoY5GEPPhoD5uXP6Fuy5ZObwYZ81kkf8WbKV-UOwyyEL8Kx6aaZGTyJtgDRfQd8NZ5FZxejBs-oj5wamTxBVCJs",
"scope":"playlist-read-private playlist-read-collaborative user-library-read user-library-modify playlist-modify-private playlist-modify-public user-read-recently-played user-top-read"}
'''

# refresh_params = {
#     'grant_type': 'refresh_token','refresh_token': 'AQA28M2HJOoEnljV2UH3cirg53cFOtIRKkzqE5RhJEP93_5bUhScuspT94v53Wldtz0ba9fldLhXq89zaRKaArVpp4tIdh3aWQEpF1s6Xrvrjoh-MmlC3Oj4vVhHw_1NLyg',
# }

# response = requests.post(AUTH_URL, params=refresh_params, headers=headers)

# print(response.text)

'''
{"access_token":"BQDjmSP4E8FLwZBLNTMUCipeUSPIv1U_Ux7a7FfkiSmd_6mXjrhrPAQgZVmxZnkMdsnxQbM8jqMHvp_QbbRtuoetft9XJLBqXGKrFGJecZmPmXQY8XyjtrxipStvSb2X8mgL5zuZRaCDoTrPPYIjeTujxKHglIguw5FztZ6ZF-uF3D21JAJVml8wpT24y2Ws8Vx3bf7DY7PTNsFQhhttsbF0des5MOQxGXqu7bBLPTgHg2JUt0hmm6Vvjm-QhYNgAHkeVASRT-tVJnkeASmyWyPA6opemYaV77ZErWYvZoA","token_type":"Bearer","expires_in":3600,"scope":"playlist-read-private playlist-read-collaborative user-library-read user-library-modify playlist-modify-private playlist-modify-public user-read-recently-played user-top-read"}
'''