from flask import Flask, request, send_from_directory, send_file
import json, uuid, subprocess
app = Flask(__name__, static_url_path = '')

FILES_DIR = 'files'
INPUT_HTML_DIR = 'input_html'

@app.route('/')
def home():
    return json.dumps({
		"response": "online"
	})

@app.route('/pdf', methods=['POST'])
def pdf():
	data = request.get_json()

	temp_name = uuid.uuid4()
	file_path = '/app/{}/{}.pdf'.format(FILES_DIR, temp_name)
	# _format = data.get('format') or ['url'] # just URL by default
	file = None
	html = data.get('html')
	if (html):
		# Create a file
		filename = "{}/{}.html".format(INPUT_HTML_DIR, temp_name)
		_f = open(filename, 'w+')
		_f.write(html)
		_f.close()
		# set source as a filename
		source = filename
	source = data.get('url') or file
	pdf_generated = subprocess.call(['wkhtmltopdf', source, temp_path])
	
	if(pdf_generated == 0):
		resp = {
			"file":"/{}/{}.pdf".format(FILES_DIR, temp_name)
		}
		return (json.dumps(resp), 200, {"Content-Type":"application/json"})
	else :
		return (json.dumps({"error": "pdf generation failed"}), 500, {"Content-Type":"application/json"})

@app.route('/files/<uuid:path>', methods=['GET'])
def send_pdf(path):
	print (path)
	return send_from_directory(FILES_DIR, path)
