import json
from jsondiff import diff
import xlsxwriter


with open('./ul_packet_loss.json') as f:
    a= json.load(f)

with open('ul_packet_loss2.json') as s:
    b= json.load(s)

c= diff(a,b)
#print(c)
c.items()
c1=list(c.items())
print(c.keys(), c.values())

# workbook = xlsxwriter.Workbook('myfile.xlsx')
# worksheet = workbook.add_worksheet()
# row = 0
# col = 0

# order=sorted(c.keys())
# for key in order:
#     row += 1
#     print(key)
#     worksheet.write(row,    col,     key)
#     for item in c[key]:
#         print(item,row, col+1)
#         worksheet.write(row, col + 1, item)
#         col += 1
#     col = 0

# workbook.close()
