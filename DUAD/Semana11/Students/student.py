class Student():
    def __init__(self, name, section, spanish_grade, english_grade, social_grade, science_grade, student_average):
        self.name = name
        self.section = section
        self.spanish_grade = spanish_grade
        self.english_grade = english_grade
        self.social_grade = social_grade
        self.science_grade = science_grade
        self.student_average = student_average

    
    def print_info(self):
        print(f"Name: {self.name}\n"
                    f" Section: {self.section}\n"
                    f" Spanish Grade: {self.spanish_grade}\n"
                    f" English: {self.english_grade}\n"
                    f" Social: {self.social_grade}\n"
                    f" Science: {self.science_grade}\n"
                    f" Average: {self.student_average}\n"
        )

    
    def convert_object_list_in_dictionary_list(self):
        dictionary = {}
        dictionary["Name"] = self.name
        dictionary["Section"] = self.section
        dictionary["Spanish Grade"] = self.spanish_grade
        dictionary["English Grade"] = self.english_grade
        dictionary["Social Grade"] = self.social_grade
        dictionary["Science Grade"] = self.science_grade
        dictionary["Average"] = self.student_average
        return dictionary


    def print_top_three(self):
        print(f"Name: {self.name}\n"
                    f" Section: {self.section}\n"
                    f" Average: {self.student_average}\n"
        )


    def search_student(self,student_name,student_section):
        if self.name.upper() == student_name.upper() and self.section.upper() == student_section.upper():
            print(f"Student {self.name}, Exist in {self.section}")
            return 0