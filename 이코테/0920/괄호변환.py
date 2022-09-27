def seperate(p):
    open_p, close_p = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[:i + 1], p[i + 1:]


def correct(u):
    if_open = []

    for p in u:
        if p == '(':
            if_open.append(p)
        else:
            if not if_open:
                return False
            if_open.pop()

    return True


def solution(p):

    if not p:
        return p

    u, v = seperate(p)

    if correct(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for i in u[1:len(u) - 1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('

    return answer
