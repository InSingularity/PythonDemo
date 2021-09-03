#实现分页功能
from PyPDF2 import  PdfFileReader, PdfFileWriter
file_reader = PdfFileReader("D:\\test\\test.pdf")
# getNumPages() 获取总页数
for page in range(file_reader.getNumPages()):
    # 实例化对象
    file_writer = PdfFileWriter()
    # 将遍历的每一页添加到实例化对象中
    file_writer.addPage(file_reader.getPage(page))
    with open("D:\\test\\{}.pdf".format(page),'wb') as out:
        file_writer.write(out)
