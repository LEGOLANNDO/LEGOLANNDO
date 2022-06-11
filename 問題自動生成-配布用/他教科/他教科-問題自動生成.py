import random
import atai
import sys
a = int(input('出題数:'))

mistake = []
done_list = []

def a1():
    print("正解")

def a2(da1, db1):
    print("不正解　(正解は " + db1 + " )")
    mistake.append(da1)

def toi(da1, db1):
    d = input(da1 + ':')
    if d == db1:
        a1()
    else:
        a2(da1, db1)

rb = atai.b - 1
rb2 = rb - 1
ab = a - 2

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

