# PDF Processing
Python scripts to merge, watermark or rotate PDFs.

# Requirements
pip3 install PyPDF2
documentation: https://pypi.org/project/PyPDF2

# PDF Merger Guide
1. Place all PDFs to merge in the root folder: pdf-processing<br>
2. In terminal run: py -3 pdfmerger.py 1.pdf 2.pdf 3.pdf<br>
Sample files are included in the root folder to run an initial sample test.<br>

# PDF Watermarker Guide
'rb' = read binary since PDFs are in binary<br>
1. Place original PDF you want to watermark in the folder at: Watermark/1_Original<br>
2. Place your watermark design in the folder at: Watermark/2_Watermark<br>
3. Launch by clicking run button in top right in VSCode or: py -3 pdfwatermarker.py<br>
4. View your outputed file in the folder at: Watermark/3_Output<br>
Sample files are included in folders 1+2 to run an initial sample test.<br>

# PDF Rotator Guide
1. Place original PDF you want to rotate in the folder: Rotate<br>
2. Adjust Original PDF name and Output PDF name in the code below.<br>
3. Enter your preferred rotation up to 360 in: rotateClockwise(#)<br>
4. Launch by clicking run button in top right in VSCode or: py -3 pdfrotator.py<br>
A sample file called brochure-letter.pdf is included to run an initial test.<br>
