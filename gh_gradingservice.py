import shelve
from datetime import date

from flask import make_response, current_app
from flask_restful import Resource, reqparse

from grade import Grade


class GradingService(Resource):

    def post(self, actor, repo, points):
        """
        adds the points from GitHub autograding to the db
        :param actor:
        :param repo:
        :param points:
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
                grade.points = points
            else:
                grade = Grade(
                    actor=actor,
                    repo=repo,
                    courseid=0,
                    assignmentid=0,
                    userid=0,
                    points=points
                )
            grade.updated = date.today()
            grades_db[key] = grade.to_dict()

        return make_response(
            'done', 200
        )