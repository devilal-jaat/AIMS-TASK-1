class OrdinalEncoder:
    def __init__(self):
        self.categories = {}

    def fit(self, data):
        unique_values = set()
        for row in data:
            unique_values.update(row)

        self.categories = {value: i for i, value in enumerate(sorted(unique_values))}

    def transform(self, data):
        return [[self.categories[value] for value in row] for row in data]

    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)
