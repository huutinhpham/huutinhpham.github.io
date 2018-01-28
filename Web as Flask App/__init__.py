from flask import Flask, Blueprint
from routes import portfolio
from rendezvooo.routes import rendezvooo
from rendezvooo.rendezvooo_api import rendezvooo_api


app = Flask(__name__)

app.register_blueprint(portfolio, url_prefix="")

app.register_blueprint(rendezvooo, url_prefix='/rendezvooo')
app.register_blueprint(rendezvooo_api, url_prefix='/rendezvooo/api')

if __name__ == "__main__":
    app.run()