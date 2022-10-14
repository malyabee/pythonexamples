"""
Input JSON
'{ "class":"EngCSE", 
   "01": {"name":"ramu", "marks":539}, 
   "02": {"name":"krishna", "marks":449},
   "03":{} 
   }
"""

"""
output 

01, ramu, EngCSE, 539
02, krishna, EngCSE, 449


"""


import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'
class_marks = '{ "class":"EngCSE", "01": { "name":"ramu", "marks":539}, "02": { "name":"krishna", "marks":449}, "03":{} }'



# parse x:
y = json.loads(class_marks)

class_name = y["class"]
y.pop("class")
#print(class_name)


for roll_no, s_info in y.items():
    if len(s_info) > 1:
       for ke in s_info:
           if ke == "name":
               name = s_info[ke]
           else:  
               marks = s_info[ke]
       print(roll_no, name, class_name, marks)       
     

