from tv import TV


# Defines a TV controls
class TVController:
    def __init__(self):
        # Initialize two TV objects and turn them on
        self.tv_1 = TV()
        self.tv_2 = TV()
        self.tv_1.turn_on()
        self.tv_2.turn_on()

    def display_tv_status(self, tv, tv_number):
        # Prints the current status of the TV
        print(f"{tv_number}'s channel is {tv.get_channel()} and volume level is {tv.get_volume()}".center(50))

    # Interaction with user
    def select_tv(self):
        # Loop for selecting a TV to control or displaying status of two TVs
        while True:
            # Displays options to user
            print("\nChoose a TV to control! \n"
                  " 1. TV 1 \n"
                  " 2. TV 2 \n"
                  " 3. Show the two TV status \n"
                  " 4. Exit the program")

            try:
                # Get user's input choice
                tv_choice = int(input("Enter your option: "))
                if tv_choice == 1:
                    selected_tv = self.tv_1
                    tv_name = "TV 1"
                elif tv_choice == 2:
                    selected_tv = self.tv_2
                    tv_name = "TV 2"
                elif tv_choice == 3:
                    print()
                    print("—" * 50)
                    self.display_tv_status(self.tv_1, "tv1")
                    self.display_tv_status(self.tv_2, "tv2")
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

    def controlling_the_tv(self, selected_tv, tv_name):
        # Loop for controlling the selected TV and its channel or volume
        while True:
            print(f"\nControlling the {tv_name}. Choose an action: \n"
                  " 1. Increase Channel \n"
                  " 2. Decrease Channel \n"
                  " 3. Set Channel \n"
                  " 4. Increase Volume \n"
                  " 5. Decrease Volume \n"
                  " 6. Set Volume \n"
                  " 7. Back to TV Selection")

            action_choice = input("Enter your choice (1-5): ")

            # Performing the action
            try:
                if action_choice == '1':
                    selected_tv.channel_up()
                elif action_choice == '2':
                    selected_tv.channel_down()
                elif action_choice == '3':
                    # Set a specific channel
                    try:
                        new_channel = int(input("Enter the channel (1-120): "))
                        if new_channel > 121 or new_channel < 0:
                            print("Invalid input. Please enter 1-7 only.")
                            continue
                        selected_tv.set_channel(new_channel)
                    except ValueError:
                        print("Invalid input. Please enter 1-120 only.")
                        continue
                elif action_choice == '4':
                    selected_tv.volume_up()
                elif action_choice == '5':
                    selected_tv.volume_down()
                elif action_choice == '6':
                    # Enters a specific volume
                    try:
                        entered_volume = int(input("Enter the volume: "))
                        if entered_volume > 7 or entered_volume < 0:
                            print("Invalid input. Please enter 1-7 only.")
                            continue
                        else:
                            selected_tv.set_volume(entered_volume)
                    except ValueError:
                        print("Invalid input. Please enter 1-7 only.")
                        continue
                elif action_choice == '7':
                    continue
                else:
                    print("Invalid input. Please enter 1-7 only.")
                    continue
            except ValueError:
                print("Invalid input. Please enter 1-5 only.")
                continue

            # Print the channel and volume level of the two TV OBJECT
            self.display_tv_status(selected_tv, tv_name)
            continue
