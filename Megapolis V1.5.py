# MEGAPOLIS 特大都市 V1.0 Made by Jason
import random
import time as ctime
import os

# DATA
ROAD =           {"name":"road",           "level":1,  "cost":200,     "exp":1,  "people":False, "environment":0}
SMALLHOUSE =     {"name":"smallhouse",     "level":1,  "cost":12500,   "exp":5,  "people":(5,10,15), "environment":-5}
WOODENHOUSE =    {"name":"woodenhouse",    "level":2,  "cost":15000,   "exp":10, "people":(10,20,25), "environment":-10}
DOUBLECABIN =    {"name":"doublecabin",    "level":2,  "cost":35000,   "exp":15, "people":(30,50,80), "environment":-15}
BASICFARM   =    {"name":"basicfarm",      "level":1,  "cost":5000,    "exp":8,  "people":False, "earns":2000, "environment":-40}
EXTRAFARM   =    {"name":"extrafarm",      "level":2,  "cost":10000,   "exp":10, "people":False, "earns":4000, "environment":-80}
TREE1  =         {"name":"tree1",          "level":1,  "cost":1000,    "exp":3, "people":False, "environment":15}
SMALLLAKE  =     {"name":"smalllake",       "level":2,  "cost":500,    "exp":2, "people":False, "environment":10}
BAMBOO  =        {"name":"bamboo",          "level":3,  "cost":5000,    "exp":15, "people":False, "environment":40}
MARKET =         {"name":"market",          "level":3,  "cost":25000,    "exp":20, "people":False, "earns":7500, "environment":-20} 
DATA = [ROAD, SMALLHOUSE, WOODENHOUSE, DOUBLECABIN, BASICFARM, EXTRAFARM, TREE1, SMALLLAKE, BAMBOO, MARKET]

lv = [10, 15, 25, 50, 100, 200, 500, 1000]
CHA = {"road": 1, "smallhouse": 5, "woodenhouse": 10, "doublecabin": 15,
       "smallpark": 15, "basicfarm": 8, "extrafarm": 15, "tree1": 3}
earns = {"basicfarm":5000, "extrafarm":10000}
PEOPLE_BUILDINGS = ["smallhouse", "woodenhouse", "doublecabin"]
EARNING_BUILDINGS = ["basicfarm", "extrafarm", "market"]
ROADS = ["road1", "road2", "road3", "road4", "road5", "road6", "road7", "road8", "road9", "road10", "road11"]

