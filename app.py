from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from gh_gradingservice import GradingService
from mdl_assignmentservice import MdlAssignmentService

from logging.config import dictConfig

app = Flask(__name__)
CORS(app)
app.config.from_pyfile('./.env')
dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
            }
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "stream": "ext://sys.stdout",
                "formatter": "default",
            },
            "file": {
                "class": "logging.FileHandler",
                "filename": app.config['LOG_FILE'],
                "formatter": "default",
            },

        },
        "root": {
            "level": app.config['LOG_LEVEL'],
            "handlers": ["console", "file"]
        },
    }
)
api = Api(app)
api.add_resource(GradingService, '/gh_grade/<actor>/<owner>/<repo>/<points>/<max>')
api.add_resource(MdlAssignmentService, '/mdl_assign/<actor>/<repo>/<assignid>/<courseid>/<userid>', '/db_show')

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
