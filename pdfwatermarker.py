#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                          PDF Watermarker                                      # * #
# * #                          project by: Anthony Akiniz                           # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Info:                                                                                 #
# Python script to watermark your PDF files.                                            #
#                                                                                       #
# Requirements:                                                                         #
# pip3 install PyPDF2                                                                   #
# documentation: https://pypi.org/project/PyPDF2                                        #
#                                                                                       #
# Guide:                                                                                #
# 'rb' = read binary since PDFs are in binary                                           #
# 1. Place original PDF you want to watermark in the folder at: Watermark/1_Original    #
# 2. Place your watermark design in the folder at: Watermark/2_Watermark                #
# 3. Launch by clicking run button in top right in VSCode or: py -3 pdfwatermarker.py   #
# 4. View your outputed file in the folder at: Watermark/3_Output                       #
# Sample files are included in folders 1+2 to run an initial sample test.               #
#########################################################################################

import PyPDF2


# Original PDF -- location/name:
template = PyPDF2.PdfFileReader(
    open('./Watermark/1_Original/original.pdf', 'rb'))


# PDF Watermark image to apply -- location/name:
watermark = PyPDF2.PdfFileReader(
    open('./Watermark/2_Watermark/watermark.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()


for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    # Outputted PDF file -- location/name, can rename 'my-file' before or after:
    with open('./Watermark/3_Output/my-file.pdf', 'wb') as file:
        output.write(file)
