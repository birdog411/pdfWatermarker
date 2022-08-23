from PyPDF2 import PdfFileWriter, PdfFileReader
import os

dir = "C:/Temp/"

global name
filelist = []
watermarkfile = "WaterMarkTemplate.pdf"

for root, dirs, files in os.walk(dir):
    for name in files:
        if name.endswith((".pdf", ".PDF")):
            filelist.append(name)
            inputfile = dir + name
            outputfile = dir + name.replace(".pdf", "") + " DRAFT.pdf"

            pdf = PdfFileReader(inputfile, strict=False)
            writer = PdfFileWriter()

            water = PdfFileReader(watermarkfile)
            watermark = water.getPage(0)

            for i in range(pdf.getNumPages()):
                page = pdf.getPage(i)
                page.mergePage(watermark)
                writer.addPage(page)

            with open(outputfile, "wb") as out:
                writer.write(out)

for i in filelist:
    os.remove("C:/Temp/" + i)