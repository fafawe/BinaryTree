# 9 552
# s = '2' * 247
# while '222' in s or '555' in s:
#     if '222' in s:
#         s = s.replace('222', '5', 1)
#     else:
#         s = s.replace('555', '2', 1)
# print(s)
# 11
# s = '>' + '1' * 25 + 17*'2'+10*'3'
# while '>1' in s or '>2' in s or '>3' in s:
#     if '>1' in s:
#         s = s.replace('>1', '22>3', 1)
#     if '>2' in s:
#         s = s.replace('>2', '2>', 1)
#     if '>3' in s:
#         s = s.replace('>3', '11>2', 1)
# print(s.count('1')*1+s.count('2')*2+s.count('3')*3)
# s = 30*'4'+30*'53'
# while '43' in s or '53' in s:
#     if '43' in s:
#         s = s.replace('43', '33', 1)
#   else:
#         s = s.replace('53', '433', 1)
#
# print(s.count('3'))
# s = 116*'7'
# while '333' in s or '777' in s:
#     if '333' in s:
#         s = s.replace('333', '77', 1)
#     else:
#         s = s.replace('7777', '3', 1)
#
# print(s)
# s = '0' + '1' * 50 + 50*'2'
# while '01' in s or '02' in s or '03' in s:
#     if '01' in s:
#         s = s.replace('01', '2023', 1)
#     if '02' in s:
#         s = s.replace('02', '310', 1)
#     if '03' in s:
#         s = s.replace('03', '1302', 1)
# # print(s.count('1')*1+s.count('2')*2+s.count('3')*3)
# print(sum(int(i)for i in s))

# s = '23' + '2'*49+49*'3'
# while '3222' in s or '23' in s :
#     if '3222' in s:
#         s = s.replace('3222', '322', 1)
#     else:
#         s = s.replace('23', '2', 1)
# # print(s.count('1')*1+s.count('2')*2+s.count('3')*3)
# print(sum(int(i)for i in s))
# 21
# def prostoe(x):
#     for d in range(2, int(x ** 0.5) + 1):
#         if x % d == 0:
#             return False
#     return True
#
#
# for n in range(1, 10000):
#     s = '>' + '0' * 39 + '1' * n + '2' * 39
#     while '>1' in s or '>2' in s or '>0' in s:
#         if '>1' in s:
#             s = s.replace('>1', '22>', 1)
#         if '>2' in s:
#             s = s.replace('>2', '2>', 1)
#         if '>0' in s:
#             s = s.replace('>0', '1>', 1)
#     sc = sum(int(i) for i in s if i.isdigit())
#     if prostoe(sc):
#         print(n)
#         break
# s = 30*'23'+30*'1'
# while '21' in s or '23' in s :
#     if '21' in s:
#          s = s.replace('21', '11', 1)
#     else:
#          s = s.replace('23', '21', 1)
# # print(s.count('1'))
# s = 100*'1'
# while '111' in s or '88888' in s :
#     if '111' in s:
#          s = s.replace('111', '88', 1)
#     else:
#          s = s.replace('88888', '8', 1)
# print(s)

# s = 86*'8'
# while '1111' in s or '8888' in s :
#     if '1111' in s:
#          s = s.replace('1111', '8', 1)
#     else:
#          s = s.replace('8888', '11', 1)
# print(s)
# s = 96*'9'
# while '22222' in s or '9999' in s :
#     if '22222' in s:
#          s = s.replace('22222', '99', 1)
#     else:
#          s = s.replace('9999', '2', 1)
# print(s)

# mx=0
# for n in range(4, 10000):
#     s = '1' + '2' * n
#     while '12' in s or '322' in s or '222' in s:
#         if '12' in s:
#             s = s.replace('12', '2', 1)
#         if '322' in s:
#             s = s.replace('322', '21', 1)
#         if '222' in s:
#             s = s.replace('222', '3', 1)
#     sc = sum(int(i) for i in s if i.isdigit())
#     if mx<sc:
#         mx=sc
# print(mx)
# 8
# s = '8' * 68
# while '222' in s or '888' in s:
#     if '222' in s:
#         s = s.replace('222', '8', 1)
#     else:
#         s = s.replace('888', '2', 1)
# print(s)
# 10

