# htmltopdf
webservice for htmltopdf conversion

# Usage

* send a post request to  `http://host-url:port/pdf` with json body like below
`{
"url":"http://google.com/"
}`

* you will get a response with  a link to  your pdf in json format
`{
"file":"http://host-url:port/temp/file.pdf"
}`

