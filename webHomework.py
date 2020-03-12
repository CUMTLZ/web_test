import pytest
import operator
#判断属于哪一个牌型
def istonghuashun(list1, list2):
    list1 = sorted(list1)
    if list1[0]+1 == list1[1] and list1[1]+1 == list1[2] and list1[2]+1 == list1[3] and list1[3]+1 ==list1[4] and  list2[0]==list2[1] and list2[1] == list2[2] and list2[2] ==list2[3] and list2[3]==list2[4]:
        return  True
    return False

def istiezhi(list1, list2):
    list1 = sorted(list1)
    if (list1[0]==list1[1] and list1[1]==list1[2] and list1[2]==list1[3]) or (list1[1]==list1[2] and list1[2]==list1[3] and list1[3] == list1[4]):
        return True
    return False

def istonghua(list1, list2):
    if list2[0]==list2[1] and list2[1] == list2[2] and list2[2] ==list2[3] and list2[3]==list2[4]:
        return True
    return False

def ishulu(list1, list2):
    list1 = sorted(list1)
    if (list1[0]==list1[1] and list1[1]==list1[2] and list1[3]==list1[4]) or (list1[0]==list1[1] and list1[2]==list1[3] and list1[3]==list1[4]):
        return True
    return False

def isshunzi(list1, list2):
    list1 = sorted(list1)
    if list1[0]+1 == list1[1] and list1[1]+1 == list1[2] and list1[2]+1 == list1[3] and list1[3]+1 ==list1[4]:
        return True
    return False

def issantiao(list1, list2):
    list1 = sorted(list1)
    if (list1[0]==list1[1] and list1[1]==list1[2]) or (list1[1]==list1[2] and list1[2]==list1[3]) or (list1[2]==list1[3] and list1[3]==list1[4]):
        return True
    return False

def isliangdui(list1, list2):
    list1 = sorted(list1)
    if (list1[0]==list1[1] and list1[3]==list1[2]) or (list1[1]==list1[2] and list1[3]==list1[4]) or (list1[0]==list1[1] and list1[3]==list1[4]):
        return True
    return False

def isduizi(list1, list2):
    list1 = sorted(list1)
    if list1[0]==list1[1] or list1[1]==list1[2] or list1[2]==list1[3] or list1[3]==list1[4]:
        return True
    return False
#同一种牌型之间的大小比较
def bijiaotiezhi(list1, list2):
    if list1[0]==list1[1]:
        a =list1[4]
    else:
        a = list1[0]
    if list2[0]==list2[1]:
        b =list2[4]
    else:
        b = list2[0]
    if list1[2]>list2[2]:
        return "black win"
    elif list1[2]<list2[2]:
        return "white win"
    elif list1[2]==list2[2] and a>b:
        return "black win"
    elif list1[2]==list2[2] and a<b:
        return "white win"
    else:
        return "Tie"

def bijiaohulu(list1,list2):
    list1 = sorted(list1)
    list2 = sorted(list2)
    if list1[1]==list1[2]:
        a1 = list1[1]
        a2 = list1[4]
    else:
        a1 = list1[4]
        a2 = list1[1]
    if list2[1]==list2[2]:
        b1 = list2[1]
        b2 = list2[4]
    else:
        b1 = list2[4]
        b2 = list2[1]
    if a1>b1:
        return "black win"
    elif a1<b1:
        return "white win"
    elif a1==b1 and a2>b2:
        return "black win"
    elif a1==b1 and a2<b2:
        return "white win"
    else:
        return "Tie"

def bijiaotonghua(list1,list2):
    list1 = sorted(list1)
    list2 = sorted(list2)
    list1.reverse()
    list2.reverse()
    if operator.gt(list1,list2):
        return "black win"
    elif operator.lt(list1,list2):
        return "white win"
    else:
        return "Tie"

def bijiaoshunzi(list1,list2):
    list1 = sorted(list2)
    list2 = sorted(list1)
    if list1[4]>list2[4]:
        return "black win"
    elif list1[4]<list2[4]:
        return "white win"
    else:
        return "Tie"

def bijiaosantiao(list1,list2):
    list1 = sorted(list1)
    list2 = sorted(list2)
    if list1[0]==list1[1] and list1[1]==list1[2]:
        a1 = list1[0]
        b1 = list1[4]
        c1 = list1[3]
    elif list1[2]==list1[1] and list1[3]==list1[2]:
        a1 = list1[1]
        b1 = list1[4]
        c1 = list1[0]
    else:
        a1 = list1[2]
        b1 = list1[1]
        c1 = list1[0]
    if list2[0]==list2[1] and list2[1]==list2[2]:
        a2 = list2[0]
        b2 = list2[4]
        c2 = list2[3]
    elif list2[2]==list2[1] and list2[3]==list2[2]:
        a2 = list2[1]
        b2 = list2[4]
        c2 = list2[0]
    else:
        a2 = list2[2]
        b2 = list2[1]
        c2 = list2[0]
    if a1>a2:
        return "blcak win"
    elif a1<a2:
        return "white win"
    elif a1==a2 and b1>b2:
        return  "black win"
    elif a1==a2 and b1<b2:
        return "white win"
    elif a1==a2 and b1==b2 and c1>c2:
        return "black win"
    elif a1==a2 and b1==b2 and c1<c2:
        return "white win"
    else:
        return "Tie"

