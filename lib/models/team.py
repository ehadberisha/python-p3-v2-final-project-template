# lib/models/team.py
from models.__init__ import CURSOR, CONN


class Team:

    def __init__(self, name, division, id=None):
        self.id = id
        self.name = name
        self.division = division

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def division(self):
        return self._division

    @division.setter
    def division(self, division):
        if isinstance(division, str) and len(division):
            self._division = division
        else:
            raise ValueError(
                "Division must be a non-empty string"
            )

    @classmethod
    def create_table(cls):
        sql = """
                CREATE TABLE IF NOT EXISTS teams (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                division TEXT
                ) """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Team instances """
        sql = """
            DROP TABLE IF EXISTS teams;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and division values of the current Team instance."""
        sql = """
            INSERT INTO teams (name, division)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.division))
        CONN.commit()

        self.id = CURSOR.lastrowid
        return self

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM teams
        """
        rows = CURSOR.execute(sql).fetchall()
        return rows
    
    @classmethod
    def find_team_by_name(cls, name):
        sql = """
            SELECT *
            FROM teams
            WHERE name is ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return row

    @classmethod
    def find_team_by_id(cls, id):
        sql = """
            SELECT * FROM teams WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return row



    # def find_players(self):
    #     from models.players import Players
    #     sql = """
    #         SELECT * FROM players 
    #         WHERE team = ?
    #     """
    #     CURSOR.execute(sql, (self.team,),)
    #     rows = CURSOR.fetchall()
    #     return rows

