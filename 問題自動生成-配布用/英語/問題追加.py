import atai
import os

while True:
    print("1=日本語1:英語1, 2=日本語2:英語1, 3=英語2:日本語1")
    a = input("選択:")
    if a == '1':
        a2 = input("日本語:")
        b2 = input("英語:")
        with open('./英語/英語-問題自動生成.py', mode='a', encoding='utf-8') as f:
            f.write("            elif b == " + str(atai.b) + ":\n")
            f.write("                toi('" + a2 + "', '" + b2 + "')\n")
        atai.b = atai.b + 1
        with open('./英語/atai.py', mode='w') as f:
            f.write("b = " + str(atai.b))
        d2 = input("続けて追加しますか？(Y/N):")
        if d2 == 'N':
            break
        else:
            atai.b + 1
    elif a == '2':
        a2 = input("日本語:")
        b2 = input("日本語:")
        c2 = input("英語:")
        with open('./英語/英語-問題自動生成.py', mode='a', encoding='utf-8') as f:
            f.write("            elif b == " + str(atai.b) + ":\n")
            f.write("                toi2('" + a2 + "', '" + b2 + "', '" + c2 + "')\n")
        atai.b = atai.b + 1
        with open('./英語/atai.py', mode='w') as f:
            f.write("b = " + str(atai.b))
        d2 = input("続けて追加しますか？(Y/N):")
        if d2 == 'N':
            break
        else:
            atai.b + 1
    elif a == '3':
        a2 = input("英語:")
        b2 = input("英語:")
        c2 = input("日本語:")
        with open('./英語/英語-問題自動生成.py', mode='a', encoding='utf-8') as f:
            f.write("            elif b == " + str(atai.b) + ":\n")
            f.write("                toi2('" + a2 + "', '" + b2 + "', " + c2 + ")\n")
        atai.b = atai.b + 1
        with open('./英語/atai.py', mode='w') as f:
            f.write("b = " + str(atai.b))
        d2 = input("続けて追加しますか？(Y/N):")
        if d2 == 'N':
            break
        else:
            atai.b + 1