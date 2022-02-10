sens = list()
while True:
    sen = input()
    if sen=='.':
        break
    else:
        sens.append(sen)

for sen in sens:
    brackets = list()
    ans='yes'
    for s in sen:
        if s=='(':
            brackets.append(s)
            continue
        elif s=='[':
            brackets.append(s)
            continue
        elif s==')':
            if len(brackets)>=1:
                if ord(s)==ord(brackets.pop())+1:
                    continue
                else:
                    ans='no'
                    break
            else:
                ans='no'
                break
        elif s==']':
            if len(brackets)>=1:
                if ord(s)==ord(brackets.pop())+2:
                    continue
                else:
                    ans='no'
                    break
            else:
                ans='no'
                break
        else:
            continue          
    if '(' in brackets:
        ans = 'no'
    elif '[' in brackets:
        ans = 'no'
    else:
        pass
    print(ans)

