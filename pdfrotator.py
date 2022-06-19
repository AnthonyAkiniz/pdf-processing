#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                          PDF Rotator                                          # * #
# * #                          project by: Anthony Akiniz                           # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Info:                                                                                 #
# Python script to rotate PDF files.                                                    #
#                                                                                       #
# Requirements:                                                                         #
# pip3 install PyPDF2                                                                   #
# documentation: https://pypi.org/project/PyPDF2                                        #
#                                                                                       #
# Guide:                                                                                #
# 'rb' = read binary since PDFs are in binary                                           #
# 1. Place original PDF you want to rotate in the folder: Rotate                        #
# 2. Adjust Original PDF name and Output PDF name in the code below.                    #
# 3. Enter your preferred rotation up to 360 in: rotateClockwise(#)                     #
# 4. Launch by clicking run button in top right in VSCode or: py -3 pdfrotator.py       #
# A sample file called brochure-letter.pdf is included to run an initial test.          #
#########################################################################################

import PyPDF2

# Original PDF to Rotate -- location/name:
with open('./Rotate/brochure-letter.pdf', 'rb') as file:
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)

    # rotate right = 90, rotate left = -90
    # flip upside down = 180
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    # Output PDF -- location/name:
    with open('./Rotate/brochure-landscape.pdf', 'wb') as new_file:
        writer.write(new_file)