#PICS2 [0]-empty [1]-smallhouse [2]-basicfarm [3]-woodenhouse [4]-doublecabin [5]-smallpark
#PICS2 [6]-road1 [7]-road2 [8]-road3 [9]-road4 [10]-road5 [11]-road6 [12]-road7
#PICS2 [13]-road8 [14]-road9 [15]-road10 [16]-road11
#PICS2 [17]-extrafarm [18]-tree1 [19]-bamboo [20]-water [21]-market
#4，5，6，7分别是上转左，上转右，下转左，下转右
# 4,5,6,7 left+up right+up left+down right+down
# 8,9,10,11 left+up+down right+up+down up+left+right down+left+right
PICS2 = [["┏━━━━━━━━━━━━━━┓", "┃              ┃","┃              ┃","┃              ┃",
         "┃              ┃","┃              ┃","┃              ┃","┗━━━━━━━━━━━━━━┛"],
         ["                ","   /^^^^^^^^\   ","/^^^^^^^^^^^^^^\\","┣┅┳┅┳━━━━┳┅┅┳┅┅┫",
         "┣┳┻┅┫    ┣━┳┻┳┅┫", "┣┻┅┳┫  ○ ┣┅┻┳┻┅┫","┣┅┳┻┫    ┣┅┳┻┳┅┫","┗┅┻┅┻┅┅┅┅┻┅┻┅┻┅┛"],
         ["┏━━━━━━━┳━━━━━━┓","┃□□□ □□□┃Basic ┃","┃□□□ □□□┃Farm  ┃","┃□□□ □□□┃      ┃",
         "┃□□□ □□□┃      ┃","┣━━━ ━━━┛      ┃","┃        2k/min┃","┗━━━━━━━━━━━━━━┛"],
         ["     ╔┉┉┉┉╗     ","  ╔╦┉╩┉┉┉┉╩┉╦╗  ","╔╦╬╬╦╦╦╦╦╦╦╦╬╬╦╗"," ╬╬ ╩ ╩  ╩ ╩ ╬╬ ",
         " ┋┋ ╔┉┉╗ ╔┉┉┉╣┋ "," ┋┋ ╠┉┉╣ ┋  ╔╣┋ "," ┋┋ ╚┉┉╝ ┋  ╚╣┋ ","╔╩╩┉┉┉┉┉┉╩┉┉┉╩╩╗"],
         ["----------------","|              |","|    Double    |","|    Cabin     |",
          "|              |","|              |","|              |","----------------"],
         ["----------------", "|              |", "|              |", "|  Small Park  |",
          "|              |", "|              |", "|              |", "----------------"],
         ["┃ ┃    ■■    ┃ ┃","┃ ┃    ■■    ┃ ┃","┃ ┃    ■■    ┃ ┃","┃ ┃    ■■    ┃ ┃",  # road 1
          "┃ ┃    ■■    ┃ ┃","┃ ┃    ■■    ┃ ┃","┃ ┃    ■■    ┃ ┃","┃ ┃    ■■    ┃ ┃"], 
         ["━━━━━━━━━━━━━━━━","━━━━━━━━━━━━━━━━","                "," ■■ ■■ ■■ ■■ ■■ ",  # road 2
          " ■■ ■■ ■■ ■■ ■■ ","                ","━━━━━━━━━━━━━━━━","━━━━━━━━━━━━━━━━"],
         ["  ┃    ■■    ┃  ","━━┛    ■■    ┗━━","       ■■       "," ■■ ■■ ■■ ■■ ■■ ",  # road 3
          " ■■ ■■ ■■ ■■ ■■ ","       ■■       ","━━┓    ■■    ┏━━","  ┃    ■■    ┃  "],
         ["━━━━━━━━━━━━━━━┓","━━━━━━━━━━━━━┓ ┃","             ┃ ┃"," ■■ ■■ ■■    ┃ ┃",  # 4
          " ■■ ■■ ■■    ┃ ┃","       ■■    ┃ ┃","━━┓    ■■    ┃ ┃","  ┃    ■■    ┃ ┃"], 
         ["┏━━━━━━━━━━━━━━━","┃ ┏━━━━━━━━━━━━━","┃ ┃             ","┃ ┃    ■■ ■■ ■■ ",  # 5
          "┃ ┃    ■■ ■■ ■■ ","┃ ┃    ■■       ","┃ ┃    ■■    ┏━━","┃ ┃    ■■    ┃  "],
         ["  ┃    ■■    ┃ ┃","━━┛    ■■    ┃ ┃","       ■■    ┃ ┃"," ■■ ■■ ■■    ┃ ┃",  #6
          " ■■ ■■ ■■    ┃ ┃","             ┃ ┃","━━━━━━━━━━━━━┛ ┃","━━━━━━━━━━━━━━━┛"],
         ["┃ ┃    ■■    ┃  ","┃ ┃    ■■    ┗━━","┃ ┃    ■■       ","┃ ┃    ■■ ■■ ■■ ",  # 7
          "┃ ┃    ■■ ■■ ■■ ","┃ ┃             ","┃ ┗━━━━━━━━━━━━━","┗━━━━━━━━━━━━━━━"],
         ["  ┃    ■■    ┃ ┃","━━┛    ■■    ┃ ┃","       ■■    ┃ ┃"," ■■ ■■ ■■    ┃ ┃", # 8
          " ■■ ■■ ■■    ┃ ┃","       ■■    ┃ ┃","━━┓    ■■    ┃ ┃","  ┃    ■■    ┃ ┃"],
         ["┃ ┃    ■■    ┃  ","┃ ┃    ■■    ┗━━","┃ ┃    ■■       ","┃ ┃    ■■ ■■ ■■ ", # 9
          "┃ ┃    ■■ ■■ ■■ ","┃ ┃    ■■       ","┃ ┃    ■■    ┏━━","┃ ┃    ■■    ┃  "],
         ["  ┃    ■■    ┃  ","━━┛    ■■    ┗━━","       ■■       "," ■■ ■■ ■■ ■■ ■■ ", # 10
          " ■■ ■■ ■■ ■■ ■■ ","                ","━━━━━━━━━━━━━━━━","━━━━━━━━━━━━━━━━"],
         ["━━━━━━━━━━━━━━━━","━━━━━━━━━━━━━━━━","                "," ■■ ■■ ■■ ■■ ■■ ", # 11
          " ■■ ■■ ■■ ■■ ■■ ","       ■■       ","━━┓    ■■    ┏━━","  ┃    ■■    ┃  "],
         ["┏━━━━━━━━━━━┳━━┓","┃□□□ □□□ □□□┃  ┃","┃□□□ □□□ □□□┃  ┃","┃□□□ □□□ □□□┃  ┃", # ExtraFarm
          "┃□□□ □□□ □□□┃  ┃","┣━━┛ ┗━━    ┛  ┃","┃FarmEX  4k/min┃","┗━━━━━━━━━━━━━━┛",],
         [" ┏━━━━━━━━━━━━┓ "," ┃  ┏┳━━━━┳┓  ┃ " ," ┃┏━┛┗┳━━┳┛┗━┓┃ " ," ┗┛   ┗┳┳┛   ┗┛ ", # Tree1
          "       ╋╋       ","       ╋╋       ","       ╋╋       ","       ┻┻       ",],
         ["      ╲┏┓╱      ","      ╲╋╋╱      ","  ╲┏┓╱╲╋╋╱      ","  ╲╋╋╱╲╋╋╱      ", # bamboo
          "  ╲╋╋╱╲╋╋╱ ╲┏┓╱ ","  ╲╋╋╱ ╋╋  ╲╋╋╱ ","   ╋╋  ╋╋  ╲╋╋╱ ","   ╋╋  ╋╋   ╋╋  "],
         ["┏━━━━━━━━━━━━━━┓","┃ ~~~ ~~   ~~  ┃","┃~~~ ~   ~~  ~~┃","┃  ~~  ~~ ~~  ~┃", # water
          "┃~ ~~~~  ~~    ┃","┃~~~   ~~~  ~~~┃","┃~~ ~ ~~~~~~  ~┃","┗━━━━━━━━━━━━━━┛"],
         ["  ╱╳╳╳╳╳╳╳╳╳╳╲  "," ╱╳╳╳╳╳╳╳╳╳╳╳╳╲ ","╱┳┻━━━━━━━━━━┻┳╲","┣┫   Market   ┣┫", # market
          "╋╈┳┳┳┳┳┳┳┳━━━┳╈╋","╋╈╈╈╈╈╈╈╈╈  ┏╈╈╋","╋╈╈╈╈╈╈╈╈╈  ┗╈╈╋","┻┻┻┻┻┻┻┻┻┻━━━┻┻┻"]] 


