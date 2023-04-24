from datetime import date

from ...drivers.interfaces.http_requester_interface import (
    HttpRequesterInterface
)

from ...errors.extract_error import ExtractError
from ..contracts.extract_contract import ExtractContract

class ExtracQuestionnairesStage:
    def __init__(self, http_requester: HttpRequesterInterface) -> None:
        self.__http_requester = http_requester
    
    async def extract(self) -> ExtractContract:
        """extract questionnaires from external api"""
        
        try:
            questionnaires = await self.__http_requester.get_questionnaires()

            return ExtractContract(
                raw_information_content=questionnaires
            )
        except Exception as exception:
            raise ExtractError(str(exception.args)) from exception
