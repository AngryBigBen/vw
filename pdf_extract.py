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

#Output pdf
for i in range(input_pdf.numPages):
    output = PdfFileWriter()
    output.addPage(input_pdf.getPage(i))
    with open("LC Healthcare Fund I LP Capital Account 2021%s_%s.pdf" % (quarter, company_name), "wb") as outputStream:
        output.write(outputStream)

