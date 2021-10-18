class_9 = {
    'teacher': 'PK Shukla sir',
    'student':{
        '001':{
            'name':'raju babu',
            'father':'babu ji',
            'grade' : 'c',
        },
        '002':{
            'name':'raja',
            'father':'mahraja',
            'grade' : 'b',
        },
        '007':{
            'name':'james bond',
            'father':'ghanshyam bond',
            'grade' : 'a'
        },
    }
}

from pprint import pprint
print(class_9,)



#how to access

print(class_9['student']['002']['father'])

#loop

for k ,val in class_9.items():
    print(k, end='->')
    if isinstance (val,str):
      print(val)

    if isinstance(val,dict):
        for k,data in val.items():
            print(k, end='->')

            if isinstance(data,str):
              print(data)
            if isinstance(data,dict):
                for k,v in data.items():
                    print(k,end='->')
                    if isinstance(v,str):
                        print(v)