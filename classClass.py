def In(coursename, prereq):
    if len(prereq)==0:
        return True
    for p in prereq:
        if coursename in p:
            return True
    return False

# class for major classes
class Course:
    #Initialize itself with a value
    def __init__(self, name, units, prereqs, isprereq, ge):
        self.name = name # example ECS 36A
        self.units = units
        self.prereqs = prereqs # list of course names
        self.taken = False
        self.isprereq = isprereq
        self.ge = ge

    def getname(self):
        return self.name

    def getunits(self):
        return self.units

    def getprereqs(self):
        return self.prereqs

    def took(self):
        self.taken = True

    def hasTook(self):
        return self.taken

    def getisprereq(self):
        return self.isprereq

    def prereqstr(self):
        string = ""
        for i in range(len(self.prereqs)):
            for j in range(len(self.prereqs[i])):
                string += self.prereqs[i][j]
                if j != len(self.prereqs[i])-1:
                    string += " or "
            if i != len(self.prereqs)-1:
                string += ", "
            else:
                string += " "
        return string

    def retstr(self):
        return self.name + " Units: " + str(self.units) + " Prereqs: " + self.prereqstr()

    def canTake(self, courses_taken):
        if self.taken == True:
            return False
        prereqs_taken = 0
        for course in courses_taken:
            if prereqs_taken == len(self.prereqs):
                return True
            if In(course.getname, self.prereqs):
                prereqs_taken += 1
        return prereqs_taken == len(self.prereqs)

