import shelve
from datetime import date, datetime

from flask import make_response, current_app
from flask_restful import Resource
import json

from grade import Grade


class MdlAssignmentService(Resource):
    def post(self, actor, repo, assignid, courseid, userid):
        """
        adds a user in a moodle assignment to the database
        :param actor:
        :param repo:
        :param assignid:
        :param courseid:
        :param userid:
        :return:
        """
        with shelve.open(
                filename=current_app.config['GRADES'],
                flag='c'
        ) as grades_db:
            key = actor + '/' + repo
            if key in grades_db:
                grade = Grade()
                grade.from_dict(grades_db[key])
            else:
                grade = Grade()
                grade.points = -1.0
            grade.actor = actor
            grade.repo = repo.lower()
            grade.courseid = courseid
            grade.assignmentid = assignid
            grade.userid = userid
            grade.updated = date.today()
            grades_db[key] = grade.to_dict()

        return make_response(
            'done', 200
        )

    def get(self):
        """
        reads the db and returns a json-array
        :return:
        """
        with shelve.open(
                filename=current_app.config['GRADES'],
                flag='r'
        ) as grades_db:
            output = '['
            keys = list(grades_db.keys())
            for key in keys:
                output += json.dumps(grades_db[key], default=self.json_serial) + ','
            output = output[:-1] + ']'

        return make_response(
            output, 200
        )

    def json_serial(self, obj):
        """JSON serializer for objects not serializable by default json code"""

        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        raise TypeError("Type %s not serializable" % type(obj))
