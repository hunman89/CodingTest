from itertools import permutations

def solution(command, buttons, scores):
    answer = []
    sum_score = 0
    answer.append(len(command))
    for i in list(permutations(buttons,len(buttons))): # 순열   
        tmp_command = command
        for j in i:
            if j in tmp_command:
                sum_score += scores[buttons.index(j)]
                tmp_command = tmp_command.replace(j,'')
        sum_score += len(tmp_command)
        answer.append(sum_score)
        sum_score = 0
    return max(answer)

def solution2(command, buttons, scores):
    answer = []
    sum_score = 0
    answer.append(len(command))
    def perm(list, n): # 재귀로 순열 구현
        permutations = []
        if n == 1:
            for i in list:
                permutations.append([i])
        for i in range(len(list)):
            next_list = [i for i in list]
            next_list.remove(list[i])
            for p in perm(next_list, n-1):
                permutations.append([list[i]] + p)
        return permutations
    
    for i in perm(buttons,len(buttons)):    
        tmp_command = command
        for j in i:
            if j in tmp_command:
                sum_score += scores[buttons.index(j)]
                tmp_command = tmp_command.replace(j,'')
        sum_score += len(tmp_command)
        answer.append(sum_score)
        sum_score = 0
    return max(answer)

#command = "ABCXYZ"
#buttons = ["BCXY"]
#scores = [2] #6
#command = "ABCXYZ"
#buttons = ["AB","CX","YZ"]
#scores = [4,4,4] # 12
command = "ABCXYZ"
buttons = ["ABC","CXY","YZ"]
scores = [4,5,4] # 9
#command = "<v>AB^CYv^XAZ"
#buttons = ["v>AB^CYv^XA", "<v>A", "^XAZ", "Yv^XA", ">AB^"]
#scores = [50,18,20,30,25] # 59

print(solution(command, buttons, scores))
print(solution2(command, buttons, scores))


'''
def solution(command, buttons, scores):
    answer = []
    sum_score = 0
    
    def search(command, buttons, sum_score):
        tmp_command = command[:]
        tmp_buttons = buttons[:]        
        if not tmp_buttons:
            sum_score += len(command)
            answer.append(sum_score)
            sum_score = 0
            return
        for i in range(len(tmp_buttons)):
            if tmp_buttons[i] in tmp_command:
                sum_score += scores[buttons.index(tmp_buttons[i])]
                tmp_command = tmp_command.replace(tmp_buttons[i],'')
            tmp_buttons.pop(i)
            print(tmp_buttons)
            search(tmp_command, tmp_buttons, sum_score)

    search(command, buttons, sum_score)
    return answer

#command = "ABCXYZ"
#buttons = ["BCXY"]
#scores = [2]
command = "<v>AB^CYv^XAZ"
buttons = ["v>AB^CYv^XA", "<v>A", "^XAZ", "Yv^XA", ">AB^"]
scores = [50,18,20,30,25]
print(solution(command, buttons, scores))
'''




'''
def solution(command, buttons, scores):    
    answer = 0    
    priority = []
    
    for i in range(len(buttons)): # 스킬의 단위 길이당 점수
        priority.append([scores[i]/len(buttons[i]),i])
    priority.sort(reverse=True) # 내림차순 정렬
    
    for i in range(len(buttons)):
        # 단위 길이당 점수가 1보다 높고, 커맨드에 존재한다면
        if priority[i][0] > 1 and buttons[priority[i][1]] in command: 
            answer += scores[priority[i][1]] # 점수 추가
            command = command.replace(buttons[priority[i][1]],'') # 커맨드에서 삭제
            
    answer += len(command) # 남은 커맨드 점수로 환산
    return answer
'''
'''
    def solution(command, buttons, scores):    
    for i in range(len(scores)):
        if scores[i] < len(buttons[i]):
            scores[i] = len(buttons[i])
    
    score_list = []
    selected = []
    
    tmp = command
    for i in range(len(buttons)):
        command = tmp
        if buttons[i] in command:
            command = command.replace(buttons[i],'')
            tmp2 = command
            for j in range(0, len(buttons)):
                command = tmp2
                if buttons[j] in command:
                    command = command.replace(buttons[j],'')
                    score_list.append(scores[i] + scores[j] + len(command))
                    selected.append(buttons[i] + buttons[j] + '' + command)
                else:
                    score_list.append(scores[i] + len(tmp2))
                    selected.append(buttons[i])
    
    if not selected:
        return len(tmp)
    else:
        return max(score)
'''