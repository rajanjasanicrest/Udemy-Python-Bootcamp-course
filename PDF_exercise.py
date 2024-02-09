import PyPDF2
import re
pdf_file = PyPDF2.PdfReader("/content/Find_the_Phone_Number.pdf")
text = ''
n = len(pdf_file.pages)
for i in range(n):
  page = pdf_file.pages[i]
  text += page.extract_text()


if re.search(r'\d{3}.\d{3}.\d{4}',text):
  print('hai')
print("Phone Number:", re.search(r'\d{3}.\d{3}.\d{4}',text).group())