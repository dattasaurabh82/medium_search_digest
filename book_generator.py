import pyqrcode
import csv
import sys
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter, A4
import time
import random


c = canvas.Canvas('successorElMedium.pdf', pagesize=letter)
width, height = letter #keep for later

csvfilename = str(sys.argv[1])

index = 0

with open(csvfilename) as myFile:
    reader = csv.DictReader(myFile)
    for row in reader:
        index+=1

        print(row['Links'])
        print(row['Headings'])

        qr = pyqrcode.create(str(row['Links']), error='L')
        qr.png(str(index)+'.png', scale=5, module_color=[17, 35, 80], background=[0xff, 0xff, 0xcc])
        print qr.terminal()

        print("\n")

        # time.sleep(1)

        c.translate(random.randint(1.5*inch, 3*inch),random.randint(inch, 2*inch))
        c.setFont("Times-Bold", 12)
        c.rotate(random.randint(0, 45))
        c.drawImage(str(index)+'.png', 2.5*inch, 2*inch)
        c.rotate(random.randint(10, 90))
        c.drawString(0, 0, str(row['Headings']))
        c.showPage()



c.save()

print("-----------------------------------------------------------------")
print("Finished Generating your guide to be the best designer out there.")
print("Go get it champ.")
print("-----------------------------------------------------------------")