MAT21A = Course("MAT 21A", 4, [], True, [2,-1])
MAT21B = Course("MAT 21B", 4, [["MAT 21A"]], True, [2,-1])
MAT21C = Course("MAT 21C", 4, [["MAT 21B"]], True, [2,-1])
MAT22A = Course("MAT 22A", 4, [["MAT 21C"]], True, [2,-1])
CHE2A = Course("CHE 2A",5,[], True, [2,-1])
CHE2B = Course("CHE 2B",5,[["CHE 2A"]], True, [2,-1])
CHE2C = Course("CHE 2C",5,[["CHE 2B"]], False, [2,-1])
PHY9A = Course("PHY 9A",5,[], True, [2,-1])
PHY9B = Course("PHY 9B",5,[["PHY 9A"]], True, [2,-1])
PHY9C = Course("PHY 9C",5,[["PHY 9B"]], False, [2,-1])
BIS2A = Course("BIS 2A",5,[], True, [2,-1])
BIS2B = Course("BIS 2B",5,[["BIS 2A"]], True, [2,-1])
BIS2C = Course("BIS 2C",5,[["BIS 2B"]], False, [2,-1])
STA131A = Course("STA 131A",4,[["MAT 21C"], ["MAT 22A"]], True, [2,-1])
STA131B = Course("STA 131B",4,[["STA 131A"]], False, [2,-1])
MAT108 = Course("MAT 108",4,[["MAT 21B"]], True, [2,-1])
MATELEC = Course("MAT Elective", 4, [["MAT 108"]], False, [2,-1])
MAT135A = Course("MAT 135A",4,[["MAT 108"]], True, [2,-1])
ECS20 = Course("ECS 20", 4, [["MAT 21A"]], True, [2,-1])
ECS36A = Course("ECS 36A", 4, [], True, [2,-1])
ECS36B = Course("ECS 36B", 4, [["ECS 36A"]], True, [2,-1])
ECS36C = Course("ECS 36C", 4, [["ECS 36B"]], False, [2,-1])
ECS50 = Course("ECS 50", 4, [["ECS 36B"]], True, [2,-1])
ECS120 = Course("ECS 120", 4, [["ECS 20"], ["ECS 36C"]], True, [2,-1])
ECS122A = Course("ECS 122A", 4, [["ECS 20"], ["ECS 36C"]], True, [2,-1])
ECS122B = Course("ECS 122B", 4, [["ECS 122A"]], False, [2,-1])
ECS124 = Course("ECS 124", 4, [["ECS 36A"], ["MAT 135A", "STA 131A"], ["BIS 2A"]], False, [2,-1])
ECS127 = Course("ECS 127", 4, [["ECS 20"], ["ECS 36A"]], True, [2,-1])
ECS129 = Course("ECS 129", 4, [["BIS 2A"],["ECS 36A"]], False, [2,-1])
ECS130 = Course("ECS 130", 4, [["ECS 36A"], ["MAT 22A"]], False, [2,-1])
ECS132 = Course("ECS 132", 4, [["ECS 36B"], ["ECS 20"], ["MAT 21C"],["MAT 22A"]], False, [2,-1])
ECS140A = Course("ECS 140A", 4, [["ECS 50"], ["ECS 36C"], ["ECS 20"], ["ECS 150"]], True, [2,-1])
ECS140B = Course("ECS 140B", 4, [["ECS 140A"]], False, [2,-1])
ECS142 = Course("ECS 142", 4, [["ECS 140A"], ["ECS 120"]], False, [2,-1])
ECS145 = Course("ECS 145", 4, [["ECS 36C"]], False, [2,-1])
ECS150 = Course("ECS 150", 4, [["ECS 36C"], ["ECS 154A"]], True, [2,-1])
ECS152A = Course("ECS 152A", 4, [["ECS 36C"],["ECS 132", "MAT 135A", "STA 131A"]], True, [2,-1])
ECS152B = Course("ECS 152B", 4, [["ECS 150"], ["ECS 152A"]], True, [2,-1])
ECS152C = Course("ECS 152C", 4, [["ECS 152A"]], False, [2,-1])
ECS153 = Course("ECS 153", 4, [["ECS 150"], ["ECS 152A"]], False, [2,-1])
ECS154A = Course("ECS 154A", 4, [["ECS 50"]], True, [2,-1])
ECS154B = Course("ECS 154B", 4, [["ECS 154A"]], False, [2,-1])
ECS158 = Course("ECS 158", 4, [["ECS 150"]], False, [2,-1])
ECS160 = Course("ECS 160", 4, [["ECS 140A"]], False, [2,-1])
ECS161 = Course("ECS 161", 4, [["ECS 36B"]], False, [2,-1])
ECS162 = Course("ECS 162", 4, [["ECS 36B"]], False, [2,-1])
ECS163 = Course("ECS 163", 4, [["ECS 36C"]], False, [2,-1])
ECS164 = Course("ECS 164", 4, [], False, [2,-1])
ECS165A = Course("ECS 165A", 4, [["ECS 36C"]], True, [2,-1])
ECS165B = Course("ECS 165B", 4, [["ECS 165A"]], False, [2,-1])
ECS170 = Course("ECS 170", 4, [["ECS 36C"]], False, [2,-1])
ECS171 = Course("ECS 171", 4, [["ECS 36C"]], False, [2,-1])
ECS173 = Course("ECS 173", 4, [["MAT 22A"], ["ECS 36C"]], False, [2,-1])
ECS174 = Course("ECS 174", 4, [["ECS 36C"]], False, [2,-1])
ECS175 = Course("ECS 175", 4, [["MAT 22A"], ["ECS 36C"]], False, [2,-1])
ECS177 = Course("ECS 177", 4, [["ECS 175"]], False, [2,-1])
ECS178 = Course("ECS 178", 4, [["ECS 175"]], False, [2,-1])
ECS188 = Course("ECS 188", 4, [], False, [2,-1])
Allcourse = [MAT21A, MAT21B, MAT21C, MAT22A,
CHE2A, CHE2B, CHE2C, PHY9A, PHY9B, PHY9C, BIS2A, BIS2B, BIS2C,
STA131A, STA131B, MAT108, MAT135A,
ECS20, ECS36A, ECS36B, ECS36C, ECS50, 
ECS122A, ECS120, ECS122B, ECS124, ECS129,
ECS130, ECS132, ECS140A, ECS140B, ECS142, ECS145,
ECS150, ECS152A, ECS152B, ECS152C, ECS153, ECS154A, ECS154B, ECS158,
ECS160, ECS161, ECS162, ECS163, ECS164, ECS165A, ECS165B,
ECS170, ECS171, ECS173, ECS174, ECS175, ECS177, ECS178, ECS188]

#56 courses