# 通过建筑名称获取建筑相关数据
def getdata(buildname, datatype):
    for data in DATA:
        if data["name"] == buildname:
            return data[datatype]

# 检测是否已经有存档存在
def checkloads():
    for load in os.listdir():
        if load.split(".")[-1] == "city":
            return True
    return False

# 获得目录下所有存档
def getloads():
    loads = []
    for load in os.listdir():
        if load.split(".")[-1] == "city":
            loads.append(load)
    return loads

# 通过存档还原地图
def remap(s):
    resultmap = []
    new = []
    s1 = s.split("$")[:-1]
    for s2 in s1:
        s2 = s2[1:-1]
        tmp = s2.split(",")
        resultmap.append(tmp)
    for i in resultmap:
        jie = []
        for j in i:
            try:
                jie.append(int(j))
            except:
                jie.append(str(j[1:][1:-1]))
        new.append(jie)
    return new

# 通过存档还原工作点
def rework(s):
    resultworkers = []
    parts = s.split("@")
    for part in parts:
        if part == "":
            continue
        resultworkers.append(part.split("#"))
    for i in range(0, len(resultworkers)):
        for j in range(0, len(resultworkers[i])):
            try:
                resultworkers[i][j] = float(resultworkers[i][j])
            except:
                pass
    return resultworkers[:-1]



# 玩家类
class Player():
    def __init__(self, name, type = "new"):
        self.type = type
        self.data = city.userdata.readlines()
        if self.type == "load":
            self.name = self.data[0].split()[-1]
            self.balance = int(self.data[1].split()[-1])
            self.level = int(self.data[2].split()[-1])
            self.exp = int(self.data[3].split()[-1])
            self.totalexp = int(self.data[4].split()[-1])
            self.nextexp = int(self.data[5].split()[-1])
        else:
            self.name = name
            self.balance = 50000
            self.level = 1
            self.exp = 0
            self.totalexp = 0
            self.nextexp = 10
            city.userdata.write("username: " + self.name + "\n")
            city.userdata.write("balance: " + str(self.balance) + "\n")
            city.userdata.write("level: " + str(self.level) + "\n")
            city.userdata.write("exp: " + str(self.exp) + "\n")
            city.userdata.write("totalexp: " + str(self.totalexp) + "\n")
            city.userdata.write("nextexp: " + str(self.nextexp) + "\n")


    def earn(self, value):
        self.balance += value

    def cost(self, value):
        if value <= self.balance:
            self.balance -= value
        else:
            return False

    def addexp(self, num):
        self.totalexp += num
        self.exp += num
        if self.exp < lv[self.level - 1]:
            print("你获得了" + str(num) + "经验!")
            return
        while self.exp >= lv[self.level - 1]:
            self.exp = self.exp - lv[self.level - 1]
            self.level += 1
            self.nextexp = lv[self.level - 1] - self.exp
            print("恭喜! 您升入等级" + str(self.level) + "!")

    def show(self):
        print("市长:" + self.name)
        print("金钱:" + str(self.balance))
        print("等级:" + str(self.level), " 经验:" + str(self.exp))
        print()

