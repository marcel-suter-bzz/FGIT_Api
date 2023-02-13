from dataclasses import dataclass


@dataclass
class Grade():
    """
    a grade for an assignment
    """
    actor: str
    repo: str
    courseid: int = 0
    assignmentid: int = 0
    userid: int = 0
    points: float = 0.0

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
            'points': self.points
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
