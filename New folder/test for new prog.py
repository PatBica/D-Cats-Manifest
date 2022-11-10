from os import path
from glob import glob
import os , shutil, wx, pdfplumber, re
import xlsxwriter

def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))
kopejais = ""
for file_name in find_ext(".","pdf"): 
    with pdfplumber.open(file_name) as pdf:
        for page in pdf.pages:
            # declaration:
            size8 = page.filter(lambda obj: obj['object_type'] == 'char' and '8.0' in str(obj['size'])).extract_text()
            pos = size8.find('22LV')
            decl = size8[pos:pos+18]
            # DUBBLE DIS

            # AWB:
            text = re.split(r'[ \n]', page.extract_text())
            for code in text:
                if len(code) == 10:
                    try:
                        awb = int(code)
                        break
                    except ValueError:
                        continue
            # kg
            for number in text:
                if re.match(r'^[0-9]+\.[0-9]{3}$', number):
                    kg = number
                    break
        kopejais += (str(awb)+'\n'+str(decl)+"\t"+str(kg)+'\n')
    shutil.move("C:\\Users\\patri\\Desktop\\Decleration_pdf\\New folder\\"+file_name,"C:\\Users\\patri\\Desktop\\Decleration_pdf\\New folder\\Done\\" + file_name)
with open("readme" + '.txt', 'w') as f:
    f.write(kopejais)


shutil.copy("C:\\Users\\patri\\Desktop\\Decleration_pdf\\New folder\\x.xlsx","C:\\Users\\patri\\Desktop\\Decleration_pdf\\New folder\\POZ.xlsx")
# workbook = xlsxwriter.Workbook("C:\\Users\\patri\\Desktop\\Decleration_pdf\\New folder\\Declarations.xlsx")
# # worksheet = workbook.add_worksheet()
# # worksheet.write("A2","test")
# workbook.close()