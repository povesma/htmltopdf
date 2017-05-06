# htmltopdf
webservice for htmltopdf conversion

# Usage

* `mkdir -p app/temp`
* `docker build -t htmltopdf .`
* `docker run -d -v ./app:/app -p 5000:80 htmltopdf

* send a post request to  `http://host-url:port/pdf` with json body like below
`{
"url":"http://google.com/"
}`

* you will get a response with  a link to  your pdf in json format
`{
"file":"http://host-url:port/temp/file.pdf"
}`

