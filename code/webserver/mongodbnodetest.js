var MongoClient = require('mongodb').MongoClient;
var http = require('http');
var dt = require('./testNode');
var url = "mongodb://CS3012Github:githubcrawler@cluster0-shard-00-00-lj8g0.gcp.mongodb.net:27017,cluster0-shard-00-01-lj8g0.gcp.mongodb.net:27017,cluster0-shard-00-02-lj8g0.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true";
MongoClient.connect(url, function(err, db) {
  if (err) throw err;
  var dbo = db.db("GithubDB");
  dbo.collection("languages").find({}).toArray(function(err, result) {
    if (err) throw err;
    console.log(result);
    db.close();
  });
});



//http.createServer(function (req, res) {
//    res.writeHead(200, {'Content-Type': 'text/html'});
//    res.write("The date and time are currently: " + dt.myDateTime());
//    res.end();
//}).listen(8080);
