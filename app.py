import time

#import redis
from flask import Flask, render_template, redirect, url_for, make_response
from pdfs import create_pdf
from flask_restful import Resource, Api


app = Flask(__name__)
#cache = redis.Redis(host='redis', port=6379)
api = Api(app)

@app.route('/pdf')
def your_view():
    vale={"monto":100,"numerodigital":"0900411210000080","code":690,"date_expired":"13 de Febrero del 2019"}
    sourceHtml = render_template('pdf.html',vale=vale)
    namefile=str(time.time())
    outputFilename = "vale-"+namefile+".pdf"
    pdf = create_pdf(sourceHtml, outputFilename)
    return 'Generado '+outputFilename
vales=[
    {"monto":100,"numerodigital":"0900411210000080","code":690,"date_expired":"13 de Febrero del 2019"},
    {"monto":100,"numerodigital":"0900411210000080","code":690,"date_expired":"13 de Febrero del 2019"},
    {"monto":200,"numerodigital":"0900411210000080","code":691,"date_expired":"14 de Febrero del 2019"},
    {"monto":300,"numerodigital":"0900411210000080","code":692,"date_expired":"15 de Febrero del 2019"},
    {"monto":400,"numerodigital":"0900411210000080","code":693,"date_expired":"16 de Febrero del 2019"}
]
class vale(Resource):
    def get(self, vale_id):
        vale=vales[vale_id]
        sourceHtml = render_template('pdf.html',vale=vale)
        namefile=str(time.time())
        outputFilename = "vale-"+namefile+".pdf"
        pdf = create_pdf(sourceHtml, outputFilename)


        #pdf_out = pdf
        #response = make_response(pdf_out)
        #response.headers['Content-Type'] = 'application/pdf'
        #response.headers['Content-Disposition'] = \
        #    'inline; filename=%s.pdf' % 'xx'
        #return response
        return {'generado': outputFilename}
api.add_resource(vale, '/api/vale/<int:vale_id>')

@app.route('/')
def hello():
    return 'Hello'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)