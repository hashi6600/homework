# main.py

class MoviePlayer:
    # Class attribute for firmware version
    firmware_version = 1.0

    def __init__(self):
        # Private attribute for storing movies
        self._movies = ['Frozen', 'Finding Nemo', 'Toy Story']
        # Attribute to store the currently playing movie
        self.current_movie = None

    def play(self):
        # Set the current movie to the first item in the movies list
        if self._movies:
            self.current_movie = self._movies[0]

    def list_movies(self):
        # Return the list of movies
        return self._movies

    @classmethod
    def update_firmware(cls, new_version):
        # Update firmware version only if the new version is more recent
        if new_version > cls.firmware_version:
            cls.firmware_version = new_version
            print("Firmware updated to version", new_version)
        else:
            print("Current firmware version is up to date")

if __name__ == '__main__':
    # Test the MoviePlayer class
    player = MoviePlayer()
    print("Movies currently on device:", player.list_movies())

    player.update_firmware(2.0)
    player.play()
    
    print("Updated player firmware version to", player.firmware_version)
    print("Currently playing:", player.current_movie)
