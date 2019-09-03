var bb8Key = require('./bb8.json');
var Cylon = require('cylon');
var flag = 0
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.urlencoded({
  extended: true
}));
app.use(bodyParser.json());

app.listen(3000);
Cylon.robot({
  connections: {
    bluetooth: { adaptor: 'central', uuid: bb8Key.uuid, module: 'cylon-ble'}
  },

  devices: {
    bb8: { driver: 'bb8', module: 'cylon-sphero-ble'},
  },
  work: (my) => {
    my.bb8.color('blue');
    app.post('/', function (req, res) {
      console.log(req.body);
      if(req.body["ID"] == 'sleepy1') {
        my.bb8.color('red');
        if(flag == 111) {
          res.send('Wake up!!! BB8 will come to you.');
          my.bb8.setHeading(0);
          my.bb8.roll(60, 0);
          flag = 1;
        }
        res.send('Wake up!');
        my.bb8.spin('right', 100);
      }
      else if(req.body["ID"] == 'sleepy2') {
        my.bb8.color('red');
        res.send('Wake up!!');
        my.bb8.spin('right', 150);
      }
      else if(req.body["ID"] == 'sleepy3') {
        my.bb8.color('red');
        res.send('Wake up!!!');
        my.bb8.spin('right', 200);
      }
      else if(req.body["ID"] == 'sleepy4') {
        my.bb8.color('red');
        res.send('Wake up!!!!');
        my.bb8.spin('right', 250);
        after(2000, function() {
          my.bb8.stop();
        });
        my.bb8.spin('left', 250);
        after(2000, function() {
          my.bb8.stop();
        });
      }
      else if(req.body["ID"] == 'awake') {
        res.send('OK. You are awake.');
        my.bb8.color('green');
        my.bb8.stop();
      }
    })}
  }).start();
