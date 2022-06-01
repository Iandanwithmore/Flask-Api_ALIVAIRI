from abc import ABCMeta, abstractmethod


class ActivityRepositoryInterface(metaclass=ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(cls, "ok")
            and hasattr(cls, "data")
            and hasattr(subclass, "get_by_id")
            and callable(subclass.load_data_source)
            and NotImplemented
        )

    @abstractmethod
    def get_by_id(self, data: str):
        """Load in the data set"""
        raise NotImplementedError
