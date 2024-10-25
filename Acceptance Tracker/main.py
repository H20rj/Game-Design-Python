#Main Acceptance tracker Script
from library import *
import time
from colorama import Fore, init

# Initialize colorama for coloring in terminal
init(autoreset=True)


def main():
    opening()
    authenticate = authentication()
    while not authenticate:
        print("Incorrect username or password. Please try again.")
        authenticate = authentication()
    is_running = True
    load_status()

    while is_running and authenticate:
        print(Fore.CYAN + """
        ╔═════════════════════════════════════════╗
        ║       What would you like to do?        ║
        ╠═════════════════════════════════════════╣
        ║     1. View status                      ║
        ║     2. Change status                    ║
        ║     3. Save and exit                    ║
        ║     4. Reset to defaults                ║
        ║     5. Change password                  ║
        ╚═════════════════════════════════════════╝

        """)

        user_choice = input(Fore.YELLOW + "Enter your choice (1/2/3/4/5): ")
        print("")

        while user_choice not in ["1", "2", "3", "4", "5"]:
            print(Fore.RED + "Invalid input.")
            user_choice = input(Fore.YELLOW + "Enter your choice (1/2/3/4/5): ")

        if user_choice == "1":
            print(Fore.CYAN + "Viewing status...")
            time.sleep(0.75)
            view_status()

        elif user_choice == "2":
            print(Fore.CYAN + "Loading change_status UI...")
            time.sleep(0.75)
            change_status()
            print(Fore.GREEN + "Status is now:")
            print("")
            view_status()

        elif user_choice == "3":
            print(Fore.CYAN + "Saving...")
            time.sleep(1)
            save_status()
            print(Fore.CYAN + "Exiting...")
            break

        elif user_choice == "4":
            print(Fore.CYAN + "Resetting to default...")
            time.sleep(1)
            default()
            print(Fore.GREEN + "Reset complete.")

        elif user_choice == "5":
            print("Opening password change UI...")
            time.sleep(0.75)
            set_user_pw()

        user_pick = input(Fore.YELLOW + "Would you like another action? (Y/N): ").lower()

        while user_pick not in ["y", "n"]:
            print(Fore.RED + "Invalid input.")
            user_pick = input(Fore.YELLOW + "Would you like another action (Y/N): ").lower()

        if user_pick == "n":
            print(Fore.CYAN + "Saving...")
            save_status()
            time.sleep(1)
            print(Fore.CYAN + "Exiting...")
            is_running = False


if __name__ == "__main__":
    main()
