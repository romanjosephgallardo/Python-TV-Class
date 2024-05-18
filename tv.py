# pseudocode

# create TV class
class TV:
    # create method for default TV object
    def __init__(self):
        self.on = False
        self.channel = 1
        self.volume_level = 1

    # create method for turning on TV
    def turn_on(self):
        self.on = True

    # create method for turning off TV
    def turn_off(self):
        self.on = False

    #  create method that returns the channel
    def get_channel(self):
        return self.channel

    #  create method that sets new channel
    def set_channel(self, channel):
        if channel in range(1, 121):
            self.channel = channel

    #  create method that gets the volume level
    def get_volume(self):
        return self.volume_level

    #   create method that sets new volume
    def set_volume(self, volume_level):
        if volume_level in range(1, 8):
            self.volume_level = volume_level

    #   create method that increases channel number by 1
    def channel_up(self):
        if self.channel < 120:
            self.channel += 1
        return self.channel

    #   create method that decreases channel number by 1
    def channel_down(self):
        if self.channel > 1:
            self.channel -= 2
        return self.channel

    #   create method that increases volume level by 1
    def volume_up(self):
        if self.volume_level < 7:
            self.volume_level += 1
        return self.volume_level

    #   create method that decreases volume level by 1
    def volume_down(self):
        if self.volume_level > 1:
            self.volume_level -= 2
        return self.volume_level



