from flask import Flask
from jsons_base import return_json_base
app = Flask(__name__)


@app.route('/log')
def get_log():
    return return_json_base.return_log()

@app.route('/rt')
def get_rt():
    return return_json_base.return_rt()

if __name__ == '__main__':
    app.run()