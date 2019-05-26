from flask import Flask, request, send_from_directory,send_file
import json,uuid,subprocess
app = Flask(__name__,static_url_path='')

@app.route('/')
def home():
    return json.dumps({
		"response":"online"
	})

@app.route('/pdf',methods=['POST'])
def pdf():
	data = request.get_json()

	temp_name = uuid.uuid4()
	temp_path = '/app/temp/{}.pdf'.format(temp_name)
	pdf_generated = subprocess.call(['wkhtmltopdf',data['url'],temp_path])
	
	if(pdf_generated == 0):
		resp = {
			"file":"/temp/{}.pdf".format(temp_name)
		}
		return (json.dumps(resp),200,{"Content-Type":"application/json"})
	else :
		return json.dumps({ "error": "pdf generation failed"})

@app.route('/temp/<path:path>')
def send_js(path):
	print (path)
	return send_from_directory('temp', path)
