from tv import TV

# create two TV objects
tv_1 = TV()
tv_2 = TV()

# set channel and volume for tv1
tv_1.set_channel(2)
tv_1.set_volume(4)

# set channel and volume for tv2
tv_2.set_channel(64)
tv_2.set_volume(7)

# Print the channel and volume level of the two TV OBJECT
print(f"tv1's channel is {tv_1.get_channel()} and volume level is {tv_1.get_volume()}")
print(f"tv2's channel is {tv_2.get_channel()} and volume level is {tv_2.get_volume()}")