from PyPDF2 import PdfWriter # i dont know this module is not available 
merger = PdfWriter()
pdfs=[]
n=int(input("how many pdf you wanna add: "))
for i in range(0,n):
    name=input(f"enter the name of the pdfs {i+1}:")
    pdfs.append()

for pdf in pdfs:
    merger.append()


merger.write("merged-pdf.pdf")
merger.close()
#here you can merge the pdf how much you wanna to .