class Hello:
    def __init__(self):
        self.name = 'Skill Test taker'

    def set_name(self, name):
        self.name = name

    def run(self):
        print('Hello {}!'.format(self.name))

h = Hello()
h.run()

h.set_name('Sharon')
h.run()
