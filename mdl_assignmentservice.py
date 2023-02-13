import shelve

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
                grade.points = 0.0
            grade.actor = actor
            grade.repo = repo
            grade.courseid = courseid
            grade.assignmentid = assignid
            grade.userid = userid
            grades_db[key] = grade.to_dict()

    def get(self):
        """
        reads the db an returns a json-array
        :return:
        """
        with shelve.open(
                filename=current_app.config['GRADES'],
                flag='r'
        ) as grades_db:
            output = '['
            keys = list(grades_db.keys())
            for key in keys:
                output += json.dumps(grades_db[key])
            output += ']'

        return make_response(
            output, 200
        )