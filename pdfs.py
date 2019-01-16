from xhtml2pdf import pisa
from io import StringIO

def create_pdf(sourceHtml, outputFilename):
    resultFile = open(outputFilename, "w+b")
    pisaStatus = pisa.CreatePDF(sourceHtml,dest=resultFile)
    resultFile.close()
    #return pisaStatus.err
    return resultFile