import os

from typing import Callable, Iterable
from contextlib import AbstractAsyncContextManager

from ..gateway.contract.questionnaire_gateway_interface import  (
    QuestionnaireGatewayInterface
)
from .interfaces.http_requester_interface import (
    HttpRequesterInterface
)


class HttpRequester(HttpRequesterInterface):
    """http requester drive"""

    def __init__(self, 
                 questionnaire_gateway: Callable[..., 
                        AbstractAsyncContextManager[QuestionnaireGatewayInterface]]
            ) -> None:
        self.__questionnaire_gateway = questionnaire_gateway
    
    async def get_questionnaires(self) -> Iterable[list]:
        """get external questionnaires"""

        async with self.__questionnaire_gateway(int(os.environ["TIMEOUT"])).get_async() as gateway:            
            _, questionnaires = gateway

        return questionnaires
