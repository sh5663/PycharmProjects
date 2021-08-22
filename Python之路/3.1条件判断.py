

#coding = utf-8
'''
# 3.1.1通过比较运算符做判断
final_score = input('请输入你的CCNA考试成绩： ')
if int (final_score) > 811:
    print('恭喜你通过考试')
elif int(final_score) == 811:
    print('恭喜你一下通过考试')
else:
    print('成绩不及格')
'''



# #3.1.2通过字符串方法+逻辑运算符做判断
# print('''请根据对应号码选择一个路由协议：
# 1.RIP
# 2.IGRP
# 3.EIGRP
# 4.OSPF
# 5.ISIS
# 6，BGP''')
# option = input('请输入你的选项（数字1-6）： ')
# if option.isdigit() and 1 <= int(option)<=6:
#     if option == '1' or option == '2' or   option == '3':
#         print('该路由协议属于距离矢量路由协议')
#     elif option == '4' or option == '5':
#         print('该路由协议属于链路状态路由协议')
#     else:
#         print('该路由协议属于路径矢量路由协议')
# else:
#     print('选项无效，程序终止')



# # 3.1.3 通过成员运算符作判断
# print('''请根据对应号码选择一个路由协议：
# 1.RIP
# 2.IGRP
# 3.EIGRP
# 4.OSPF
# 5.ISIS
# 6，BGP''')
# option = input('请输入你的选项（数字1-6）： ')
# if option.isdigit() and int(option) in list(range(1,7)):
#     if int(option) in list(range(1,4)):
#         print('该路由协议属于距离矢量路由协议')
#     elif int(option) in list (range(4,6)):
#         print('该路由协议属于链路状态路由协议')
#     else:
#         print('该路由协议属于路径矢量路由协议')
# else:
#     print('选项无效，程序终止')


# # 3.2.1 通过成员运算符作循环判断
# print('''请根据对应号码选择一个路由协议：
# 1.RIP
# 2.IGRP
# 3.EIGRP
# 4.OSPF
# 5.ISIS
# 6，BGP''')
# while True:
#     option = input('请输入你的选项（数字1-6）： ')
#     if option.isdigit() and int(option) in list(range(1,7)):
#         if int(option) in list(range(1,4)):
#             print('该路由协议属于距离矢量路由协议')
#         elif int(option) in list (range(4,6)):
#             print('该路由协议属于链路状态路由协议')
#         else:
#             print('该路由协议属于路径矢量路由协议')
#         break
#     else:
#         print('选项无效，程序终止')

# # 3.2.2
# routing_protocols = ['RIP','IGRP','OSPF','ISIS','BGP','EIGRP']
# link_state_protocols = ['OSPF','ISIS']
# for protocols in routing_protocols:
#     # print(protocols)
#     if protocols not in link_state_protocols:
#         print(protocols + '不属于链路状态路由协议')

#3.4.3 嵌套函数
def squ(x):
    result = x ** 2
    return result
def cube (x):
   result = squ(x) * 2
   return result
cube(3)
print(cube(3))