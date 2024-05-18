

# create TV class
class TV:

    # Initialize a TV object
    def __init__(self):
        self.on = False
        self.channel = 1
        self.volume_level = 1

    # Turns on the TV
    def turn_on(self):
        self.on = True

    # Turns off the TV
    def turn_off(self):
        self.on = False

    # Returns the channel
    def get_channel(self):
        return self.channel

    # Sets a new channel
    def set_channel(self, channel):
        if channel in range(1, 121):
            self.channel = channel

    # Gets the volume level for the TV
    def get_volume(self):
        return self.volume_level

    # Sets a new volume level
    def set_volume(self, volume_level):
        if volume_level in range(1, 8):
            self.volume_level = volume_level

    # Increases the channel number by 1
    def channel_up(self):
        self.channel = (self.channel + 1) % 120
        return self.channel

    # Decreases channel number by 1
    def channel_down(self):
        self.channel = (self.channel - 2) % 120
        return self.channel

    # Increases volume level by 1
    def volume_up(self):
        if self.volume_level < 7:
            self.volume_level += 1
        return self.volume_level

    # Decreases volume level by 1
    def volume_down(self):
        if self.volume_level > 1:
            self.volume_level -= 2
        return self.volume_level



