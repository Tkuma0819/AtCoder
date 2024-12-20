'''
#リストの作成方法１
lis = list("文字列")
print(lis)
#リストの作成方法２
lis = [12,"as"]
print(lis)
'''


'''
lis = []
# 要素の追加方法1
lis.append("hello")
print(lis)
# 要素の追加方法2 「＋」を使い追加する 「＋」と「＝」の間は開けない
lis += ["hi"]
print(lis)

ans = []
ans += ['ボルシャック']
ans += ['・']
ans += ['ドラゴン']
print(ans)
aru = (ans)
print(aru)
# 参照
print(lis[0])
# 参照の開始と終了を指定
print(lis[0:2])
# 参照の開始、終了、間隔を指定
print(lis[0:6:2])

# 要素の削除
lis.pop(0)
print(lis)
'''
'''
a = input().split()
print(a)
b = list(a)
print(b)
'''
'''
lis = []
# 要素の追加方法1
lis.append("hello")
# 要素の追加方法2
lis += ["hi"]

# 参照の開始、終了、間隔を指定
print(lis[0:2:2])
'''
'''
aaa = [1,2,3,4,5,6,7,8,9,10]
print(aaa[0:10:2])
'''
'''
lis = []
# 要素の追加方法1
lis.append("hello")
# 要素の追加方法2
lis += ["hi"]
print(lis)
print(lis[0:2:2])
'''
a = [1,2,3,4,5,6,7,8,9,10]
b = a[1:]
c = a[::2]
d = a[:2:]
print(b)
print(c)
print(d)