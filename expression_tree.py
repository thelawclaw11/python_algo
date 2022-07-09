from abc import ABC, abstractmethod
from typing import List


class Node(ABC):
    left = None
    right = None

    @abstractmethod
    def evaluate(self) -> int:
        pass


class ValNode(Node):
    val = 0
    left = None
    right = None

    def evaluate(self) -> int:
        return self.val


class AddNode(Node):
    def evaluate(self) -> int:
        return self.left.evaluate() + self.right.evaluate()


class SubNode(Node):
    def evaluate(self) -> int:
        return self.left.evaluate() - self.right.evaluate()


class MultNode(Node):
    def evaluate(self) -> int:
        return self.left.evaluate() * self.right.evaluate()


class DivNode(Node):
    def evaluate(self) -> int:
        return self.left.evaluate() // self.right.evaluate()


class TreeBuilder(object):
    def buildTree(self, postfix: List[str]) -> 'Node':

        def F(i):
            if postfix[i].isnumeric():
                node = ValNode()
                node.val = int(postfix[i])
                return node, i - 1

            node = None

            if postfix[i] == "+":
                node = AddNode()
            elif postfix[i] == "*":
                node = MultNode()
            elif postfix[i] == "-":
                node = SubNode()
            elif postfix[i] == "/":
                node = DivNode()

            right, left_index = F(i - 1)
            left, return_index = F(left_index)

            node.right = right
            node.left = left

            return node, return_index

        root = F(len(postfix) - 1)
        return root[0]



tb = TreeBuilder()

# a = tb.buildTree(["3", "4", "+", "2", "*", "7", "/"])
b = tb.buildTree(["4","5","2","7","+","-","*"])
print(b)

print(b.evaluate())

