print('-'*40)
print('欢迎进入通讯录管理系统')
print('-'*40)
tip='''
1. 增加姓名和对应手机号码
2. 删除姓名及其对应手机号码
3. 修改手机号码
4. 查询通讯录所有用户数据
5. 查询单个用户
6. 清空通讯录
7. 退出
'''
print(tip)

namelist=[]
numlist=[]
while(1):
    choice=int(input('请输入相应操作对应编号：'))
    if(choice==1):
        print('请输入您要添加的姓名和对应的手机号：\n')
        while(1):
            name=input('姓名:')
            number=input('号码：')
            if(number in numlist):
                print('您输入的号码已经在此通讯录中！请重新输入')
            else:
                namelist.append(name)
                numlist.append(number)
                print('添加成功！')
                break
    elif(choice==2):
        if(not namelist):
            print('通讯录暂时还没有数据哦！')
        else:
            while(1):
                name=input('请输入您要删除的姓名：(输入exit退出)     ')
                number=input('请输入您要删除的姓名对应的号码：(输入exit退出)     ')
                if(name=='exit' and number=='exit'):
                    print('退出成功')
                    break
                else:
                    result=0
                    # 删除操作
                    tmp=-1
                    for i in range(len(namelist)):
                        if(number==numlist[i] and namelist[i]==name):
                            tmp=i
                            result=1
                            break
                    if(result==0):
                        print('您输入的用户不存在！请检查信息是否匹配并重新输入！')
                    else:
                        del(namelist[tmp])
                        del(numlist[tmp])
                        print('删除成功')
                        break # 退出删除操作
    elif(choice==3):
        if(not namelist):
            print('通讯录中暂时还没有数据哦！')
        else:
            while(1):
                name=input('请输入您要修改的姓名：(输入exit退出)  ')
                number=input('请输入您要修改的姓名对应的号码: (输入exit退出)  ')
                if(name=='exit' and number=='exit'):
                    print('退出成功！')
                    break
                else:
                    flag=0
                    for i in range(len(namelist)):
                        if(namelist[i]==name and numlist[i]==number):
                            cname=input('请输入您修改后的新名字： ')
                            cnumber=input('请输入您修改后的新号码： ')
                            namelist[i]=cname
                            numlist[i]=cnumber
                            flag=1
                    if(flag):
                        print('修改成功')
                        break # 退出修改操作
                    else:
                        print('您输入的用户不存在，请重新输入！')
    elif(choice==4):
        if(not namelist):
            print('通讯录中还没有数据哦！')
        else:
            print('通讯录用户数据如下：')
            for i in range(len(namelist)):
                print("- {}: {} - ".format(namelist[i],numlist[i]))
    elif(choice==5):
        if(namelist):
            while(1):
                choc=int(input('根据姓名查询号码请输入1，根据号码查询名字请输入2:  '))
                # 根据姓名查询
                if(choc==1):
                    while(1):
                        name=input('请输入名字：输入exit退出查询')
                        if(name=='exit'):
                            print('退出查询！')
                            break
                        elif(namelist.count(name)==0):
                            print('您输入的姓名不存在！请重新输入！')
                        else:
                            print('所有{}的电话号码如下：一共{}条搜索结果'.format(name,namelist.count(name)))
                            cnt=0
                            for i in range(len(namelist)):
                                if(namelist[i]==name):
                                    cnt+=1
                                    print('{}. {}'.format(cnt,numlist[i]))
                            break
                    break
                # 根据号码查询
                elif(choc==2):
                    while(1):
                        number=input('请输入号码：（输入exit退出查询）')
                        if(number=='exit'):
                            print('退出成功！')
                            break
                        elif(numlist.count(number)==0):
                            print('您输入的号码不存在，请重新输入')
                        else:
                            print('您要查找的号码主人如下：')
                            id=numlist.index(number)
                            print(namelist[id])
                            break
                    break
                else:
                    print('您的输入有误!请重新输入！')
        else:
            print('通讯录中暂时还没有数据哦')
    elif(choice==7):
        print('退出通讯录系统成功！！！')
        break
    elif(choice==6):
        namelist.clear()
        numlist.clear()
        print('清空成功')
    else:
        print('您输入的服务不存在！请重新输入！')