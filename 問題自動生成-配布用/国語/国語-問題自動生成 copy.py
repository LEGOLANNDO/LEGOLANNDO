import random
import atai
import sys
a = int(input('出題数:'))

mistake = []
done_list = []

def a1():
    print("正解")

def a2(da1, db1):
    print("不正解　(正解は " + da1 + " )")
    mistake.append(db1)

def b2(db1, da1):
    print("不正解　(正解は " + db1 + " )")
    mistake.append(da1)

def a3(da2, db2, dc2):
    print("不正解　(正解は " + da2 + " または " + db2 + " )")
    mistake.append(dc2)

def b3(da2, db2, dc2):
    print("不正解　(正解は " + dc2 + " )")
    mistake.append(da2 + "・" + db2)

def toi(da1, db1):
    c = random.randint(1, 2)
    if c == 1:
        d = input(db1 + ':')
        if d == da1:
            a1()
        else:
            a2(da1, db1)
    else:
        d = input(da1 + ':')
        if d == db1:
            a1()
        else:
            b2(db1, da1)

rb = atai.b - 1
rb2 = rb - 1
ab = a - 2
f = 0

for i in range(a):
    while True:
        b = random.randint(1, rb)

        if b not in done_list:
            done_list.append(b)
            if a > rb:
                if len(done_list) > ab:
                    print("間違えた問題：" + str(mistake))
                    sys.exit()
            if len(done_list) > a:
                print("間違えた問題：" + str(mistake))
                sys.exit()
            elif len(done_list) > rb2:
                a = a - rb
                done_list = []

