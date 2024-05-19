from tv import TV

# create two TV objects
tv_1 = TV()
tv_2 = TV()

# Turn on the TVs
tv_1.turn_on()
tv_2.turn_on()

# Interaction with user
while True:
    # Displays options to user
    print("Choose a TV to control! \n"
          " 1. TV 1 \n"
          " 2. TV 2 \n"
          " 3. Show the two TV status \n"
          " 4. Exit the program")

# Print the channel and volume level of the two TV OBJECT
    print(f"tv1's channel is {tv_1.get_channel()} and volume level is {tv_1.get_volume()}")
    print(f"tv2's channel is {tv_2.get_channel()} and volume level is {tv_2.get_volume()}")
    break
