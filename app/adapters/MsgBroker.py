from app.infrastructure.FileStore import FileStore
from app.services.MsgBrokerInterface import MsgBrokerInterface

loMSgBroker = FileStore()


class MsgBroker(MsgBrokerInterface):
    def publish_msg(self, msg: str):
        loMSgBroker.publish_msg()
        pass

    def response_msg(self, status: str):
        loMSgBroker.response_msg()
        pass
