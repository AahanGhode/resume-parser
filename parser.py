from pyresparser import ResumeParser
import os
import gspread
import pickle
from os.path import getsize as size

sa=gspread.service_account(filename="resume-summarizer/%APPDATA%/gspread/service_account.json")
sh = sa.open("Parsed Resumes")
wks=sh.worksheet("Data")
wks.format("A:K", {"wrapStrategy": "OVERFLOW_CELL"})
num=2
filename='resume-summarizer/num.pk'
if size(filename)>0:
    with open(filename, 'rb') as fi:
        num = pickle.load(fi)

for i in os.listdir('resume-summarizer/static/files/'):
    data = ResumeParser('resume-summarizer/static/files/'+i).get_extracted_data()
    keys = [str(eachvalue) for eachvalue in data.keys()]
    values = [str(eachvalue) for eachvalue in data.values()]
    Data =[{'range': 'A1:K1','values': [keys],}, {'range': 'A'+str(num)+':'+'K'+str(num),'values': [values],}]
    wks.batch_update(Data)
    num+=1

with open(filename, 'wb') as fi:
    pickle.dump(num, fi)

for root, dirs, files in os.walk('resume-summarizer/static/files/', topdown=False):
    for file in files:
        os.remove(os.path.join(root, file))