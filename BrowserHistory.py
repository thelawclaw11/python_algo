from collections import deque

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = deque()
        self.history.append(homepage)
        self.current = 0

    def visit(self, url: str) -> None:
        self.history.append(url)
        self.current = len(self.history) - 1

    #
    # def back(self, steps: int) -> str:
    #
    # def forward(self, steps: int) -> str:

bh = BrowserHistory("leetcode.com")
bh.visit("google.com")
bh.visit("facebook.com")
bh.visit("youtube.com")

print(bh.history)
