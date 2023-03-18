import time
from flask import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def ksyusha_timetable():
    data_set = {'Test': '1', 'Timestamp': time.time()}
    json_dump = json.dumps(data_set)
    return json_dump


if __name__ == "__main__":
    app.run()
