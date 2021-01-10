balloons = [[2,2],[4,4],[1,4],[-1,-4]]

def solution(balloons):
    list1, list2, list3, list4= [], [], [], []
    for balloon in balloons:
        if balloon[0] >= 0 and balloon[1] > 0:
            list1.append(balloon[0]/balloon[1])
        if balloon[0] <= 0 and balloon[1] > 0:
            list2.append(balloon[0]/balloon[1])    
        if balloon[0] <= 0 and balloon[1] < 0:
            list3.append(balloon[0]/balloon[1])
        if balloon[0] >= 0 and balloon[1] < 0:
            list4.append(balloon[0]/balloon[1])
    list1, list2, list3, list4 = set(list1), set(list2), set(list3), set(list4)    
    return len(list1) + len(list2) + len(list3) + len(list4) 
    
print(solution(balloons))