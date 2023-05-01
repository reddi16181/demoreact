var express = require('express');
var app = express();

app.get('/',function(req,res) {
  res.send("Hello World");
});

app.listen(3002);
console.log("open in brower localhost:3002");
