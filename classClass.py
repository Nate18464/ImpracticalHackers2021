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
    def __init__(self, name, units, prereqs):
        self.name = name # example ECS 36A
        self.units = units
        self.prereqs = prereqs # list of course names
        self.taken = False

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

MAT21A = Course("MAT 21A", 4, [])
MAT21B = Course("MAT 21B", 4, [["MAT 21A"]])
MAT21C = Course("MAT 21C", 4, [["MAT 21B"]])
MAT22A = Course("MAT 22A", 4, [["MAT 21C"]])
CHE2A = Course("CHE 2A",5,[])
CHE2B = Course("CHE 2B",5,[["CHE 2A"]])
CHE2C = Course("CHE 2C",5,[["CHE 2B"]])
PHY9A = Course("PHY 9A",5,[])
PHY9B = Course("PHY 9B",5,[["PHY 9A"]])
PHY9C = Course("PHY 9C",5,[["PHY 9B"]])
BIS2A = Course("BIS 2A",5,[])
BIS2B = Course("BIS 2B",5,[["BIS 2A"]])
BIS2C = Course("BIS 2C",5,[["BIS 2B"]])
STA131A = Course("STA 131A",4,[["MAT 21C"], ["MAT 22A"]])
STA131B = Course("STA 131B",4,[["STA 131A"]])
MAT108 = Course("MAT 108",4,[["MAT 21B"]])
MAT135A = Course("MAT 135A",4,[["MAT 108"]])
ECS20 = Course("ECS 20", 4, [["MAT 21A"]])
ECS36A = Course("ECS 36A", 4, [])
ECS36B = Course("ECS 36B", 4, [["ECS 36A"]])
ECS36C = Course("ECS 36C", 4, [["ECS 36B"]])
ECS50 = Course("ECS 50", 4, [["ECS 36B"]])
ECS120 = Course("ECS 120", 4, [["ECS 20"], ["ECS 36C"]])
ECS122A = Course("ECS 122A", 4, [["ECS 20"], ["ECS 36C"]])
ECS122B = Course("ECS 122B", 4, [["ECS 122A"]])
ECS124 = Course("ECS 124", 4, [["ECS 36A"], ["MAT 135A", "STA 131A"], ["BIS 2A"]])
ECS127 = Course("ECS 127", 4, [["ECS 20"], ["ECS 36A"]])
#Fill out prereqs for the classes below, note, it is a list of lists where if there is multiple strings in a list, it means or.
ECS129 = Course("ECS 129", 4, [])
ECS130 = Course("ECS 130", 4, [])
ECS132 = Course("ECS 132", 4, [])
ECS140A = Course("ECS 140A", 4, [])
ECS140B = Course("ECS 140B", 4, [])
ECS142 = Course("ECS 142", 4, [])
ECS145 = Course("ECS 145", 4, [])
ECS150 = Course("ECS 150", 4, [])
ECS152A = Course("ECS 152A", 4, [])
ECS152B = Course("ECS 152B", 4, [])
ECS152C = Course("ECS 152C", 4, [])
ECS153 = Course("ECS 153", 4, [])
ECS154A = Course("ECS 154A", 4, [])
ECS154B = Course("ECS 154B", 4, [])
ECS158 = Course("ECS 158", 4, [])
ECS160 = Course("ECS 160", 4, [])
ECS161 = Course("ECS 161", 4, [])
ECS162 = Course("ECS 162", 4, [])
ECS163 = Course("ECS 163", 4, [])
ECS164 = Course("ECS 164", 4, [])
ECS165A = Course("ECS 165A", 4, [])
ECS165B = Course("ECS 165B", 4, [])
ECS170 = Course("ECS 170", 4, [])
ECS171 = Course("ECS 171", 4, [])
ECS173 = Course("ECS 173", 4, [])
ECS174 = Course("ECS 174", 4, [])
ECS175 = Course("ECS 175", 4, [])
ECS177 = Course("ECS 177", 4, [])
ECS178 = Course("ECS 178", 4, [])
ECS188 = Course("ECS 188", 4, [])