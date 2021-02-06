# class for major classes
class Course:
    #Initialize itself with a value and a photoimage
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
            if course.getname in self.prereqs:
                prereqs_taken += 1
        return prereqs_taken == len(self.prereqs)




