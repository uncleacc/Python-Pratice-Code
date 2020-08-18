import random

name="Uncleacc"
password="601162956"
print("*"*30,"\n","欢迎来到澳门赌场","\n","*"*30)
while(1):
    c=input('您是否要开始游戏？y/n？  ')
    if(c=='y'):
        print("请输入您的用户名及密码！")
        cnt=0
        while(cnt<=3):
            cnt+=1
            nm=input("用户名：")
            pw=input("密码：")
            if(nm==name and pw==password):
                print("欢迎进入澳门赌场系统！！！")
                print('您的初始余额为20元，每次进行对局都需要花费您10元余额，输光为止，当然您也可以充值余额，但是充值余额必须为50的倍数')
                print('-'*10,"Have a good time",'-'*10)
                money=20
                while(money):
                    money-=10
                    num=random.randint(1,11)
                    print("本轮游戏开始！")
                    print('请猜一个1到10之间的数，1次猜中您可以得到20元奖励，2到3次猜中您可以得到10元奖励，超过3次则本轮游戏结束')
                    cnt2=0
                    flag=0
                    while(cnt2<=2):
                        cnt2+=1
                        your=int(input("请输入您猜的数字： "))
                        if(your==num):
                            flag=1
                            break
                        elif(your>num):
                            print("您猜大了！")
                        else:
                            print("您猜小了！")
                    if(flag==1 and cnt2==1):
                        money+=20
                        print("恭喜您一次即中，获得20元奖励")
                    elif(flag==1 and (cnt2==2 or cnt2==3)):
                        money+=10
                        print("恭喜您花了{}次猜中，获得10元奖励".format(cnt2))
                    else:
                        print("十分遗憾，本轮您无法获取金额")
                    if(money<=0):
                        print("您的金额已经为0，您是否选择充值？")
                        c3=input("y/n? ")
                        if(c3=='y'):
                            while(1):
                                tmp=int(input("请输入您要充值的金额："))
                                if(tmp<=0 or tmp%50):
                                    print("您输入格式有误！必须是50的倍数请重新输入！")
                                else:
                                    money+=50
                                    print("充值成功！现在您账户余额为：{}！".format(money))
                                    break
                        else:
                            print("欢迎下次再来！")
                            break
                    while(1):
                        c2=input("您是否要继续游戏？y/n:  ")
                        if(c2=='n'):
                            if(money>20):
                                print("恭喜您赚到了{}元".format(money-20))
                            elif(money<20):
                                print("很不幸，您赔了{}元".format(20-money))
                            else:
                                print("不幸的是您今天一无所获，庆幸的是您获得了我们免费给您的20元基本金")
                            break
                        elif(c2!='y'):
                            print("您输入格式有误！")
                        else:
                            break
                    if(c2=='n'):
                        break
                break
            else:
                print('抱歉，您输入的密码有误！请重新输入！')
            if(cnt>=3):
                print('您输入错误次数超过3次，请停10秒钟后再重新输入')
                for i in range(1,11):
                    print(i)
        break
    elif(c=='n'):
        print('好的，欢迎下次再来')
        break
    else:
        print("您输入格式有误！")