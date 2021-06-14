var express = require('express');
var exphbs  = require('express-handlebars');
var path = require('path');

var app = express();

app.engine('handlebars', exphbs());
app.set('view engine', 'handlebars');
app.set('views', path.join(__dirname, '/views'));
app.use(express.static(path.join(__dirname, 'public')));

app.get('/', function (req, res) {
    res.render('home');
});

app.listen(3000, function(){
    console.log("Server is running at http://localhost:3000")
});