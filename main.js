var app = require('./config/express')();
var tryjson = require('tryjson');

var device = require('./routes/device')(tryjson);
app.use('/device', device);

var home = require('./routes/home')(tryjson);
app.use('/', home);

var contact = require('./routes/contact')(tryjson);
app.use('/contact', contact);

// init.d or init.rd
app.listen(2000, function(req,res){
    console.log('Connected, 2000 port!');
});
