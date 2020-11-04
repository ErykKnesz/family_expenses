import json


class Expenses:
    def __init__(self):
        try:
            with open("expenses.json", "r") as f:
                self.expenses = json.load(f)
        except FileNotFoundError:
            self.expenses = []

    def all(self):
        return self.expenses

    def get(self, id):
        return self.expenses[id - 1]

    def create(self, data):
        if 'csrf_token' in data:
            data.pop('csrf_token')
        try:
            data.setdefault(
                'id', expenses.all()[-1]['id'] + 1)
        except IndexError:
            data.setdefault(
                'id', 1)
        self.expenses.append(data)
        self.save_all()

    def delete(self, id):
        expense = self.get(id)
        if expense:
            self.expenses.remove(expense)
            self.save_all()
            return True
        return False

    def save_all(self):
        with open("expenses.json", "w") as f:
            json.dump(self.expenses, f)

    def update(self, id, data):
        if 'csrf_token' in data:
            data.pop('csrf_token')
        expense = self.get(id)
        if expense:
            index = self.expenses.index(expense)
            self.expenses[index] = data
            self.expenses[index].setdefault('id', id)
            self.save_all()
            return True
        return False


expenses = Expenses()
