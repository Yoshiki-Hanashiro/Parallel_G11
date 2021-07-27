import random
#コインの出る回数,確率をシュミレートする
#Aはコインを投げる回数
def coin(A):
    table_count = 0#表が出る回数
    back_count = 0#裏が出る回数

    for i in range(A):
        X = random.randint(0, 1)
        if X == 0:
            table_count += 1
        else:
            back_count += 1

    print("表が{}回出ました,裏が{}回出ました".format(table_count,back_count))
    
    print("今回の事象が起こる確率は{}")





