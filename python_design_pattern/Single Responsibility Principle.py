#SRP
# single responsible principle
#this principle state that a class should  have a one reason to change, that means every class should have single 
# reason , responsiblity or single purpose
# EX  like the task is divided into different different teams for developing software , testing software and , FE design
# and BE design. like this
# a class should not be modified for other requirements , otherwise class will lengthy.
class Journal:
    def __init__(self):
        self.entries = [];
        self.count = 0
        
    def add_count(self,text):
        self.entries.append(text)
        self.count += 1
    
    def del_count(self,index):
        del self.entries[index]
        
    def __str__(self):
        return '\n'.join(self.entries)

######### now from here on it will break SRP #####
    def saveIntoFile(self):
        pass
    def load(self):
        pass
    def load_aws(self):
        pass
##### Above all these three methos will break SRP since they are not related to any how 
##### to this class. thease can be done in different class.

class WriteToFile:
    def save_to_file(jornal,file):
        with.open(fiename,'w')
        pass
    
    
j = Journal()
j.add_count('my name is rahul')
j.add_count('fuck you')
j.del_count(1)
## 
p = WriteToFile(j,'rhaul.txt')
print(j)
