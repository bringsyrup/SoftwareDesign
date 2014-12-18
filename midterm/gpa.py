#! /bin/env python

class GPA(object):

    def __init__(self, grades_file="raw_grades.txt"):
        self.grades_file = grades_file

    def calc_gpa(self, grades):
        grade_dict = {
                "A": 4.0,
                "B": 3.0,
                "C": 2.0,
                "D": 1.0,
                "F": 0.0
                }
        return sum(grade_dict[grade.strip(",")] for grade in grades)/len(grades)

    def useful_array(self):
        with open(self.grades_file, "r") as grades:
            return [[word.strip(",") for word in line.split()] for line in grades]

    def print_gpa(self, return_only=True):
        if return_only == False:
            gpa_file = open("class-grades.txt", "w")
            for person in self.useful_array():
                gpa_file.write(str(person[0]) + ": " + str(self.calc_gpa(person[1:])) + "\n")
            gpa_file.close()
        else:
            return [[person[0], self.calc_gpa(person[1:])] for person in self.useful_array()]

    def twf_tupe(self):
        as_tuples = [(person[0], person[1]) for person in self.print_gpa()]
        graduates = list()
        superseniors = list()
        for tupe in as_tuples:
            if tupe[1] < 2.5:
                superseniors.append(tupe)
            else:
                graduates.append(tupe)
        return graduates, superseniors

    def twf_dict(self):
        as_dict = {str(person[0]): person[1] for person in self.print_gpa()}
        graduates = dict()
        superseniors = dict()
        for dude in as_dict:
            if as_dict[dude] < 2.5:
                superseniors[dude] = as_dict[dude]
            else:
                graduates[dude] = as_dict[dude]
        return graduates, superseniors

def main():
    grades = GPA()
    grades.print_gpa(return_only=False)
    grads_tupes, supers_tupes = grades.twf_tupe()
    grads_dict, supers_dict = grades.twf_dict()
    print "grads as tuples: " + str(grads_tupes)
    print "supers as tuples: " + str(supers_tupes)
    print "grads as dicts: " + str(grads_dict)
    print "supers as dicts: " + str(supers_dict)

if __name__=="__main__":
   main() 
