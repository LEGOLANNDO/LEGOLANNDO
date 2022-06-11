import atai
import os

while True:
    a2 = input("問題:")
    b2 = input("答え:")
    with open('./他教科/他教科-問題自動生成.py', mode='a', encoding='utf-8') as f:
        f.write("            elif b == " + str(atai.b) + ":\n")
        f.write("                toi('" + a2 + "', '" + b2 + "')\n")
    atai.b = atai.b + 1
    with open('./他教科/atai.py', mode='w') as f:
        f.write("b = " + str(atai.b))
    d2 = input("続けて追加しますか？(Y/N):")
    if d2 == 'N':
        break
    else:
        atai.b + 1