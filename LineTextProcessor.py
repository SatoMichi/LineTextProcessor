import re
import sys
import matplotlib.pyplot as plt

path = sys.argv[1]
with open(path,encoding="utf-8") as f:
    txt = f.read()

txt = re.sub(r".*が退会しました。","",txt)
txt = re.sub(r".*が.*を退会させました。","",txt)
txt = re.sub(r".*が.*を招待しました。","",txt)
txt = re.sub(r".*が参加しました。","",txt)
txt = re.sub(r".*が.*の招待をキャンセルしました。","",txt)
txt = re.sub(r".*がグループの画像を変更しました。","",txt)
txt = re.sub(r".*がグループのプロフィール写真を変更しました。","",txt)
txt = re.sub(r".*アルバムを作成しました","",txt)
txt = re.sub(r".*に写真を追加しました","",txt)
txt = re.sub(r".*の写真を削除しました。","",txt)
#txt = re.sub(r".*")

days = re.findall("\d{4}/\d{2}/\d{2}\(.\)",txt)
txt = re.split("\d{4}/\d{2}/\d{2}\(.\)",txt)[1:]

data = []

for day,text in zip(days,txt):
    times = re.findall("\d{2}:\d{2}\t",text)
    names = re.findall("\t.*\t",text)
    cont = [re.sub("\t.*\t","",s) for s in re.split("\d{2}:\d{2}",text)][1:]
    for i in range(len(times)):
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