# lib/helpers.py
from models.team import Team


def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()


def list_teams():
    """List all basketball teams."""
    teams = Team.get_all()
    for team in teams:
        print(f"Name: {team.name}, Division: {team.division}")

# hellofeofwe