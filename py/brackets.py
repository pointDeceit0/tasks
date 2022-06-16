def brackets(s: str):
    left, right = [], list(s)[::-1]
    first = [] # first entry of left brackets

    for i in range(1, len(right) + 1):
        el = right.pop()

        if el in {'(', '{', '['}:
            left.append(el)
            first.append(i)
        elif el in {')', '}', ']'}:
            if len(left) == 0:
                return i 

            top = left.pop()
            if  (el != ')' and top == '(') or\
                (el != ']' and top == '[') or\
                (el != '}' and top == '{'):
                return i
            
            first.pop() # delete ind of last left bracket if condition works

    return 'Success' if (not right and not left) else first.pop()


def test():
    assert brackets('([](){([])})') == "Success"
    assert brackets('()[]}') == 5
    assert brackets('{{[()]]') == 7
    assert brackets('[') == 1
    assert brackets(']') == 1
    assert brackets(']') == 1
    assert brackets(']}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}') == 1
    assert brackets('((((((((((((((((((((((((((((((((((((((((((((((') == 46
    assert brackets('{{{[][][]') == 3
    assert brackets('[]([]') == 3
    assert brackets('((({[]})') == 2
    assert brackets('(slkj{lk[lsj]}') == 1

    
def main():
    test()
    print(brackets(input().strip()))
    

if __name__ == "__main__":
    main()