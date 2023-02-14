import shelve
from datetime import date

from flask import make_response, current_app
from flask_restful import Resource, reqparse

from grade import Grade


class GradingService(Resource):

    def post(self, owner, repo, points, max):
        """
        adds the points from GitHub autograding to the db
        :param owner:
        :param repo:
        :param points:
        :param max:
        :return:
        """
        parts = repo.rsplit('-', 1)
        if len(parts) > 1:
            with shelve.open(
                    filename=current_app.config['GRADES'],
                    flag='c'
            ) as grades_db:
                key = parts[1] + '/' + parts[0]
                if key in grades_db:
                    grade = Grade()
                    grade.from_dict(grades_db[key])
                    grade.points = points
                else:
                    grade = Grade(
                        actor=parts[1],
                        repo=parts[0],
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