class Base10:
    def __init__(self, *digits):
        total = 0
        for power, digit in enumerate(reversed(digits)):
            total += (10 ** power) * digit
        self._number = total
    
    @property
    def number(self):
        return self._number

def fix_symmetry_endpoints(func):
    cache = {}
    def with_fixed_endpoints(digits):
        for symmetry in func(digits):
            print(symmetry)
            symmetry[0] = True
            t = tuple(symmetry)
            if t in cache:
                pass
            else:
                cache[t] = True
                yield t
    return with_fixed_endpoints
                
            
@fix_symmetry_endpoints
def generate_symmetries(digits):
    if digits == 1:
        yield [False]
        yield [True]
    elif digits == 2:
        yield [False, False]
        yield [True, True]
    elif digits == 3:
        yield [False, False, False]
        yield [False, True, False]
        yield [True, True, True]
    else:
        for symmetry in generate_symmetries(digits - 2):
            false_case = [False * digits]
            for i, value in enumerate(symmetry):
                false_case[i + 1] = value
                yield false_case
        for symmetry in generate_symmetries(digits - 2):
            true_case = [True * digits]
            for i, value in enumerate(symmetry):
                true_case[i + 1] = value
                yield true_case

def get_symmetries():
    digits = 1
    while True:
        yield from generate_symmetries(digits)
        digits += 1

for i, symmetry in enumerate(get_symmetries()):
    if i > 10:
        break
    print(i, symmetry)