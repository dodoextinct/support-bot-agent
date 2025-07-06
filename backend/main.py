from flask import Flask
from dotenv import load_dotenv
import logging
import os
from flask_cors import CORS, cross_origin

# Load env vars
load_dotenv()

# Logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger("pymongo").setLevel(logging.WARNING)

# Init Flask app
app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

# Register agent route
from routes.support import support_bp
app.register_blueprint(support_bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
