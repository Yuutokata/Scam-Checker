from flask import Flask
from flask_cors import CORS

from utils.config import Config
from utils.logger import logger

from routes.phishing import phishing
from routes.safesearch import safeSearch
from routes.dnsrecords import dns_records

config = Config()


class WebServer(Flask):
    def __init__(self):
        super().__init__(__name__)

    def configure_routes(self):
        logger.info("Configure Routes")

        self.add_url_rule("/check/phishing", view_func=phishing, methods=["GET"])
        self.add_url_rule("/check/safe-search", view_func=safeSearch, methods=["GET"])
        self.add_url_rule("/check/dns", view_func=dns_records, methods=["GET"])

    def run(self):
        logger.info("Starting Webserver", extra={"emoji": ":bomb:"})

        self.configure_routes()

        CORS(self)  # Cross Origin Resource Sharing

        super().run(config.ip, config.port)
