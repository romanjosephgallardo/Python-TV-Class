from tv import TV


class TVController:
    """
    A class to represent a TV controller that manages two TVs,
    and specifically made for user-interaction purposes.
    """
    def __init__(self):
        """Initialize two TV objects and turn them on."""
        self.tv_1 = TV()  # TV1 Object
        self.tv_2 = TV()  # TV2 Object
        self.tv_1.turn_on()
        self.tv_2.turn_on()

    def display_tv_status(self, tv, tv_number):
        """Prints the current status of the TV."""
        print(f"{tv_number}'s channel is {tv.get_channel()} and volume level is {tv.get_volume()}".center(50))

    def display_one_tv_status(self, tv, tv_number):
        """Prints the current status of one TV only in a formatted style."""
        print("\n" + "—" * 50)
        self.display_tv_status(tv, tv_number)
        print("—" * 50)

    def display_two_tv_status(self, tv1, name1, tv2, name2):
        """Prints the current status of two TVs in a formatted style."""
        print("\n" + "—" * 50)
        self.display_tv_status(tv1, name1)
        self.display_tv_status(tv2, name2)
        print("—" * 50)

    def display_output_message(self, message):
        """Display formatted message for errors and other outputs."""
        horizontal_border = "—" * 50
        formatted_message = (f"{horizontal_border}\n"
                             f"{message.center(50)}\n"
                             f"{horizontal_border}")
        print(formatted_message)

    def select_tv(self):
        """
        Provides a menu for user to select a TV to control,
        or display a status of the two TV.
        """
        while True:
            # Displays options to user
            print("\n" + "-" * 50)
            print("Choose a TV to control! \n"
                  " 1. TV 1 \n"
                  " 2. TV 2 \n"
                  " 3. Show the two TV status \n"
                  " 4. Exit the program")

            try:
                # Get user's input choice
                tv_choice = int(input("Enter your option (1-4): "))
                if tv_choice == 1:
                    self.controlling_the_tv(self.tv_1, "tv1")
                elif tv_choice == 2:
                    self.controlling_the_tv(self.tv_2, "tv2")
                elif tv_choice == 3:
                    # Display the status of both TVs with format
                    self.display_two_tv_status(self.tv_1, "tv1", self.tv_2, "tv2")
                    continue
                elif tv_choice == 4:
                    self.display_output_message("Thank you for using the program!")
                    break
                else:
                    self.display_output_message("Invalid input. Please enter 1-4 only.")
                    continue
            except ValueError:
                self.display_output_message("Invalid input. Please enter 1-4 only.")
                continue

    def controlling_the_tv(self, selected_tv, tv_name):
        """ Provides a menu for controlling the selected TV and its channel or volume."""
        while True:
            # Display control options to the user
            print("\n" + "-" * 50)
            print(f"Controlling the {tv_name}. Choose an action: \n"
                  " 1. Increase Channel \n"
                  " 2. Decrease Channel \n"
                  " 3. Set Channel \n"
                  " 4. Increase Volume \n"
                  " 5. Decrease Volume \n"
                  " 6. Set Volume \n"
                  " 7. Back to TV Selection")

            action_choice = input("Enter your choice (1-7): ")

            # Performing the action
            try:
                if action_choice == '1':
                    selected_tv.channel_up()  # Increase the channel number
                elif action_choice == '2':
                    selected_tv.channel_down()  # Decrease the channel number
                elif action_choice == '3':
                    # Set a specific channel
                    try:
                        new_channel = int(input("Enter the channel (1-120): "))
                        if new_channel > 121 or new_channel < 0:
                            self.display_output_message("Invalid input. Please enter 1-120 only.")
                            continue
                        else:
                            selected_tv.set_channel(new_channel)
                            self.display_one_tv_status(selected_tv, tv_name)
                            break
                    except ValueError:
                        self.display_output_message("Invalid input. Please enter 1-120 only.")
                        continue
                elif action_choice == '4':
                    selected_tv.volume_up()  # Increase the volume level by 1
                elif action_choice == '5':
                    selected_tv.volume_down()  # Decrease the volume level by 1
                elif action_choice == '6':
                    # Set a specific volume
                    try:
                        entered_volume = int(input("Enter the volume: "))
                        if entered_volume > 7 or entered_volume < 0:
                            self.display_output_message("Invalid input. Please enter 1-7 only.")
                            continue
                        else:
                            selected_tv.set_volume(entered_volume)
                    except ValueError:
                        self.display_output_message("Invalid input. Please enter 1-7 only.")
                        continue
                elif action_choice == '7':
                    # Exit to TV selection menu
                    break
                else:
                    self.display_output_message("Invalid input. Please enter 1-7 only.")
                    continue
            except ValueError:
                self.display_output_message("Invalid input. Please enter 1-5 only.")
                continue

            # Display the current status of the selected TV
            self.display_one_tv_status(selected_tv, tv_name)
            break

