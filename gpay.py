import PyPDF2
import time

sum_sent=0
sum_paid=0
sum_received=0

def split_word(line):
    new=''
    split_after = line.split()[2:3]
    
    return split_after

def total(val):
    new=''
    if ',' in val:
        val=val.replace(',','')
    for x in val:
        if x.isalpha():
            new += x.replace(x, '')
        else:
            new+=x
    sum=0
    sum+=float(new)
    return sum

with open('D:\\VisualStudio\\Python\\Projects\\Gpay-History\\gpay.pdf', 'rb') as file:

    pdf = PyPDF2.PdfFileReader(file)

    for page in range(pdf.getNumPages()):
        text = pdf.getPage(page).extractText()

        lines = text.split('\n')

        for line in lines:
            if 'Sent' in line:
                sent = split_word(line)
                for val in sent:
                    sum_s = total(val)
                    sum_sent+=sum_s
            
            if 'Paid' in line:
                paid = split_word(line)
                for val in paid:
                    sum_p = total(val)
                    sum_paid+=sum_p
            elif 'Received' in line:
                received = split_word(line)
                for val in received:
                    sum_r = total(val)
                    sum_received+=sum_r
      
print("Total money sent = " + "₹" + str(format(sum_sent,".2f")))
time.sleep(2)
print("Total money paid = " + "₹" + str(format(sum_paid,".2f")))
time.sleep(2)
print("Total money received = " + "₹" + str(format(sum_received,".2f")))
print()
time.sleep(4)
print("Total Transaction = " + "₹" + str(format(sum_sent+sum_paid+sum_received,".2f")))
