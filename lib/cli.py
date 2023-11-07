# lib/cli.py

from helpers import (
    exit_program,
    list_teams,
    list_players,
    find_team_by_name,
    find_team_by_id
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
        elif choice == "4":
            find_team_by_id()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all the players")
    print("2. List all the teams")
    print("3. Find team by name.")
    print("4. Find team by id.")


if __name__ == "__main__":
    main()
