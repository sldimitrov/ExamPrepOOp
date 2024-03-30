from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    INITIAL_BUDGET = 500.0  # EUR
    INCREMENT_ADVANTAGE = 145
    TYPE_ = 'IndoorTeam'

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, budget=self.INITIAL_BUDGET)

    def win(self):
        self.advantage += self.INCREMENT_ADVANTAGE
        self.wins += 1
