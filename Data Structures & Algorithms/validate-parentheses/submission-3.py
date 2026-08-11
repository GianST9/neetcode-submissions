class Solution:
    def isValid(self, s: str) -> bool:
        order = []

        for c in s:
            if c in "([{":
                order.append(c)

            elif c in ")]}":
                if not order:
                    return False

                if c == ")" and order[-1] == "(":
                    order.pop()
                elif c == "]" and order[-1] == "[":
                    order.pop()
                elif c == "}" and order[-1] == "{":
                    order.pop()
                else:
                    return False

        return len(order) == 0