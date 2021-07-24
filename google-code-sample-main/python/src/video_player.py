"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""
    currently_playing = ""
    paused = 0
    playlists = []
    for item in playlists:
        item = []

    def __init__(self):
        self._video_library = VideoLibrary()

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        vids = self._video_library.get_all_videos()
        vids.sort(key = lambda x: x.title)
        for vid in vids:
            strings = str(vid.tags).replace("'","").replace(",","").replace("(","[").replace(")","]")
            print("  " + vid.title + " (" + vid.video_id + ") "+ strings)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        currently_playing = self.currently_playing
        vid = self._video_library.get_video(video_id)

        try:
            self.currently_playing = vid.title
            if currently_playing != "":
                print("Stopping video: " + str(currently_playing))
            print("Playing video: " + str(vid.title))
            self.paused = 0
        except:
            print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""
        if self.currently_playing != "":
            print("Stopping video: " + str(self.currently_playing))
            self.currently_playing = ""
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""

        videos = self._video_library.get_all_videos()
        list_of_ids = []
        for video in videos:
            list_of_ids.append(video.video_id)

        self.play_video(random.choice(list_of_ids))


    def pause_video(self):
        """Pauses the current video."""
        if self.currently_playing != "":
            if self.paused == 0:
                print("Pausing video: " + str(self.currently_playing))
                self.paused = 1
            else:
                print("Video already paused: " + str(self.currently_playing))
        else:
            print("Cannot pause video: No video is currently playing")


    def continue_video(self):
        """Resumes playing the current video."""
        if self.currently_playing != "":
            if self.paused == 1:
                print("Continuing video: " + str(self.currently_playing))
                self.paused = 0
            else:
                print("Cannot continue video: Video is not paused")

        else:
            print("Cannot continue video: No video is currently playing")



    def show_playing(self):
        """Displays video currently playing."""
        if self.currently_playing != "":
            videos = self._video_library.get_all_videos()
            for video in videos:
                if video.title == self.currently_playing:
                    tags = str(video.tags).replace("'", "").replace(",", "").replace("(", "[").replace(")", "]")
                    if self.paused == 1:
                        print("Currently playing: " + video.title + " (" + video.video_id + ") " + tags + " - PAUSED")
                    else:
                        print("Currently playing: "+ video.title + " (" + video.video_id + ") " + tags)
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        self._video_library.get_all_videos()
        lower_playlists = []
        for i in range(len(self.playlists)):
            lower_playlists.append(self.playlists[i].lower())

        if playlist_name.lower() not in lower_playlists:
            print("Successfully created new playlist: " + playlist_name)
            self.playlists.append(playlist_name)
        else:
            print("Cannot create playlist: A playlist with the same name already exists")




    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """



    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
