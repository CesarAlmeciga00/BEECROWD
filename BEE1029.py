def answer(a):
    promedio = 127
    answer = "0"
    letters = {
        0:"A",
        1:"B",
        2:"C",
        3:"D",
        4:"E"
    }
    for i in range(len(a)):
        if int(a[i]) <= promedio and answer == "0":
            answer = letters[i]
        elif int(a[i]) <= promedio and answer != "0":
            answer = "*"
        elif answer == "*":
            break
    if answer == "0":
        answer = "*"
    
    return answer


while True:
    cases = int(input())
    if cases==0:break
    for i in range(cases):
        answers = input()
        answers = answers.split()
        print(answer(answers))
        
    
    