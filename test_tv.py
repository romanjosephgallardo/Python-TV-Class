from tv_controls import TVController


def main():
    """Main function to run the TV control program."""
    try:
        tv_program = TVController()
        tv_program.select_tv()
    except:
        # Catches any errors
        print("\nAn unexpected error occurred. Stopping the program...")


main()
