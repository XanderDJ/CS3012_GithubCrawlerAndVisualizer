var http = require("http");
var fs = require('fs');
http.createServer(function (req, res) {
  fs.readFile('test.html', function(err, data) {
  res.writeHead(200, {'Content-Type': 'text/javascript'});
  res.write(data);
  res.end();
});
}).listen(8080);
