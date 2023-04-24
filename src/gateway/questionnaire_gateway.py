import aiohttp, os
from aiohttp import ClientTimeout
from contextlib import asynccontextmanager

from .contract.questionnaire_gateway_interface import (
    QuestionnaireGatewayInterface
)

class QuestionnaireGateway(QuestionnaireGatewayInterface):

    def __init__(self, timeout: int) -> None:
        self._timeout = ClientTimeout(timeout)

    @asynccontextmanager
    async def get_async(self):
        """get questionnaires async"""
          
        async with aiohttp.ClientSession(timeout=self._timeout) as session:
            async with session.get(os.environ["URL_BASE"]) as response:
                if response.status != 200:
                    response.raise_for_status()
                            
                yield response.status, await response.json() 
