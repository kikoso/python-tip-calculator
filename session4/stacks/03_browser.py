# Exercise: browser back button with a history stack


class Browser:
    def __init__(self, start):
        self.current = start
        self.history = []

    def visit(self, url):
        self.history.append(self.current)
        self.current = url

    def back(self):
        if self.history:
            self.current = self.history.pop()
        return self.current


b = Browser("hdbw.de")
b.visit("moodle.de")
b.visit("python.org")
print(b.back())
print(b.back())
print(b.back())
