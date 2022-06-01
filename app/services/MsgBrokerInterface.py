from abc import ABCMeta, abstractmethod


class MsgBrokerInterface(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "publish_msg")
            and hasattr(subclass, "response_msg")
            and callable(subclass.load_data_source)
            and NotImplemented
        )

    @abstractmethod
    def publish_msg(self, data: str):
        """Load in the data set"""
        raise NotImplementedError

    @abstractmethod
    def response_msg(self, data: str):
        """Load in the data set"""
        raise NotImplementedError
