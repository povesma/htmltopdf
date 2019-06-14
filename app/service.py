from flask import Flask, request, send_from_directory, send_file
import json, uuid, subprocess
import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__, static_url_path = '')

FILES_DIR = 'files'
INPUT_HTML_DIR = 'input_html'

pdfs_path = '{}/{}'.format(ROOT_PATH, FILES_DIR)
htmls_path = '{}/{}'.format(ROOT_PATH, INPUT_HTML_DIR)

@app.route('/')
def home():
    return json.dumps({
		"response": "online"
	})

@app.route('/pdf', methods=['POST'])
def pdf():
	data = request.get_json()

	temp_name = uuid.uuid4()
	file_path = '{}/{}.pdf'.format(pdfs_path, temp_name)
	# _format = data.get('format') or ['url'] # just URL by default
	source = data.get('url')
	html = data.get('html')
	if (html):
		# Create a file
		filename = "{}/{}.html".format(htmls_path, temp_name)
		_f = open(filename, 'w+')
		_f.write(html)
		_f.close()
		# set source as a filename
		source = filename
	pdf_generated = subprocess.call(['wkhtmltopdf', source, file_path])
	
	if(pdf_generated == 0):
		resp = {
			"file":"/{}/{}.pdf".format(FILES_DIR, temp_name),
			"prefix":"/{}/{}/".format(FILES_DIR, temp_name),
		}
		return (json.dumps(resp), 200, {"Content-Type":"application/json"})
	else :
		return (json.dumps({"error": "pdf generation failed"}), 500, {"Content-Type":"application/json"})

@app.route('/files/<string:path>', methods=['GET'])
def send_pdf(path):
	#fn = "{}.{}".format(path, '.pdf')
	print (path)
	return send_from_directory(pdfs_path, path)

@app.route('/files/<uuid:path>/<string:filename>', methods=['GET'])
def send_named_pdf(path, filename):
	#fn = "{}.{}".format(path, '.pdf')
	print ("Changind filename:", path, filename)
	return send_from_directory(pdfs_path, "{}.pdf".format(path))
