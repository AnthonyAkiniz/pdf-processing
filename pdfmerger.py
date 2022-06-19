#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                          PDF Merger                                           # * #
# * #                          project by: Anthony Akiniz                           # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Info:                                                                                 #
# Python script to merge multiple PDF files into 1 PDF file.                            #
#                                                                                       #
# Requirements:                                                                         #
# pip3 install PyPDF2                                                                   #
# documentation: https://pypi.org/project/PyPDF2                                        #
#                                                                                       #
# Guide:                                                                                #
# 1. Place all PDFs to merge in the root folder: pdf-processing                         #
# 2. In terminal run: py -3 pdfmerger.py 1.pdf 2.pdf 3.pdf                              #
# Sample files are included in the root folder to run an initial sample test.           #
#########################################################################################

import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)  # all pdfs in root folder
        merger.append(pdf)
    merger.write('merged-final.pdf')  # file output name


pdf_combiner(inputs)
