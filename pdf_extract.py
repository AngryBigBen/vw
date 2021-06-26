import pandas as pd
import re
import pdfplumber
import 


#extract pdf content
with pdfplumber.open('name_list.pdf') as test_pdf:
    master = []
    for i in range(len(test_pdf.pages)):
        page = test_pdf.pages[i]
        text = [i.rstrip() for i in page.extract_text().splitlines()]
        text = [i for i in text if i] #remove empty strings
        master.append(text)

def get_company_name(pdf):

    return company_name


def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)


#Output pdf
for i in range(input_pdf.numPages):
    output = PdfFileWriter()
    output.addPage(input_pdf.getPage(i))
    with open("LC Healthcare Fund I LP Capital Account 2021%s_%s.pdf" % (quarter, company_name), "wb") as outputStream:
        output.write(outputStream)

