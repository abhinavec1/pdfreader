#   Run pip install pdfplumber

import pdfplumber
import re

pdf = pdfplumber.open("NANHE_LAL.pdf")
page = pdf.pages[0]
text = page.extract_text()
print(text)
pdf.close()

fields_re = re.compile(r'[\w.] : \w|[\w.] :\w')

fields = [  'UHID',
            'IPD NO.', 
            'UMR NO',
            'PATIENT NAME', 
            'MOBILE NO', 
            'WARD', 
            'AGE/SEX', 
            'AGE/GENDER',
            'CATEGORY', 
            'CONSULTANT NAME', 
            'DATE OF ADMISSION', 
            'TYPE OF DISCARGE', # Correct this
            'ADDRESS', 
            'DATE OF DISCHARGE', 
            'ADMISSION NO',
            'CONSULTANT 1',
            'CONSULTANT 2',
            'DEPARTMENT 1',
            'DEPARTMENT 2',
            'REFERRED BY',
            'SUMMARY DATE'
            ]


temp = re.split(' : | :', text)
rslt = []
end_of_info = False
for i in range(len(temp)):
    if end_of_info:
        break
    for field in fields:
        index = temp[i].upper().find(field)
        if index != -1:
            if index == 0:
                rslt.append('')
            else:
                rslt.append(temp[i][:index-1])
            rslt.append(field)
            break
    if index == -1:
        print(temp[i])
        rslt.append(temp[i])
        end_of_info = True

# Cleaning the last value
index = rslt[-1].find('\n')
rslt[-1] = rslt[-1][:index]

rslt.pop(0) # Deleting the undesired first entry
print(rslt)






