var express = require('express');
var bodyParser = require('body-parser'); // for app.post 

var app = express();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.locals.pretty = true;

app.post('/sensor', function(req,res){
    res.setHeader('Content-Type', 'application/json');
    
    //mimic a slow network connection
    setTimeout(function(){
        //console.log("json test : "+req.body.cardno);
        res.send(JSON.stringify({
             DeviceName: req.body.name || null,
             DeviceStatus: req.body.status || null
        }));
    }, 1000)
    var info = req.body;
    console.log("Temperature : "+info.temperature+" °C, " + "Humidity :"+info.humidity+" % "+ "Status : "+info.status);
    
});

app.listen(2000, function(req,res){
    console.log('Connected, 2000 port!');
});
