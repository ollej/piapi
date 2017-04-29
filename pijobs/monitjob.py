import scrollphat
import settings
import os

from pijobs.matrixjob import MatrixJob

class MonitJob(MatrixJob):
    def init(self):
        self.monit_updater = MonitUpdater(os.environ.get("MONIT_URL"), os.environ.get("MONIT_USERNAME"), os.environ.get("MONIT_PASSWORD"))

    def run(self):
        for i in range(self.options['loop']):
            self.update()
            self.sleep_interval()

    def update(self):
        statuses = self.monit_updater.get_statuses("(apps)")
        matrix = self.convert_to_matrix(statuses)
        self.update_matrix(matrix)

class MonitUpdater:
    def __init__(self, url, username, password):
        self.login(url, username, password)

    def login(self, url, username, password):
        self.url = url
        self.session = requests.session()
        self.get('/index.csp')
        credentials = {
            "z_username": username,
            "z_password": password,
            "z_csrf_protection": "off"
        }
        self.post('/z_security_check', data=credentials)

    def get(self, path):
        return self.session.get(self.url + path)

    def post(self, path, data=None):
        return self.session.post(self.url + path, data)

    def get_statuses(self, match):
        result = self.get("/status/hosts/list")
        return self.extract_statuses(result.json(), match)

    def extract_statuses(self, statuses, match):
        status_leds = []
        for status in statuses['records']:
            if status['hostname'].find(match) > -1:
                status_leds.append(status['heartbeat'])
        return status_leds

