stack = []
PIS_operator = {"(" : 0, "+" : 1, "-" : 1, "*" : 2, "/" : 2, "^" : 3} # 스택에서의 우선 순위
PIE_operator = {"(" : 4, "+" : 1, "-" : 1, "*" : 2, "/" : 2, "^" : 3} # 수식에서의 우선 순위
operator = ["+", "-", "*", "/","(",")","^"]
expression = list(input('수식을 입력하시오 : '))
exp = []
postfix = [] #후위계산법을 담을 리스트

Top = len(stack) - 1 #스택의 Top 설정

def is_empty(stack): # underflow 확인을 위한 함수
    if len(stack) == 0:
        ans = True
    else:
        ans = False
    return ans

for e in range(0, len(expression) - 1): #중위표기식 리스트에서 두자리 이상의 수가 있을 경우 합치기 위함
    if expression[e] not in operator:
        if expression[e + 1] not in operator:
            expression[e + 1] = expression[e] + expression[e + 1]
        else:
            exp.append(expression[e])
    else:
        exp.append(expression[e])
exp.append(expression[-1])

for i in exp: #중위표기식을 후위표기식으로 만드는 반복문
    if is_empty(stack):
        if i in PIE_operator:
            stack.append(i)
        else:
            if i != ")":
                postfix.append(i)
    else:
        if i in PIE_operator:
            if PIE_operator[i] > PIS_operator[stack[Top]]:
                stack.append(i)
            else:
                for s in range(len(stack)):
                    if PIS_operator[stack[Top]] < PIE_operator[i]:
                        stack.append(i)
                    else:
                        postfix.append(stack.pop())
                if not is_empty(stack):
                    if i is not stack[Top]:
                        stack.append(i)
                else:
                    stack.append(i)

        else:
            if i == ")":
                for k in range(len(stack)):
                    if stack[Top] == "(":
                        stack.pop()
                    else:
                        postfix.append(stack.pop())
            else:
                postfix.append(i)


for k in range(len(stack)): #스택에 남은 연산자를 pop시키는 과정
    postfix.append(stack.pop())

print("후위표기법은: ",' '.join(postfix))

for post in postfix:
    if post not in operator:
        stack.append(post)
    else:
        if post == '^':
            post = '**'
        T2 = stack.pop()
        T1 = stack.pop()
        T3 = str(eval(T1 + post + T2))
        stack.append(T3)
print(stack.pop())
