from collections import Counter

class Matcher:
    RECIPROCALS = {
        ')': '(',
        '}': '{',
        ']': '[',
    }
    
    def __init__(self, expression):
        self._character_stack = []
        self._matched = True
        self._feed(expression)
    
    def _end_match(self, char):
        reciprocal = self.__class__.RECIPROCALS[char]
        if len(self._character_stack) < 1:
            self._matched = False
        elif self._character_stack[-1] != reciprocal:
            self._matched = False
        else:
            res = self._character_stack.pop()
            if not res:
                self._matched = False
            
    def _feed(self, expression):
        for char in expression:
            if char in ('(', '{', '['):
                self._character_stack.append(char)
            else:
                self._end_match(char)
    
    @property
    def matched(self):
        return self._matched and len(self._character_stack) == 0
        
def is_matched(expression):
    return Matcher(expression).matched

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