# s = '1' * 50 + 50*'2'+50*'3'
# while '12' in s or '32' in s or '31' in s:
#     if '12' in s:
#         s = s.replace('12', '21', 1)
#     if '32' in s:
#         s = s.replace('32', '23', 1)
#     if '31' in s:
#         s = s.replace('31', '13', 1)
# print(s[20]+' '+s[80]+' '+s[120]+' ')
# print(s)

# 12
# for n in range(1,100):
#     s = n*'3'
#     while '333' in s :
#         # if '333' in s:
#             s = s.replace('333', '4', 1)
#         # else:
#             s = s.replace('4444', '3', 1)
#     if s=='43' :
#         print(n)
# 12
# s = 29*'5'+6*'4'+17*'43'
# while '43' in s or '53' in s :
#     if '43' in s:
#         s = s.replace('43', '33', 1)
#     else:
#         s = s.replace('53', '433', 1)
# print(s.count('3'))
# 16
# s = 89*'Y'
# while 'YYYY' in s or 'XX' in s:
#     if 'YYYY' in s:
#         s = s.replace('YYYY', 'XYX', 1)
#     else:
#         s = s.replace('XX', 'Y', 1)
# print(s)
# 18
# for n in range(100,10000):
#     s = n*'2'
#     while '22222' in s or '111' in s:
#         # if '333' in s:
#             s = s.replace('22222', '11', 1)
#         # else:
#             s = s.replace('111', '22', 1)
#     if len(s)<3:
#         print(n)
#         break

# 20

# s = 'O'+'Y'*40+'X'*20+'Z'*10
# while 'OX' in s or 'OY' in s or 'YO' in s or 'XO' in s:
#     if 'OX' in s:
#         s = s.replace('OX', '2O', 1)
#     else:
#         s = s.replace('XO', 'O3', 1)
#     if 'OY' in s:
#         s = s.replace('OY', '4O', 1)
#     else:
#         s = s.replace('YO', 'O2', 1)
# print(sum(int(i) for i in s if i.isdigit()))

# 22
# for n in range(4,10000):
#     s = '3'+n*'5'
#     while '25' in s or '355' in s or '555' in s:
#         if '25' in s:
#             s = s.replace('25', '32', 1)
#         # else:
#         if '355' in s:
#             s = s.replace('355', '25', 1)
#         if '555' in s:
#             s = s.replace('555', '3', 1)
#     if sum(int(i) for i in s)==17:
#         print(n)
#         break

# 26

# s = '8'*70
# while '2222' in s or '8888' in s :
#     if '2222' in s:
#         s = s.replace('2222', '88', 1)
#     else:
#         s = s.replace('8888', '22', 1)
# print(s)

# 28
# s = '9'*84
# while '33333' in s or '999' in s :
#     if '33333' in s:
#         s = s.replace('33333', '99', 1)
#     else:
#         s = s.replace('999', '3', 1)
# print(s)

# 30
# for n in range(4,10000):
#     s = '5'+n*'2'
#     while '72' in s or '522' in s or '2222' in s:
#         if '72' in s:
#             s = s.replace('72', '2', 1)
#         # else:
#         if '522' in s:
#             s = s.replace('522', '27', 1)
#         if '2222' in s:
#             s = s.replace('2222', '5', 1)
#     if sum(int(i) for i in s)==63:
#         print(n)
#         break
# 32
for n in range(4,10000):
    s = '1'+n*'8'
    while '18' in s or '388' in s or '888' in s:
        if '18' in s:
            s = s.replace('18', '8', 1)
        # else:
        if '388' in s:
            s = s.replace('388', '81', 1)
        if '888' in s:
            s = s.replace('888', '3', 1)
    if s.count('1')==3:
        print(n)
        break





