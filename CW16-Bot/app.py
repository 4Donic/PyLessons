from flask import Flask
from config import Configuration
from flask import request

app = Flask(__name__)
app.config.from_object(Configuration)






# @app.route('/', methods=['POST'])
# def index():
#     if request.method == ['POST']:
#         resp = request.get_json()
#     return resp
#
#
# if __name__ == '__main__':
#     app.run()