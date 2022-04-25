'''
Wrapper class for Spotify Web API
'''

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


class SpotifyAPI:
    '''
    Wrapper class for Spotify Web API
    Attributes:
        CLIENT_ID: Spotify API client ID
        CLIENT_SECRET: Spotify API client secret
    '''

    def __init__(self):
        '''
        Initialize a Spotify object that can be used to connect to and make
        requests from Spotify Web API
        Args:
            None
        '''
        with open('spotify_creds.txt', encoding="utf-8") as credentials:
            lines = [line.strip() for line in credentials.readlines()]
            self.client_id = lines[0]
            self.client_secret = lines[1]

        authenticate = SpotifyClientCredentials(client_id=self.client_id,
                                               client_secret=self.client_secret)
        self.spotify = spotipy.Spotify(auth_manager=authenticate)

    def get_track_id(self, song, artist):
        '''
        Get track IDs for the input songs and artists.
        Args:
            song (str): Song name
            artist (str): Artist name
        Returns:
            track_id (str): Track ID for the input song and artist
        '''

        # Get track IDs for the input song and artist
        search_results = self.spotify.search(
            q=f"track:{song} artist:{artist}", limit=1,
            offset=0, type='track', market="IN")

        # return search_results
        return search_results['tracks']['items'][0]['id']

    def get_audio_features(self, track_id):
        '''
        Get audio features for the input track ID.
        Args:
            track_id (str): Track ID
        Returns:
            audio_features (dict): Audio features for the input track ID
        '''
        # audio_features = self.spotify.audio_features(track_id)
        audio_features = self.spotify.audio_analysis(track_id)
        return audio_features
    
    def get_track_info(self, track_id):
        '''
        Get track information for the input track ID.
        Args:
            track_id (str): Track ID
        Returns:
            track (dict): Track information for the input track ID
        '''
        track = self.spotify.track(track_id)
        return track
