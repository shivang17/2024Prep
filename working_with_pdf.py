# The best and most stable module is PyPDF2

# The three main classes are PDFFileReader, PDFFileWriter, and PDFFileMerger

# Open the PDF file and then read it
# It's very important to open this file in the read binary mode. 
# PyPDF2 has been deprecated/replaced by PyPDF, but we will try to conceptually understand here what needs to be achieved:

"""
import PyPDF2

with open("Technical Assessment - Nicolas Giraldi.pdf", "rb) as file:
    reader = PyPDF2.PDFfileReader(file)
    page = reader.getPage(0)
    page.rotateClockWise(90)
// This doesn't change the original file. So, you will need to write this to a separate pdf file. 
    writer = PyPDF2.PDFfileWriter()
    writer.addPage(page)
    with open("rotated.pdf", "wb") as output
        writer.write(output)

"""

"""
    with open("read.pdf") as file:
    reader = PyPDF2.PDFFileReader(file)
    page =  reader.getPage(0)
    page.rotateClockWise(90)

    writer = PyPDF2.PDFFileWriter()
    writer.addPage(page)
    with open("writer.pdf", "wb") as output:
        writer.write(output)

"""

# You are doing everything in the memory above an would need to add it to the disc. 

# How to merge the files:

"""
import PyPDF2

merger = PyPDF2.PDFFileMerger()

file_names = ["first.pdf", "second.pdf", "third.pdf"]
for file_name in file_names:
    merger.append(file_name)

// To write it on disc

merger.write("combined.pdf")
"""

