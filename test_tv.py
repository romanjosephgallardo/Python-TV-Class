from tv import TV


def display_tv_status(tv, tv_number):
    # Prints the current status of the TV
    print(f"{tv_number}'s channel is {tv.get_channel()} and volume level is {tv.get_volume()}".center(50))


# create two TV objects
tv_1 = TV()
tv_2 = TV()

# Turn on the TVs
tv_1.turn_on()
tv_2.turn_on()

# Interaction with user
while True:
    # Displays options to user
    print("\nChoose a TV to control! \n"
          " 1. TV 1 \n"
          " 2. TV 2 \n"
          " 3. Show the two TV status \n"
          " 4. Exit the program")

    try:
        tv_choice = int(input("Enter your option: "))
        if tv_choice == 1:
            selected_tv = tv_1
            tv_name = "TV 1"
        elif tv_choice == 2:
            selected_tv = tv_2
            tv_name = "TV 2"
        elif tv_choice == 3:
            print()
            print("—" * 50)
            display_tv_status(tv_1, "tv1")
            display_tv_status(tv_2, "tv2")
            print("—" * 50)
            continue
        elif tv_choice == 4:
            print("Thank you for using the program!")
            break
        else:
            print("Invalid input. Please enter 1-4 only.")
            continue
    except ValueError:
        print("Invalid input. Please enter 1-4 only.")
        continue

    print(f"\nControlling the {tv_name}. Choose an action: \n"
          " 1. Increase Channel \n"
          " 2. Decrease Channel \n"
          " 3. Increase Volume \n"
          " 4. Decrease Volume \n"
          " 5. Back to TV Selection")

    action_choice = input("Enter your choice (1-5): ")

    # Performing the action
    try:
        if action_choice == '1':
            selected_tv.channel_up()
        elif action_choice == '2':
            selected_tv.channel_down()
        elif action_choice == '3':
            selected_tv.volume_up()
        elif action_choice == '4':
            selected_tv.volume_down()
        elif action_choice == '5':
            continue
        else:
            print("Invalid input. Please enter 1-4 only.")
            continue
    except ValueError:
        print("Invalid input. Please enter 1-5 only.")
        continue

    # Print the channel and volume level of the two TV OBJECT
    display_tv_status(selected_tv, tv_name)
    continue
