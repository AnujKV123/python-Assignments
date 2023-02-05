
# 8. Access the nested key ‘salary’ from the following JSON
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
   { 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
   { 
      "employee":{ 
         "name":"emma",
         "payble":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""

# emp-id     emp-name -- salary

import json



data = '''{ 
   "company":[
      { 
         "employee":{ 
            "name":"emma",
            "payble":{ 
               "salary":7000,
               "bonus":800
            }
         }
      },
      { 
         "employee":{ 
            "name":"emma",
            "payble":{ 
               "salary":7000,
               "bonus":800
            }
         }
      },
      { 
         "employee":{ 
            "name":"emma",
            "payble":{ 
               "salary":7000,
               "bonus":800
            }
         }
      }
   ]
}'''

parsedData = json.loads(data)
id = 1
for item in parsedData["company"]:
   print(f'{id}   {item["employee"]["name"]}  --  {item["employee"]["payble"]["salary"]}')
   id += 1

