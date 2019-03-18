########################
#  python 3.6          #
#  库：PyPDF2           #
#  2019.3.18 by:Ljy    #
########################
# encoding:utf-8
from PyPDF2 import PdfFileReader, PdfFileWriter


readFile = 'C:/Users/Ljy/Desktop/test.pdf'
outFile = 'C:/Users/Ljy/Desktop/ok.pdf'
pdfFileWriter = PdfFileWriter()

 # 获取 PdfFileReader 对象
pdfFileReader = PdfFileReader(readFile)  # 或者这个方式：pdfFileReader = PdfFileReader(open(readFile, 'rb'))
 #文档总页数
numPages = pdfFileReader.getNumPages()
print (numPages)
if numPages > 1:
# 从第n页之后的页面，输出到一个新的文件中，即分割文档
    n=1
    for index in range(n, numPages):
        pageObj = pdfFileReader.getPage(index)
        pdfFileWriter.addPage(pageObj)
    # 添加完每页，再一起保存至文件中
    pdfFileWriter.write(open(outFile, 'wb'))
