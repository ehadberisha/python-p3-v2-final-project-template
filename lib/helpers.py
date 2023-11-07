# lib/helpers.py
from models.team import Team
from models.players import Players

def helper_1():
    print("Performing useful function#1.")


def exit_program():
    print("Goodbye!")
    exit()

def list_teams():
    teams = Team.get_all()
    if len(teams) < 1:
        print("\n No teams in database.")
    print("ID", "\t", '{0: <25}'.format("NAME"), "DIVISION")
    for team in teams:
        print(team[0], "\t", '{0: <25}'.format(team[1]), team[2])
    

def list_players():
    players = Players.get_all()
    if len(players) < 1:
        print("\n No players in database.")
    print("PLAYER ID", "\t", '{0: <25}'.format("NAME"), "TEAM ID")
    for player in players:
        print(player[0], "\t", "\t", '{0: <25}'.format(player[1]), player[2])


def find_team_by_name():
    name_input = input("Type in team's name: ")
    # team_search = Team.find_team_by_name(name_input)
    team_search = Team.find_team_by_name_fuzzy(name_input)
    if len(team_search) < 1:
        print("\n No team found by that name in database. Try typing in a team like in the format Washington Wizards")
    else:
        print(team_search)


def find_team_by_id():
    id_input = input("Enter the team's id: ")
    team_search = Team.find_team_by_id(id_input)
    print(team_search)

    
# def find_players_by_team():
#     players = Players.find_players()
#     team = input("Enter the team name: ")

    
