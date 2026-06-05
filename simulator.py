class AlephOlamSimulator:

    def __init__(self):
        self.state = {}

    def initialize(self):
        self.state["initialized"] = True

    def run(self):
        return self.state
