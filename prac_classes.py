from dataclasses import dataclass



class Operations_on_string :
    def __init__(self, main_string, sub_string):
        self.main_string = main_string
        self.sub_string = sub_string
        self.dict_return = {}

    def is_sub_string_present(self):
        start = 0
        sub_start = 0

        while start < len(self.main_string):
            if self.main_string[start] == self.sub_string[sub_start]:
                sub_start +=1
                if sub_start == len(self.sub_string):
                    return "Present"       
            else:
                sub_start = 0
            start += 1
                
        return "Not Present" 

    def get_sub_string_indices(self):

        start = 0
        sub_start = 0
        indices = []

        while start < len(self.main_string):
            if self.main_string[start] == self.sub_string[sub_start]:
                sub_start +=1
                if sub_start == len(self.sub_string):
                    end = start
                    start_index = start - len(self.sub_string) + 1
                    indices.append((start_index, end))
                    sub_start = 0    
            else:
                sub_start = 0
            start += 1
                
        return indices if indices else "Not present"
    

                
                

string_1 = Operations_on_string("CouStrikenterStrike", "Strike")
print(string_1.is_sub_string_present())

print(string_1.get_sub_string_indices())
