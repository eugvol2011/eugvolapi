import time
from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    data_set = {'Test': '2', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    return json_dump


if __name__ == "__main__":
    app.run()
