def make_uv(str):
    count_left = 0
    count_right = 0

    for i in range(0, len(str)):
        if str[i] == '(':
            count_left += 1
        else:
            count_right += 1
        if count_left == count_right:
            break

    return str[:i+1], str[i+1:]


def check_ok(u):
    count = 0
    check = True

    for i in range(len(u)):
        if u[i] == '(':
            count += 1
        else:
            count -= 1
        if count < 0:  # '('이 ')'보다 적어지면 break
            check = False
            break

    return check


def fix_u(u):
    return result


def solution(p):
    # 1
    if p == "":
        return ''
    # 2
    u, v = make_uv(p)

    # 3
    if check_ok(u) == True:
        return u+solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        reverse_u = u[1:-1]
        for i in range(len(reverse_u)):
            if reverse_u[i] == '(':
                answer += ')'
            else:
                answer += '('

    return answer
