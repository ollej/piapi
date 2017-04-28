import scrollphat
from pijobs.scrollphatjob import ScrollphatJob
from pyteamcity import TeamCity

class BuildsJob(ScrollphatJob):
    def __init__(self, options):
        self.tc = TeamCity('dashing', 'l,sA-j2s9a', 'https://ci.avidity.se/httpAuth/app/rest/')

    def run(self):
        print(self.tc.get_projects())

BuildsJob({}).run()
