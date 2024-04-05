from typing import List

from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan
from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.clients.base_client import BaseClient


class BankApp:
    VALID_LOAN_TYPES = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENT_TYPES = {"Student": Student, "Adult": Adult}
    APPROPRIATE_LOAN_GRANTS = {"Student": "StudentLoan", "Adult": "MortgageLoan"}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOAN_TYPES:
            raise Exception("Invalid loan type!")

        loan = self.VALID_LOAN_TYPES[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENT_TYPES:
            raise Exception("Invalid client type!")
        if len(self.clients) >= self.capacity:
            return f"Not enough bank capacity."

        client = self.VALID_CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self.find_client_by_id(client_id)
        if loan_type != self.APPROPRIATE_LOAN_GRANTS[client.__class__.__name__]:
            raise Exception("Inappropriate loan type!")

        loan = [el for el in self.loans if el.__class__.__name__ == loan_type][0]

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self.find_client_by_id(client_id)
        if client is None:
            return f"No such client!"
        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = [loan.increase_interest_rate() for loan in self.loans
                                   if loan.__class__.__name__ == loan_type]

        return f"Successfully changed {len(number_of_changed_loans)} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_client_rates_number += 1

        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):
        clients_interest_rate = [client.interest for client in self.clients]
        if clients_interest_rate:
            avg_client_interest_rate = sum(clients_interest_rate) / len(clients_interest_rate)
        else:
            avg_client_interest_rate = 0

        total_sum = 0
        total_loans = 0
        for person in self.clients:
            for loan in person.loans:
                total_sum += loan.amount
                total_loans += 1

        result = f"""Active Clients: {len(self.clients)}
Total Income: {sum(client.income for client in self.clients):.2f}
Granted Loans: {total_loans}, Total Sum: {total_sum:.2f}
Available Loans: {len(self.loans)}, Total Sum: {sum([loan.amount for loan in self.loans]):.2f}
Average Client Interest Rate: {avg_client_interest_rate:.2f}"""

        return result

    # Helper method
    def find_client_by_id(self, client_id):
        client = [c for c in self.clients if c.client_id == client_id][0]
        if client:
            return client
        return None
