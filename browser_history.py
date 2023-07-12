class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.prev = []

    def visit(self, url: str) -> None:
        self.stack.append(url)
        self.prev = []

    def back(self, steps: int) -> str:
        if steps > len(self.stack) - 1:
            steps = len(self.stack) - 1

        for _ in range(steps):
            abandoned_page = self.stack.pop()
            self.prev.append(abandoned_page)

        return self.stack[-1]

    def forward(self, steps: int) -> str:
        if steps > len(self.prev):
            steps = len(self.prev)

        for _ in range(steps):
            comeback_page = self.prev.pop()
            self.stack.append(comeback_page)

        return self.stack[-1]


if __name__ == '__main__':
    s = BrowserHistory('leetcode.com')
    s.visit('google.com')
    s.visit('facebook.com')
    s.visit('youtube.com')
    print(s.back(1))
    print(s.back(1))
    print(s.forward(1))
    s.visit('linkedin.com')
    print(s.forward(2))
    print(s.back(2))
    print(s.back(7))