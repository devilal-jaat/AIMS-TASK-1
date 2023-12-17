class SimpleImputer:
    def __init__(self, strategy='mean'):
        self.strategy = strategy
        self.imputation_values = {}

    def fit(self, data):
        if self.strategy == 'mean':
            self.imputation_values = {j: sum(filter(None, col)) / len(list(filter(None, col))) for j, col in enumerate(zip(*data))}
        elif self.strategy == 'median':
            self.imputation_values = {j: sorted(filter(None, col))[len(list(filter(None, col))) // 2] for j, col in enumerate(zip(*data))}
        elif self.strategy == 'most_frequent':
            self.imputation_values = {j: max(set(filter(None, col)), key=col.count) for j, col in enumerate(zip(*data))}
        else:
            raise ValueError("Invalid imputation strategy. Supported strategies are 'mean', 'median', and 'most_frequent'.")

    def transform(self, data):
        return [[self.imputation_values[j] if value is None else value for j, value in enumerate(row)] for row in data]

    def fit_transform(self, data):
        self.fit(data)
        return self.transform(data)
