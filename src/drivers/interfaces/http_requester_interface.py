from abc import ABC, abstractmethod


class HttpRequesterInterface(ABC):
    @abstractmethod
    async def get_questionnaires(self):
        """get questionnaires of an externanl api"""

        return NotImplementedError("Method not implemented")
