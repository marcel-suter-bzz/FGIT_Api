from dataclasses import dataclass
from datetime import datetime


@dataclass
class Grade():
    """
    a grade for an assignment
    """
    actor: str
    repo: str
    courseid: int
    assignmentid: int
    userid: int
    points: float
    updated: datetime

    def to_dict(self):
        """
        returns a dict with the data
        :return:
        """
        data = {
            'actor': self.actor,
            'repo': self.repo,
            'courseid': self.courseid,
            'assignmentid': self.assignmentid,
            'userid': self.userid,
            'points': self.points,
            'updated': self.updated
        }
        return data

    def from_dict(self, dict):
        """
        initialize the object from a dictionary
        :param dict:
        :return:
        """
        self.actor = dict['actor']
        self.repo = dict['repo']
        self.courseid = dict['courseid']
        self.assignmentid = dict['assignmentid']
        self.userid = dict['userid']
        self.points = dict['points']
        self.updated = dict['updated']

    @property
    def actor(self):
        return self._actor

    @actor.setter
    def actor(self, value):
        self._actor = value

    @property
    def repo(self):
        return self._repo

    @repo.setter
    def repo(self, value):
        self._repo = value

    @property
    def courseid(self):
        return self._courseid

    @courseid.setter
    def courseid(self, value):
        self._courseid = value

    @property
    def assignmentid(self):
        return self._assignmentid

    @assignmentid.setter
    def assignmentid(self, value):
        self._assignmentid = value

    @property
    def userid(self):
        return self._userid

    @userid.setter
    def userid(self, value):
        self._userid = value

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        self._points = value

    @property
    def updated(self):
        return self._updated
    
    @updated.setter
    def updated(self, value):
        self._updated = value