# 城市工作经营类
class Worker():
    def __init__(self, name, type, money):
        T = ctime.time()
        self.name = name
        self.type = type
        self.oncemoney = money
        self.totaltime = 0 # 游戏总时长
        self.time = 0 # 距离上次获得利润时间
        self.starttime = T # 起始时间刻（每局常量）
        self.nowtime = T # 现在时间刻
        self.lastearntime = T # 上次盈利时间
        self.totalearn = 0 # 盈利总金额

    # 刷新现在的时间刻
    def update(self):
        self.nowtime = ctime.time()
        self.totaltime = int(self.nowtime - self.starttime)
        self.time = int(self.nowtime - self.lastearntime)

    # 盈利
    def earn(self):
        # 这里规定 单次收取的最大利润不可以大于10min所获得的利润
        self.update()
        if int(self.time) < 60:
            return False
        self.lastearntime = ctime.time()
        earns = (int(self.time) // 60) * self.oncemoney
        if earns > 10 * self.oncemoney:
            earns = 10 * self.oncemoney
        self.totalearn += earns
        return earns



# 城市类
class City():
    def __init__(self, name, size = "8x8", type = "new", username = "/"):
        self.name = name
        self.height = int(size.split("x")[1])
        self.width = int(size.split("x")[0])
        self.map = [[j, i, "empty"] for i in range(1, self.height+1) for j in range(1, self.width+1)]
        self.environment = 100
        self.env_type = "perfect"
        self.people = 0
        self.people_env_list = [0, 0, 0] # 应当反映的人口数量和环境状态的关系 bad-good-perfect 顺序
        
        self.earn = 0
        self.housecount = 0
        self.workcount = 0
        self.parkcount = 0
        self.buildcount = 0

        self.isfull = False
        self.lasttime = 0
        self.workers = []

        self.filedata = []
        self.f, self.f2 = 0, 0
        if type == "new":
            self.f = open("{}.city".format(name), "w+")
            self.userdata = open("{}.user".format(name), "w+")
            self.log = open("{}.log".format(name), "a+")
            '''
            userdata.write("username: "+ username +"\n")
            userdata.write("balance: 50000\n")
            userdata.write("level: 1\n")
            userdata.write("exp: 0\n")
            userdata.write("totalexp: 0\n")
            userdata.write("nextexp: 0\n")
            '''
            self.writedata("创建存档\n")
            self.f.write("cityname: " + self.name + "\n")
            self.f.write("height: " + str(self.height) + "\n")
            self.f.write("width: " + str(self.width) + "\n")
            self.f.write("environment: " + str(self.environment) + "\n")
            self.f.write("people: " + str(self.people) + "\n")
            self.f.write("people_env_list: " + str(self.people_env_list)[1:-1] + "\n")
            workers_data = self.workers_data_change()
            self.f.write("workers: " + str(workers_data) + "\n")  
            self.f.write("earn: " + str(self.earn) + "\n")
            self.f.write("housecount: " + str(self.housecount) + "\n")
            self.f.write("workcount: " + str(self.workcount) + "\n")
            self.f.write("parkcount: " + str(self.parkcount) + "\n")
            self.f.write("buildcount: " + str(self.buildcount) + "\n")
            self.f.write("citymap: " + str(self.map))

        elif type == "load":
            try:
                self.f = open("{}.city".format(name), "r+")
                self.userdata = open("{}.user".format(name), "r+")
                self.log = open("{}.log".format(name), "a+")

            except:
                print("错误！没有找到存档！")
        self.filedata = self.f.readlines()
        if type == "load":
            self.name = self.filedata[0].split()[-1]
            self.height = int(self.filedata[1].split()[-1])
            self.width = int(self.filedata[2].split()[-1])
            self.environment = int(self.filedata[3].split()[-1])
            self.people = int(self.filedata[4].split()[-1])
            self.people_env_list = self.filedata[5][17:-1].split(", ")
            for i in range(0, len(self.people_env_list)):
                self.people_env_list[i] = int(self.people_env_list[i])
            
            workerslist = rework(self.filedata[6].split(":")[-1])
            self.map = remap(self.filedata[12][9:])
            for worker in workerslist:
                tmpworker = Worker(worker[0], worker[1], worker[2])
                tmpworker.totaltime = worker[3]
                tmpworker.time = worker[4]
                tmpworker.starttime = worker[5]
                tmpworker.nowtime = worker[6]
                tmpworker.lastearntime = worker[7]
                tmpworker.totalearn = worker[8]
                self.workers.append(tmpworker)
            self.workcount = len(self.workers)

    # 建造建筑
    def build(self, what, where):
        w = self.changexy(where)
        for i in range(0, len(self.map)):
            if self.map[i][0] == int(w[0]) and self.map[i][1] == int(w[1]) and self.map[i][2] == "empty":
                self.map[i][2] = what
                break
        if what in PEOPLE_BUILDINGS:
            self.housecount += 1
            self.people_change(what, "increase")
        if what in EARNING_BUILDINGS:
            self.workcount += 1
            worker = Worker(str(len(self.workers) + 1), what, self.getplacedata(what, "earns"))
            self.workers.append(worker)

        self.changemap()
        self.writedata("在 {} 处建造 {} 建筑\n".format(where, what))
        self.show()

    # 道路建造
    def buildroad(self, where, isShow=True):
        w = self.changexy(where)
        x, y = w[0], w[1]
        if self.getplace(x, y) != "empty":
            return False

        self.map[self.getmapnum(x, y)][2] = "road3"
        self.roadmove(x, y, 1)

        # 判断1：如果目标道路上下左右都没有道路，建road3十字路口
        if self.getplace(x + 1, y) not in ROADS and self.getplace(x - 1, y) not in ROADS and self.getplace(x,
                                                                                                           y + 1) not in ROADS and self.getplace(
                x, y - 1) not in ROADS:
            self.map[self.getmapnum(x, y)][2] = "road3"
        else:
            self.roadcheck(x, y)

        self.writedata("在 {} 处建造道路\n".format(where))
        self.changemap()
        if isShow:
            self.show()

    # 更改.city的数据
    def changemap(self):
        self.f.close()
        os.remove("{}.city".format(self.name))
        ctime.sleep(0.1)
        self.f = 0
        self.f = open("{}.city".format(self.name), "w+")
        self.f.write("cityname: " + self.name + "\n")
        self.f.write("height: " + str(self.height) + "\n")
        self.f.write("width: " + str(self.width) + "\n")
        self.f.write("environment: " + str(self.environment) + "\n")
        self.f.write("people: " + str(self.people) + "\n")
        self.f.write("people_env_list: " + str(self.people_env_list)[1:-1] + "\n")
        workers_data = self.workers_data_change()
        self.f.write("workers: " + str(workers_data) + "\n")  
        self.f.write("earn: " + str(self.earn) + "\n")
        self.f.write("housecount: " + str(self.housecount) + "\n")
        self.f.write("workcount: " + str(self.workcount) + "\n")
        self.f.write("parkcount: " + str(self.parkcount) + "\n")
        self.f.write("buildcount: " + str(self.buildcount) + "\n")
        self.f.write("citymap: ")
        for i in self.map:
            self.f.write(str(i) + "$")

        self.f.seek(0, 0)
        self.filedata = self.f.readlines()


    # 变换坐标
    def changexy(self, string):
        s = string.split(",")
        return int(s[0]), int(s[1])

    # 更改.user的用户信息（钱数，等级等等）
    def changeuserdata(self, name, balance, level, exp, totalexp, nextexp):
        self.userdata.close()
        self.userdata = open("{}.user".format(self.name), "w+")
        self.userdata.write("username: " + name + "\n")
        self.userdata.write("balance: " + str(balance) + "\n")
        self.userdata.write("level: " + str(level) + "\n")
        self.userdata.write("exp: " + str(exp) + "\n")
        self.userdata.write("totalexp: " + str(totalexp) + "\n")
        self.userdata.write("nextexp: " + str(nextexp) + "\n")
    
    def check(self):
        return self.height, self.width, self.map

    # 检测坐标上是否是空位
    def checkempty(self, where):
        w = self.changexy(where)
        for i in range(0, len(self.map)):
            if self.map[i][0] == int(w[0]) and self.map[i][1] == int(w[1]) and self.map[i][2] == "empty":
                return True
            elif self.map[i][0] == int(w[0]) and self.map[i][1] == int(w[1]) and self.map[i][2] != "empty":
                return False

    # 环境状态监测
    def checkenv(self):
        if self.environment < 0:
            self.env_type = "bad"
        elif 0 < self.environment and self.environment < 100:
            self.env_type = "good"
        elif self.environment > 100:
            self.env_type = "perfect"

    # 检测坐标是否超出范围
    def checkout(self, where):
        w = self.changexy(where)
        if w[0] <= self.width and w[1] <= self.height and w[0] > 0 and w[1] > 0:
            return True
        else:
            return False

    # 检测城市是否满格
    def checkplace(self):
        isOk = True
        for i in range(0, len(self.map)):
            if self.map[i][2] == "empty":
                self.isfull = False
                return
        self.isfull = True

    # 检查工作点并返回工作点的信息列表
    def checkworkplace(self):
        res = []
        for i in self.workers:
            i.update()
            res.append(str(int(float(i.name))) + " " + i.type + " 工作时间：" + str(i.time) + "秒")
        return res

    # 商业性建筑的盈利
    def earnmoney(self, num):
        for i in self.workers:
            if int(i.name) == num:
                result = i.earn()
                if result == False:
                    return None
                else:
                    self.writedata("收取 {} 建筑的利润 ￥{} \n".format(i.type, result))
                    return result

    # 获取系统内部图的序号
    def getmapnum(self, xray, yray):
        for i in range(0, len(self.map)):
            if self.map[i][0] == xray and self.map[i][1] == yray:
                return i
        return False

    # 获取该位置上的建筑物
    def getplace(self, xray, yray):

        if xray == 0 or yray == 0 or xray > self.width or yray > self.height:
            return False
        
        for target in self.map:
            if target[0] == xray and target[1] == yray:
                return target[2]
        return False

    # 通过建筑名称获取建筑的所有信息 tag 表示信息种类
    def getplacedata(self, placename, tag):
        for data in DATA:
            if data["name"] == placename:
                return data[tag]
        return False
        
    # 动态更新人口
    def people_change(self, what = None, mode = "increase"):
        if what != None:
            peoples = self.getplacedata(what, "people")
            self.people_env_list[0] += (peoples[0] if mode == "increase" else -peoples[0])
            self.people_env_list[1] += (peoples[1] if mode == "increase" else -peoples[1])
            self.people_env_list[2] += (peoples[2] if mode == "increase" else -peoples[2])

        # 动态更新
        if self.env_type == "bad": self.people = self.people_env_list[0]
        elif self.env_type == "good": self.people = self.people_env_list[1]
        elif self.env_type == "perfect": self.people = self.people_env_list[2]

    # 拆除建筑
    def remove(self, where, isShow = True):
        w = self.changexy(where)
        removething = ""
        for i in range(0, len(self.map)):
            if self.map[i][0] == int(w[0]) and self.map[i][1] == int(w[1]):
                removething = self.map[i][2]
                self.map[i][2] = "empty"
                if removething in ROADS:
                     # 拆除的如果是道路，拆除后对其他道路的朝向重新检测 
                    self.roadmove(int(w[0]), int(w[1]), 2)
                break
        if removething in PEOPLE_BUILDINGS:
            self.housecount -= 1
            self.people_change(removething, "decrease")
        self.changemap()
        
        self.writedata("在 {} 处拆除 {}\n".format(where, removething))
        if isShow:
            self.show()

    # 判断一个道路四周的道路方向并加以调整
    def roadcheck(self, x, y):
        placesnear = [self.getplace(x-1, y-1), self.getplace(x, y-1), self.getplace(x+1, y-1),
                      self.getplace(x-1, y),   self.getplace(x, y),   self.getplace(x+1, y)  ,
                      self.getplace(x-1, y+1), self.getplace(x, y+1), self.getplace(x+1, y+1)]
        #print(x, y, self.getplace(x, y))
        # 前判断：如果原点不是道路，直接返回
        if placesnear[4] not in ROADS:
            return
        # 判断1：如果一方出现道路，那么将一方的道路改为单向道路
        if placesnear[1] in ROADS and placesnear[3] not in ROADS and placesnear[5] not in ROADS and placesnear[7] not in ROADS:
            self.map[self.getmapnum(x, y)][2] = "road1"
        elif placesnear[3] in ROADS and placesnear[1] not in ROADS and placesnear[5] not in ROADS and placesnear[7] not in ROADS:
            self.map[self.getmapnum(x, y)][2] = "road2"
        elif placesnear[5] in ROADS and placesnear[1] not in ROADS and placesnear[3] not in ROADS and placesnear[7] not in ROADS:
            self.map[self.getmapnum(x, y)][2] = "road2"
        elif placesnear[7] in ROADS and placesnear[1] not in ROADS and placesnear[3] not in ROADS and placesnear[5] not in ROADS:
            self.map[self.getmapnum(x, y)][2] = "road1"
        # 判断2：双连路口 
        elif placesnear[1] in ROADS and placesnear[3] in ROADS and placesnear[5] not in ROADS and placesnear[7] not in ROADS:
            self.map[self.getmapnum(x, y)][2] = "road6"
        elif placesnear[1] in ROADS and placesnear[5] in ROADS and placesnear[3] not in ROADS and placesnear[7] not in ROADS:
            self.map[self.getmapnum(x, y)][2] = "road7"
        elif placesnear[1] in ROADS and placesnear[7] in ROADS and placesnear[3] not in ROADS and placesnear[5] not in ROADS:
            self.map[self.getmapnum(x, y)][2] = "road1"
        elif placesnear[3] in ROADS and placesnear[5] in ROADS and placesnear[1] not in ROADS and placesnear[7] not in ROADS:
            self.map[self.getmapnum(x, y)][2] = "road2"
        elif placesnear[3] in ROADS and placesnear[7] in ROADS and placesnear[1] not in ROADS and placesnear[5] not in ROADS:
            self.map[self.getmapnum(x, y)][2] = "road4"
        elif placesnear[5] in ROADS and placesnear[7] in ROADS and placesnear[1] not in ROADS and placesnear[3] not in ROADS:
            self.map[self.getmapnum(x, y)][2] = "road5"
        # 判断3：丁字路口
        elif placesnear[1] in ROADS and placesnear[3] in ROADS and placesnear[5] in ROADS and placesnear[7] not in ROADS:
            self.map[self.getmapnum(x, y)][2] = "road10"
        elif placesnear[1] in ROADS and placesnear[3] in ROADS and placesnear[7] in ROADS and placesnear[5] not in ROADS:
            self.map[self.getmapnum(x, y)][2] = "road8"
        elif placesnear[1] in ROADS and placesnear[5] in ROADS and placesnear[7] in ROADS and placesnear[3] not in ROADS:
            self.map[self.getmapnum(x, y)][2] = "road9"
        elif placesnear[3] in ROADS and placesnear[5] in ROADS and placesnear[7] in ROADS and placesnear[1] not in ROADS:
            self.map[self.getmapnum(x, y)][2] = "road11" 
        # 判断4：十字路口
        elif placesnear[1] in ROADS and placesnear[3] in ROADS and placesnear[5] in ROADS and placesnear[7] in ROADS:
            self.map[self.getmapnum(x, y)][2] = "road3" 

    # 动态道路分析判断
    def roadmove(self, x, y, time):
        # time 递归次数（拓展范围） 
        #print(x, y, self.getplace(x, y), time)
        if time == -1:
            return
        #if self.getplace(x, y) not in ROADS :
            #return

        self.roadcheck(x, y)
        # 递归
        self.roadmove(x-1, y-1, time-1)
        self.roadmove(x, y-1, time-1)
        self.roadmove(x+1, y-1, time-1)
        self.roadmove(x-1, y, time-1)
        self.roadmove(x+1, y, time-1)
        self.roadmove(x-1, y+1, time-1)
        self.roadmove(x, y+1, time-1)
        self.roadmove(x+1, y+1, time-1)

    # 打印城市模型
    def show(self):
        def printlines(things):
            oneline = ""
            for line in range(0, 8):
                for i in things:
                    if i == "empty":
                        oneline += PICS2[0][line]
                    elif i == "smallhouse":
                        oneline += PICS2[1][line]
                    elif i == "basicfarm":
                        oneline += PICS2[2][line]
                    elif i == "woodenhouse":
                        oneline += PICS2[3][line]
                    elif i == "doublecabin":
                        oneline += PICS2[4][line]
                    elif i == "smallpark":
                        oneline += PICS2[5][line]
                    elif i == "road1":
                        oneline += PICS2[6][line]
                    elif i == "road2":
                        oneline += PICS2[7][line]
                    elif i == "road3":
                        oneline += PICS2[8][line]
                    elif i == "road4":
                        oneline += PICS2[9][line]
                    elif i == "road5":
                        oneline += PICS2[10][line]
                    elif i == "road6":
                        oneline += PICS2[11][line]
                    elif i == "road7":
                        oneline += PICS2[12][line]
                    elif i == "road8":
                        oneline += PICS2[13][line]
                    elif i == "road9":
                        oneline += PICS2[14][line]
                    elif i == "road10":
                        oneline += PICS2[15][line]
                    elif i == "road11":
                        oneline += PICS2[16][line]
                    elif i == "extrafarm":
                        oneline += PICS2[17][line]
                    elif i == "tree1":
                        oneline += PICS2[18][line]
                    elif i == "bamboo":
                        oneline += PICS2[19][line]
                    elif i == "smalllake":
                        oneline += PICS2[20][line]
                    elif i == "market":
                        oneline += PICS2[21][line]
                print(oneline)
                oneline = ""
        tmp, things = 0, []
        for i in range(0, len(self.map)):
            things.append(self.map[i][2])
            tmp += 1
            if tmp == self.width:
                printlines(things)
                tmp, things = 0, []
                
    # 打印城市信息
    def show_information(self):
        self.update()
        print("城市名称:" + self.name)
        print("金钱：{} 等级 {} 距下一级还需 {} 经验".format(player.balance, player.level, player.nextexp))
        print("人口:" + str(self.people))
        print("环境指数:" + str(self.environment), self.env_type.capitalize())
        print()

    # 有事没事更新一下游戏各种数据~
    def update(self):
        player.nextexp = lv[player.level - 1] - player.exp # 更新下一等级所需经验数
        self.checkenv() # 更新环境等级
        self.people_change()  # 依照环境更新人口
            
    # 改变Worker类的数据为可见的列表
    def workers_data_change(self):
        result = ""
        if self.workers == []:
            return []
        for each in self.workers:
            temp = str(each.name) + "#" + str(each.type) + "#" + str(each.oncemoney) + "#" +str(each.totaltime) + "#" +str(each.time) + "#" +str(each.starttime) + "#" +str(each.nowtime) + "#" +str(each.lastearntime) + "#" +str(each.totalearn)
            result += temp + "@"
        
        return result

    # 工作时间检查
    def worktimecheck(self):
        res = self.checkworkplace()

    # 记录玩家操作日志
    def writedata(self, thing):
        self.log.write(ctime.strftime("%Y-%m-%d %H:%M:%S") + " " + thing)

        
# 初始化城市
isRead = False
print("----------欢迎来到Megapolis!----------")
print("市长，我们该如何称呼您：")
name = input()
if checkloads():
    loads = []
    print("系统检测到您已经有存档，存档如下：")
    loads = getloads()
    print(loads)
    print("您想选择打开存档，还是新建一个城市？(打开：1/新建：2)")
    user = int(input())
    if user == 1:
        print("您想打开哪一个存档？输入序号：")
        num = int(input())
        load = loads[num - 1]
        print("正在加载中，请稍后......")
        isRead = True
    elif user == 2:
        print("您好, " + name + ", 现在，为您的城市创建一个新名称:")
        cityname = input()
        print("您的城市大小是多少？ (运用数字x数字的方式，例如 4x4, 8x8)")
        citysize = input()
        print("城市创建中，请稍后......")
else:
    print("您好, " + name + ", 现在，为您的城市创建一个新名称:")
    cityname = input()
    print("您的城市大小是多少？ (运用数字x数字的方式，例如 4x4, 8x8)")
    citysize = input()
    print("城市创建中，请稍后......")
# 创造并打印城市
if isRead:
    city = City(load.split(".")[0], "1x1", "load")
    # 创造玩家
    player = Player(name, type = "load")
else:
    city = City(cityname, citysize)
    player = Player(name)
city.show()
player.show()

def fast_road_building():
    print("您要把道路安放在哪些地方？（用2,3 2,4 2,5这样的连续坐标来安置道路，坐标之间要加空格哦）")
    while True:
        try:
            wheres = input()
            if wheres == "退出":
                print("好的，已经退出~")
                return
            else:
                wheres = wheres.split()
        except:
            print("输入有误，请重新尝试哦~")
        else:
            not_empty_places = []
            is_repeated = True if len(list(set(wheres))) != len(wheres) else False
            wheres = list(set(wheres))
            print(wheres)
            all_count = len(wheres)
            # 制作一个wheres的拷贝，方便完整遍历where
            wheres_copy = wheres.copy()
            for where in wheres_copy:
                if not city.checkempty(where) or not city.checkout(where):
                    not_empty_places.append(where)
                    wheres.remove(where)

            rest_empty_places = (all_count - len(not_empty_places))
            total_price = 200 * rest_empty_places
            total_exp = 2 * rest_empty_places
            if is_repeated:
                print("您输入了重复的坐标，已经自动帮您去除重复~")
            if len(wheres) == 0:
                print("您所描述的位置上均有建筑或位于城市区域之外，无法建造道路！")
                return
            elif len(not_empty_places) != 0:
                print("您所描述的位置中，{} 位置不能建造道路。剩余可建造的道路总价为￥{}".format(str(not_empty_places)[1:-1], total_price))
            else:
                print("建造这些道路需要￥{}".format(total_price))
            print("继续建造吗？（建造/不建造）")
            is_build = input()
            if is_build == "建造":
                player.cost(total_price)
                player.addexp(total_exp)
                city.changeuserdata(player.name, player.balance, player.level, player.exp, player.totalexp,
                                    player.nextexp)
                for where in wheres:
                    city.buildroad(where, isShow = False)
                city.show()
                player.show()
                return
            else:
                print("好的，已经取消建造！")
                return

def fast_removing():
    print("您要拆除哪些地方的建筑？（用2,3 2,4 2,5这样的连续坐标来拆除建筑，坐标之间要加空格哦）")
    while True:
        try:
            wheres = input()
            if wheres == "退出":
                print("好的，已经退出~")
                return
            else:
                wheres = wheres.split()
        except:
            print("输入有误，请重新尝试哦~")
        else:
            not_empty_places = []
            is_repeated = True if len(list(set(wheres))) != len(wheres) else False
            wheres = list(set(wheres))
            print(wheres)
            all_count = len(wheres)
            # 制作一个wheres的拷贝，方便完整遍历where
            wheres_copy = wheres.copy()
            for where in wheres_copy:
                if city.checkempty(where) or not city.checkout(where):
                    not_empty_places.append(where)
                    wheres.remove(where)

            rest_empty_places = (all_count - len(not_empty_places))
            total_price = 200 * rest_empty_places
            total_exp = 2 * rest_empty_places
            if is_repeated:
                print("您输入了重复的坐标，已经自动帮您去除重复~")
            if len(wheres) == 0:
                print("您所描述的位置上均没有可拆除的建筑或位于城市区域之外，无法拆除！")
                return
            elif len(not_empty_places) != 0:
                print("您所描述的位置中，{} 位置无法拆除。".format(str(not_empty_places)[1:-1]))
            print("继续拆除吗？（拆除/不拆除）")
            is_build = input()
            if is_build == "拆除":
                for where in wheres:
                    city.remove(where, isShow = False)
                city.show()
                player.show()
                return
            else:
                print("好的，已经取消拆除！")
                return


def choose_building(housetypes, prices):
    l = len(housetypes)
    if housetypes == "road":
        if player.balance < prices:
            print("市长，您没有足够的金钱建造道路!\n")
            return
        elif city.isfull:
            print("市长，您的城市空位不足！\n")
            return
        else:
            print("您想要把道路安放在何处:(运用 x,y 例如 3,3)")
            while True:
                where = input()
                if where == "退出":
                    print("好的，已退出建造！")
                    break
                if not city.checkout(where):
                    print("市长，您不能把道路放在城市土地之外！")
                elif not city.checkempty(where):
                    print("市长，这块地上已经有建筑了，请换一块地！")
                else:
                    break

            player.cost(prices)
            player.addexp(2)
            city.changeuserdata(player.name, player.balance, player.level, player.exp, player.totalexp, player.nextexp)
            city.buildroad(where)
            player.show()
            return
    while True:
        print("请告诉我建筑物的序号(用0来停止):")
        num = int(input())
        if num > l or num < 0:
            print("没有这个序号的建筑物，请重试！")
        elif num == 0:
            print("好的，已经退出选择！")
            break
        else:
            if player.level < getdata(housetypes[num - 1], "level"):
                print("市长，您的等级不够建造此建筑！\n")
                break
            if player.balance < prices[num - 1]:
                print("市长，您没有足够的金钱建造该建筑!\n")
                break
            elif city.isfull:
                print("市长，您的城市空位不足！\n")
                break
            else:
                print("您想要把该建筑安放在何处:(运用 x,y 例如 3,3)")
                while True:
                    where = input()
                    if not city.checkout(where):
                        print("市长，您不能把道路放在城市土地之外！")
                    elif not city.checkempty(where):
                        print("市长，这块地上已经有建筑了，请换一块地！")
                    else:
                        break

                player.cost(prices[num - 1])
                city.environment += int(getdata(housetypes[num - 1], "environment"))
                city.checkenv()
                city.build(housetypes[num - 1], where)
                player.addexp(city.getplacedata(housetypes[num - 1], "exp"))
                city.changeuserdata(player.name, player.balance, player.level, player.exp, player.totalexp, player.nextexp)
                player.show()
                break

# 主循环
while True:
    city.update()
    print("亲爱的市长，您想做些什么？（建造/铲除建筑/查看信息/盈利/退出）")
    users = input()
    if users == "建造":
        print("您想建造什么样的建筑?(房屋/工作点/道路/绿化)")
        kind = input()
        if kind == "房屋":
            print("以下是一些种类的房屋：")
            print("1.小房子      价格:12500  需求等级:1 容纳人数:5/10/15  环境指数:-5")
            print("2.精致木屋    价格:15000  需求等级:2 容纳人数:10/20/25 环境指数:-10")
            print("3.双层旅馆    价格:35000  需求等级:2 容纳人数:30/50/80 环境指数:-15")
            choose_building(["smallhouse", "woodenhouse", "doublecabin"],
                            [12500, 15000, 35000])

        elif kind == "工作点":
            print("以下是一些种类的工作点（利润单位为元/分钟）:")
            print("1.基础农场     价格:5000  需求等级:1 利润:￥2000/min  环境指数:-40")
            print("2.大型农场     价格:15000 需求等级:2 利润:￥4000/min  环境指数:-80")
            print("3.小商店       价格:25000 需求等级:3 利润:￥7500/min  环境指数:-20")
            choose_building(["basicfarm", "extrafarm", "market"],
                            [5000, 15000, 25000])
        elif kind == "道路":
            print("道路的价格为￥200/1格")
            print("选择快速建造道路模式吗？（是/否）")
            is_fast_road_building = input()
            if is_fast_road_building == "是":
                fast_road_building()
            else:
                choose_building("road", 200)
        elif kind == "绿化":
            print("以下是不同种类的绿化：")
            print("1.树木       价格:1000 需求等级:1 环境指数:+15")
            print("2.小型湖泊   价格:500 需求等级:2 环境指数:+10")
            print("3.竹林       价格:5000 需求等级:3 环境指数:+40")
            choose_building(["tree1", "smalllake", "bamboo"], [1000, 500, 5000])
        else:
            print("不好意思，您输入的建筑类型还不存在哦~")
    elif users == "铲除建筑":
        print("选择快速拆除建筑模式吗？（是/否）")
        is_fast_removing = input()
        if is_fast_removing == "是":
            fast_removing()
        else:
            print("输入你想铲除的建筑坐标:(运用 x,y 例如 3,3)")
            while True:
                where = input()
                if where == "退出":
                    print("好的，已经退出拆除界面！")
                    break
                if not city.checkout(where):
                    print("市长，您不能铲除城市土地之外的建筑，请重新尝试！")
                elif city.checkempty(where):
                    print("这块土地上没有建筑可以铲除，请重新尝试！")
                else:
                    city.remove(where)
                    player.show()
                    break

    elif users == "查看信息":
        city.show_information()
    elif users == "盈利":
        if city.workcount == 0:
            print("市长，您还没有任何的工作点!")
        else:
            result = city.checkworkplace()
            print("您有以下几个工作点:")
            print(result)
            print("您想要选择哪一个? 请告诉我序号:")
            index = int(input())
            tmpmoney = city.earnmoney(int(result[index - 1].split()[0]))
            money = None if tmpmoney == None else int(tmpmoney)
            if money == None:
                print("等一下，市长！工人们还没有生产完毕！")
            else:
                player.earn(money)
                city.changeuserdata(player.name, player.balance, player.level, player.exp, player.totalexp, player.nextexp)
                city.changemap()
                print("您获得了 ￥" + str(money) + "!")
    elif users == "退出":
        print("欢迎下次再来, " + name + "!")
        break
    
city.f.close()
city.log.close()
city.userdata.close()
            
