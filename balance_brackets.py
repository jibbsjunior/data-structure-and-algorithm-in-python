from stack import Stack

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def is_parent_balanced(parent_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(parent_string) and is_balanced:
        parent = parent_string[index]
        if parent in "([{":
            s.push(parent)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, parent):
                    is_balanced = False
                    break
                pass
            pass
        index += 1
        pass
    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print("String : (((({})))) Balanced or not?")
print(is_parent_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_parent_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_parent_balanced("[][]"))
