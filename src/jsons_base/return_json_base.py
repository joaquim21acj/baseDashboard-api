import json

def return_log():
    return json.loads('''{
            "log": [
            {
                "dtgRX": "aaaa-mm-dd-hh-mm-ss",
                "dtg": [
                "2019-12-13",
                19,
                40,
                52
                ],
                "pkgCount": "xxxxxx",
                "azElPo": [
                0.04443359375,
                -0.98486328125,
                -0.183349609375
                ],
                "dtgTele": "aaaa-mm-dd-hh-mm-ss",
                "base1": {
                "posBase": "xx.xxxx,yy.yyyy,zz.zzzz",
                "posSat": "xx.xxxx,yy.yyyy,zz.zzzz",
                "dtgBase": "aaaa-mm-dd-hh-mm-ss"
                },
                "base2": {
                "posBase": "xx.xxxx,yy.yyyy,zz.zzzz",
                "posSat": "xx.xxxx,yy.yyyy,zz.zzzz",
                "dtgBase": "aaaa-mm-dd-hh-mm-ss"
                },
                "base3": {
                "posBase": "xx.xxxx,yy.yyyy,zz.zzzz",
                "posSat": "xx.xxxx,yy.yyyy,zz.zzzz",
                "dtgBase": "aaaa-mm-dd-hh-mm-ss"
                },
                "posSat": "xx.xxxx,yy.yyyy,zz.zzzz",
                "rssi": "xxx",
                "latLongBase": "xx.xxxx,yy.yyyy,zz.zzzz"
            },
            {
                "dtgRX": "aaaa-mm-dd-hh-mm-ss",
                "dtg": [
                "2019-12-13",
                19,
                40,
                53
                ],
                "pkgCount": "xxxxxx",
                "azElPo": [
                0.04443359375,
                -0.987548828125,
                -0.174560546875
                ],
                "dtgTele": "aaaa-mm-dd-hh-mm-ss",
                "base1": {
                "posBase": "xx.xxxx,yy.yyyy,zz.zzzz",
                "posSat": "xx.xxxx,yy.yyyy,zz.zzzz",
                "dtgBase": "aaaa-mm-dd-hh-mm-ss"
                },
                "base2": {
                "posBase": "xx.xxxx,yy.yyyy,zz.zzzz",
                "posSat": "xx.xxxx,yy.yyyy,zz.zzzz",
                "dtgBase": "aaaa-mm-dd-hh-mm-ss"
                },
                "base3": {
                "posBase": "xx.xxxx,yy.yyyy,zz.zzzz",
                "posSat": "xx.xxxx,yy.yyyy,zz.zzzz",
                "dtgBase": "aaaa-mm-dd-hh-mm-ss"
                },
                "posSat": "xx.xxxx,yy.yyyy,zz.zzzz",
                "rssi": "xxx",
                "latLongBase": "xx.xxxx,yy.yyyy,zz.zzzz"
            }
            ]
        }'''), 200

def return_rt():
    return json.loads('''{
    "realTime": [
      {
        "dtgRX": "aaaa-mm-dd-hh-mm-ss",
        "dtg": [
          "2019-12-18",
          22,
          20,
          16
        ],
        "pkgCount": "xxxxxx",
        "azElPo": [
          -24.894729888358835,
          -58.88120092723473,
          3.4404761904761907
        ],
        "dtgTele": "aaaa-mm-dd-hh-mm-ss",
        "base1": {
          "posBase": "xx.xxxx,yy.yyyy,zz.zzzz",
          "posSat": "xx.xxxx,yy.yyyy,zz.zzzz",
          "dtgBase": "aaaa-mm-dd-hh-mm-ss"
        },
        "base2": {
          "posBase": "xx.xxxx,yy.yyyy,zz.zzzz",
          "posSat": "xx.xxxx,yy.yyyy,zz.zzzz",
          "dtgBase": "aaaa-mm-dd-hh-mm-ss"
        },
        "base3": {
          "posBase": "xx.xxxx,yy.yyyy,zz.zzzz",
          "posSat": "xx.xxxx,yy.yyyy,zz.zzzz",
          "dtgBase": "aaaa-mm-dd-hh-mm-ss"
        },
        "posSat": "xx.xxxx,yy.yyyy,zz.zzzz",
        "rssi": "xxx",
        "latLongBase": "xx.xxxx,yy.yyyy,zz.zzzz"
      }
    ]
  }'''), 200