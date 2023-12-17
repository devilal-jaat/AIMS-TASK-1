class OneHotEncoder:
    def __init__(self):
        self.categories = {}

    def fit(self, data):
        unique_values = set()
        for row in data:
            unique_values.update(row)

        self.categories = {value: i for i, value in enumerate(unique_values)}

    def transform(self, data):
        num_samples = len(data)
        num_categories = len(self.categories)

        one_hot_encoded = [[0] * num_categories for _ in range(num_samples)]

        for i, row in enumerate(data):
            for value in row:
                if value in self.categories:
                    one_hot_encoded[i][self.categories[value]] = 1

        return one_hot_encoded

    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)
