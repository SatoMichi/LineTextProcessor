import re
import sys
import datetime
import matplotlib.pyplot as plt

path = sys.argv[1]
with open(path,encoding="utf-8") as f:
    txt = f.read()

txt = re.sub(r".*が退会しました。","",txt)
txt = re.sub(r".*が.*を退会させました。","",txt)
txt = re.sub(r".*が.*を招待しました。","",txt)
txt = re.sub(r".*が参加しました。","",txt)
txt = re.sub(r".*が退出しました。","",txt)
txt = re.sub(r".*が.*の招待をキャンセルしました。","",txt)
txt = re.sub(r".*がグループの画像を変更しました。","",txt)
txt = re.sub(r".*がグループのプロフィール写真を変更しました。","",txt)
txt = re.sub(r".*アルバムを作成しました","",txt)
txt = re.sub(r".*に写真を追加しました","",txt)
txt = re.sub(r".*の写真を削除しました。","",txt)
txt = re.sub(r".*アルバムを削除しました。","",txt)
txt = re.sub(r".*が.*アルバムの名前を.*に変更しました","",txt)
txt = re.sub(r".*chat.message.groupcall.started.long","",txt)
txt = re.sub(r".*グループ通話が終了しました","",txt)
txt = re.sub(r".*メッセージの送信を取り消しました","",txt)

days = re.findall("\d{4}/\d{2}/\d{2}\(.\)",txt)
txt = re.split("\d{4}/\d{2}/\d{2}\(.\)",txt)[1:]

data = []

for day,text in zip(days,txt):
    times = re.findall("\d{2}:\d{2}\t",text)
    names = re.findall("\t.*\t",text)
    cont = [re.sub("\t.*\t","",s) for s in re.split("\d{2}:\d{2}",text)][1:]
    for i in range(len(times)):
        if not times == []:
            dic = {"Time":day+"_"+times[i][:-1],"Name":names[i][1:-1],"Text":cont[i]}
            data.append(dic)

def showNameGraph(data):
    names = [d["Name"] for d in data]
    nums = {}
    for n in names:
        if n not in nums:
            nums[n] = 1
        else:
            nums[n] += 1
    nameplt = nums.keys()
    numplt = nums.values()
    plt.bar(nameplt, numplt)
    plt.show()
    return nums

def showDayGraph(data):
    times = [d["Time"] for d in data]
    nums = {}
    for n in times:
        if n[:10] not in nums:
            nums[n[:10]] = 1
        else:
            nums[n[:10]] += 1
    dayplt = nums.keys()
    numplt = nums.values()
    plt.plot(numplt)
    plt.show()
    return nums

def showAllDaysGraph(data):
    y = int(data[0]["Time"][:4])
    m = int(data[0]["Time"][5:7])
    d = int(data[0]["Time"][8:10])
    start = datetime.date(y,m,d)
    y = int(data[-1]["Time"][:4])
    m = int(data[-1]["Time"][5:7])
    d = int(data[-1]["Time"][8:10])
    end = datetime.date(y,m,d)
    daysList = [start]
    while not start == end:
        delta = datetime.timedelta(1)
        start += delta
        daysList.append(start)
    daysList.append(end)
    days = [re.sub("-","/",str(day)) for day in daysList]
    graph = {}
    for day in days:
        graph[day] = 0
    times = [d["Time"] for d in data]
    for n in times:
        graph[n[:10]] += 1
    dayplt = graph.keys()
    numplt = graph.values()
    plt.plot(numplt)
    plt.show()
    return graph