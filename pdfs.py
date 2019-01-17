from flask import make_response
from xhtml2pdf import pisa
from io import StringIO

def create_pdf(sourceHtml, outputFilename):
    resultFile = open(outputFilename, "w+b")
    pisaStatus = pisa.CreatePDF(sourceHtml,dest=resultFile)
    resultFile.close()
    return pisaStatus.err
    #pdf = StringIO(sourceHtml)
    #resp = pdf.getvalue()
    
    #response = make_response(outputFilename)
    #return response