def bijiaoliangdui(list1,list2):
    list2 = sorted(list2)
    list1 = sorted(list1)
    print(list1)
    print(list2)
    if list1[2]==list1[1] and list1[3]==list1[4]:
        a1 = list1[4]
        b1 = list1[1]
        c1 = list1[0]
    elif list1[0]==list1[1] and list1[3]==list1[4]:
        a1 = list1[4]
        b1 = list1[0]
        c1 = list1[2]
    elif list1[0]==list1[1] and list1[2]==list1[3]:
        a1 = list1[3]
        b1 = list1[0]
        c1 = list1[4]
    if list2[2]==list2[1] and list2[3]==list2[4]:
        a2 = list2[4]
        b2 = list2[1]
        c2 = list2[0]
    elif list2[0]==list2[1] and list2[3]==list2[4]:
        a2 = list2[4]
        b2 = list2[0]
        c2 = list2[2]
    elif list2[0]==list2[1] and list2[2]==list2[3]:
        a2 = list2[3]
        b2 = list2[0]
        c2 = list2[4]
    if a1>a2:
        return "blcak win"
    elif a1<a2:
        return "white win"
    elif a1==a2 and b1>b2:
        return  "black win"
    elif a1==a2 and b1<b2:
        return "white win"
    elif a1==a2 and b1==b2 and c1>c2:
        return "black win"
    elif a1==a2 and b1==b2 and c1<c2:
        return "white win"
    else:
        return "Tie"

def bijiaoduizi(list1,list2):
    list1 = sorted(list1)
    list2 = sorted(list2)
    set(list1)
    set(list2)
    list1.reverse()
    list2.reverse()
    if operator.gt(list1,list2):
        return "black win"
    elif operator.lt(list1,list2):
        return "white win"
    else:
        return "Tie"

def bijiaosanpai(list1,list2):
    list1 = sorted(list1)
    list2 = sorted(list2)
    list1.reverse()
    list2.reverse()
    if operator.gt(list1,list2):
        return "black win"
    elif operator.lt(list1,list2):
        return "white win"
    else:
        return "Tie"
#将TQJKA转换为对应的数字，-->10,11,12,13,14
def zhuanhuan(s):
    int1 = s.split(" ", -1)[0][0]
    char1 = s.split(" ", -1)[0][1]
    int2 = s.split(" ", -1)[1][0]
    char2 = s.split(" ", -1)[1][1]
    int3 = s.split(" ", -1)[2][0]
    char3 = s.split(" ", -1)[2][1]
    int4 = s.split(" ", -1)[3][0]
    char4 = s.split(" ", -1)[3][1]
    int5 = s.split(" ", -1)[4][0]
    char5 = s.split(" ", -1)[4][1]
    list = [int1, int2, int3, int4, int5]
    list2 = [char1, char2, char3, char4, char5]
    for k in range(5):
        if list[k] =='T':
            list[k] = 10
        if list[k] == 'J':
            list[k] = 11
        if list[k] == 'Q':
            list[k] = 12
        if list[k] == 'K':
            list[k] = 13
        if list[k] == 'A':
            list[k] = 14
    list = [int(list[0]),int(list[1]),int(list[2]),int(list[3]),int(list[4])]
    return list, list2
#比较两个牌型的大小
def bijiao(result1, result2,list_black,list_white):
    dict = {"sanpai":1, "duizi":2, "liangdui":3, "santiao":4, "shunzi":5, "tonghua":6,"hulu":7,"tiezhi":8,"tonghuashun":9}
    if result1!=result2:
        if dict[result1]>dict[result2]:
            return "black win"
        else:
            return "white win"
    elif result1==result2=="tonghuashun":
        list_black = sorted(list_black)
        list_white = sorted(list_white)
        if list_black>list_white:
            return "black win"
        elif list_black<list_white:
            return "white win"
        else:
            return "Tie"
    elif result1==result2=="tiezhi":
        return bijiaotiezhi(list_black,list_white)
    elif result1==result2=="hulu":
        return  bijiaohulu(list_black,list_white)
    elif result2 ==result1=="tonghua":
        return  bijiaotonghua(list_black,list_white)
    elif result1==result2=="shunzi":
        return bijiaoshunzi(list_black,list_white)
    elif result1==result2=="santiao":
        return  bijiaosantiao(list_black,list_white)
    elif result2==result1=="liangdui":
        return bijiaoliangdui(list_black,list_white)
    elif result1==result2=="duizi":
        return bijiaoduizi(list_black,list_white)
    elif result1==result2=="sanpai":
        return bijiaosanpai(list_black,list_white)
#测试方法，供测试调用
def test(black,white):
    list1, list2 = zhuanhuan(black)
    list3, list4 = zhuanhuan(white)
    if istonghuashun(list1, list2):
        result1 = 'tonghuashun'
    elif istiezhi(list1, list2):
        result1 = 'tiezhi'
    elif ishulu(list1, list2):
        result1 = 'hulu'
    elif istonghua(list1, list2):
        result1 = 'tonghua'
    elif isshunzi(list1, list2):
        result1 = 'shunzi'
    elif issantiao(list1, list2):
        result1 = 'santiao'
    elif isliangdui(list1, list2):
        result1 = 'liangdui'
    elif isduizi(list1, list2):
        result1 = 'duizi'
    else:
        result1 = 'sanpai'
    if istonghuashun(list3, list4):
        result2 = 'tonghuashun'
    elif istiezhi(list3, list4):
        result2 = 'tiezhi'
    elif ishulu(list3, list4):
        result2 = 'hulu'
    elif istonghua(list3, list4):
        result2 = 'tonghua'
    elif isshunzi(list3, list4):
        result2 = 'shunzi'
    elif issantiao(list3, list4):
        result2 = 'santiao'
    elif isliangdui(list3, list4):
        result2 = 'liangdui'
    elif isduizi(list3, list4):
        result2 = 'duizi'
    else:
        result2 = 'sanpai'
    return bijiao(result1,result2,list1,list3)




