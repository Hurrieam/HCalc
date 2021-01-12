import math

print("PyCalc Ver 1.0.0.0")
print("by Hurrieam")
print("on 20191229\n")

while True:
    try:
        expression = str(input("请键入数学表达式\n>>"))
        print("\n" + str(expression) + "=" + str(eval(expression)) + "\n")
    except:
        print("您的键入有误，请检查后重新输入！\n")
