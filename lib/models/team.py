# lib/models/team.py
from models.__init__ import CURSOR, CONN


class Team:

    all = {}

    def __init__(self, name, division, id=None):
        self.id = id
        self.name = name
        self.division = division

    @classmethod
    def create_table(cls):
        pass

    @classmethod
    def drop_table(cls):
        pass

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM teams
        """

        rows = CURSOR.execute(sql).fetchall()
        teams = []

        for row in rows:
            team = cls.instance_from_db(row)
            teams.append(team)

        return teams

    @classmethod
    def list_all_teams(cls):
        pass

    @classmethod
    def create_team(cls, name, division):
        team = cls(name, division)
        team.save()
        return team

    def save(self):
        """ Insert a new row with the name and division values of the current Team instance.
        Update object id attribute using the primary key value of the new row.
        Save the object in a local dictionary using the table row's PK as a dictionary key.
        """
        sql = """
            INSERT INTO teams (name, division)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.division))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def instance_from_db(cls, row):
        """Return a Team object having the attribute values from the table row."""
        # Check the dictionary for an existing instance using the row's primary key
        team = cls.all.get(row[0])
        if team:
            # Ensure attributes match row values in case the local instance was modified
            team.name = row[1]
            team.division = row[2]
        else:
            # Not in the dictionary, create a new instance and add it to the dictionary
            team = cls(row[1], row[2])
            team.id = row[0]
            cls.all[team.id] = team
        return team