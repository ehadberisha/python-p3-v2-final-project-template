# lib/cli.py

from helpers import (
    exit_program,
    list_teams,
    list_players,
    find_team_by_name
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_players()
        elif choice == "2":
            list_teams()
        elif choice == "3":
            find_team_by_name()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all the players")
    print("2. List all the teams")
    print("3. Find team by name.")


if __name__ == "__main__":
    main()
