import pyttsx3, PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('', 'rb'))
speaker = pyttsx3.init()
for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractTest()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()
