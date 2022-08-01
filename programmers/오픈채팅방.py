import sys

def solution(record):
    answer = []
    dict = {}
    
    for i in record:
        if(i.startswith("Enter") or i.startswith("Change")):
            dict[i.split(" ")[1]] = i.split(" ")[2]
            
    for i in record:
        s = ""
        if i.startswith("Enter"):
            s = dict[i.split(' ')[1]] + "님이 들어왔습니다."
            answer.append(s)
        elif i.startswith("Leave"):
            s = dict[i.split(' ')[1]] + "님이 나갔습니다."
            answer.append(s)
        
    return answer