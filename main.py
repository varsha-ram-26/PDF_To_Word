from pydoc import Doc
import PyPDF2
import os
from PDF_To_Page.Single_Page import Single_Page
from PDF_To_Pages.Multiple_Pages import Multiple_Pages

cd = os.chdir('./Documents/Personal/GitHub/PDF_to_Word/PDF_To_Word/')
print(os.getcwd())

pdf_file = open(input("Enter the File Name: "),"rb")


pdfReader = PyPDF2.PdfFileReader(pdf_file)
print("1. PDF to Single Word Doc")
print("2. PDF to Multiple Word Doc")
options = int(input("Enter the Choice of yours :  "))

if(options == 1):
    Single_Page(pdfReader=pdfReader)
elif(options == 2):
    Multiple_Pages(pdfReader=pdfReader)
else:
    print("You've Entered the Wrong Option!")

pdf_file.close()