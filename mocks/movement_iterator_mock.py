class EaseCounter:
    def __init__(self, steps):
        self.steps = steps
        self.current = 0

    def __iter__(self):
        return self

    def next(self): # Python 3: def __next__(self)
        # print(self.current, ">", self.steps.size)
        if self.current >= self.steps.size:
            raise StopIteration
        else:
            self.current += 1
            return self.steps[self.current - 1]
