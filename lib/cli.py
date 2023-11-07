#!/usr/bin/env python3

from helpers import list_teams
from seed import seed_database
import os

def main():
    while True:
        print("1. Seed Database")
        print("2. List Teams")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            seed_database()
        elif choice == "2":
            list_teams()
        elif choice == "3":
            exit_program()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()