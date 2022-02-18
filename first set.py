import math

samuel = float(input("pick a lucky number :"))
if samuel >= 10 and samuel <= 50:
    problem = math.sqrt(samuel)
    print(problem)
else:
    print ('Wrong answer !')
