# pseudocode

# create TV class
class TV:
    # create method for default TV object
    def __init__(self):
        self.on = False
        self.channel = 1
        self.volume = 1

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
        return self.volume


#   create method that sets new volume
#   create method that increases channel number by 1
#   create method that decreases channel number by 1
#   create method that increases volume level by 1
#   create method that decreases volume level by 1

# create two TV objects
tv_1 = TV()
tv_2 = TV()

# set channel and volume for tv1
tv_1.set_channel(2)

# set channel and volume for tv2
tv_2.set_channel(64)
# Print the channel and volume level of the two TV  OBJECT
print(f"tv1's channel is {tv_1.get_channel()}")
print(f"tv2's channel is {tv_2.get_channel()}")
