# create TV class
class TV:
    """A class to represent a TV set."""
    def __init__(self):
        self.on = False  # TV is initially off
        self.channel = 1  # Default channel is set to 1
        self.volume_level = 1   # Default volume is set to 1

    def turn_on(self):
        """Turns on the TV. """
        self.on = True

    def turn_off(self):
        """Turns off the TV."""
        self.on = False

    def get_channel(self):
        """Returns the channel."""
        return self.channel

    def set_channel(self, channel):
        """Sets a new channel."""
        if channel in range(1, 121):
            self.channel = channel

    def get_volume(self):
        """Gets the volume level for the TV."""
        return self.volume_level

    def set_volume(self, volume_level):
        """Sets a new volume level."""
        if volume_level in range(1, 8):
            self.volume_level = volume_level

    def channel_up(self):
        """Increases the channel number by 1."""
        self.channel = (self.channel + 1) % 120
        if self.channel == 0:
            self.channel = self.channel + 120  # Goes back to 120
        return self.channel

    def channel_down(self):
        """Decreases channel number by 1."""
        self.channel = (self.channel - 1) % 120
        if self.channel == 0:
            self.channel = self.channel + 120  # Goes back to 120
        else:
            return self.channel

    def volume_up(self):
        """Increases volume level by 1."""
        self.volume_level = min(self.volume_level + 1, 7)  # Stops at 7 if it exceeds 7
        return self.volume_level

    def volume_down(self):
        """Decreases volume level by 1."""
        self.volume_level = max(self.volume_level - 1, 1)  # Stops at 1 if it goes below 7
        return self.volume_level



