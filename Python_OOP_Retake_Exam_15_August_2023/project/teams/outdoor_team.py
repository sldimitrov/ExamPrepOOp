from project.teams.base_team import BaseTeam



class OutdoorTeam(BaseTeam):
    INITIAL_BUDGET = 1000.0  # EUR
    INCREMENT_ADVANTAGE = 115
    TYPE_ = 'OutdoorTeam'

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=self.INITIAL_BUDGET)

    def win(self):
        self.advantage += self.INCREMENT_ADVANTAGE
        self.wins += 1
