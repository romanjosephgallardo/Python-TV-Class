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

    tv_choice = input("Enter your option: ")

    if tv_choice == '1':
        selected_tv = tv_1
        tv_name = "TV 1"
        print(f"\nControlling the {tv_name}. Choose an action: \n"
              " 1. Increase Channel \n"
              " 2. Decrease Channel \n"
              " 3. Increase Volume \n"
              " 4. Decrease Volume \n"
              " 5. Back to TV Selection")

        action_choice = input("Enter your choice (1-5): ")

        # Performing the action
        if action_choice == '1':
            tv_1.channel_up()
        if action_choice == '2':
            tv_1.channel_down()
        if action_choice == '3':
            tv_1.volume_up()
        if action_choice == '4':
            tv_1.volume_down()
        if action_choice == '5':
            continue

    # For TV 2
    if tv_choice == '2':
        selected_tv = tv_1
        tv_name = "TV 1"
        print(f"\nControlling the {tv_name}. Choose an action: \n"
              " 1. Increase Channel \n"
              " 2. Decrease Channel \n"
              " 3. Increase Volume \n"
              " 4. Decrease Volume \n"
              " 5. Back to TV Selection")

        action_choice = input("Enter your choice (1-5): ")

        # Performing the action
        if action_choice == '1':
            tv_2.channel_up()
        if action_choice == '2':
            tv_2.channel_down()
        if action_choice == '3':
            tv_2.volume_up()
        if action_choice == '4':
            tv_2.volume_down()
        if action_choice == '5':
            continue

    # Print the channel and volume level of the two TV OBJECT
    print(f"tv1's channel is {tv_1.get_channel()} and volume level is {tv_1.get_volume()}")
    print(f"tv2's channel is {tv_2.get_channel()} and volume level is {tv_2.get_volume()}")
    continue
