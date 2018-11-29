var MongoClient = require('mongodb').MongoClient;

var url = "mongodb://CS3012Github:githubcrawler@cluster0-shard-00-00-lj8g0.gcp.mongodb.net:27017,cluster0-shard-00-01-lj8g0.gcp.mongodb.net:27017,cluster0-shard-00-02-lj8g0.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true";

module.exports = {
  languages: function() {
    return MongoClient.connect(url).then(function(db) {
      var collection = db.db("GithubDB").collection('languages');
      return collection.find().toArray();
    }).then(function(items) {
      return items;
    });
  }
};
