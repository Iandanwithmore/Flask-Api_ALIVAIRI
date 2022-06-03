from datetime import datetime

from app.config import Config
from app.fn_base import FnBase


class FileStore:
    now = datetime.now()

    def publish_msg(self, msg: str):
        if FnBase.isJson(msg):
            with open(
                Config.ROOT_DIR + self.now.strftime("%Y-%m-%d") + "/publish.txt",
                encoding="utf-8",
            ) as f:
                f.write(msg + "\n")

    def response_msg(self, msg: str):
        if FnBase.isJson(msg):
            with open(
                Config.ROOT_DIR + self.now.strftime("%Y-%m-%d") + "/response.txt",
                encoding="utf-8",
            ) as f:
                f.write(msg + "\n")
