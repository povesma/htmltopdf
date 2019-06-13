
# htmltopdf / HTML-TO-PDF
Web service for HTML to PDF (htmltopdf) conversion based on _wkhtmltopdf_. This service converts HTML (local - as a text, or remote - as URL) to a PDF file, and make this file accessible on the web.

# Instalation and launch

`git clone https://github.com/povesma/htmltopdf.git && cd htmltopdf`

## Stand alone
`pip3 install -r app/requirements.txt`

`FLASK_APP=./app/service.py python3 -m flask run --host 0.0.0.0 --port 5000`

_Update your host and port!_

## In Docker container
### Local build
`docker build -t html-to-pdf .`

`docker run -d -v "$(pwd)"/app/input_html:/app -v "$(pwd)"/app/files:/app -p 127.0.0.1:5000:80 --rm --name html-to-pdf html-to-pdf`

### From Docker Hub
Alternatively, you can install and run _html-to-pdf_ right from Docker Hub:

`mkdir files && mkdir input_html`

`docker run -d -v input_html:/app/input_html -v files:/app/files -p 127.0.0.1:5000:80 --rm --name html-to-pdf povesma/html-to-pdf`

In this case you can skip `git clone...`, but do not forget to create directories for data persistence (if you need it)


### Note: Data persistency
Mount file system endpoint for data persistency after restarting Docker container:

**/app/files** - to keep resulting PDFs 

**/app/input_html** - to keep HTML sources that were converted to HTML

Please keep in mind, than you can only use **absolute** path for source directory!

# Usage
Use header `Content-type: application/json` send a POST HTTP request to `http://your-server:5000/pdf` 
with JSON body like below:

```
{
    "url":"http://google.com/"
}
```

or

```
{
    "html":"<h1>Welcome!</h1><br>to HTML-2-PDF convertor!"
}
```


You will get a response with a link to your PDF in JSON format
```
{
    "file":"/files/file.pdf"
}
```

_If you provide both url and html, url will prevail._

To access resulting PDF, use URL like: `http://your-server:port/files/file.pdf`

# Testing

## Create PDF from HTML
`curl -H 'Content-type: application/json' -d '{"url":"http://google.com/"}' http://localhost:5000/pdf`

## Create PDF from URL
`curl -H 'Content-type: application/json' -d '{"html":"<h1>Welcome!</h1><br>to HTML-2-PDF convertor!"}' http://localhost:5000/pdf`

## Check the result
Go to URL like `http://localhost:5000/files/da78717f-e09f-413e-81f6-ab39d3351266.pdf`

