import pytest

from src.gateway.questionnaire_gateway import (
    QuestionnaireGateway
)

@pytest.mark.asyncio
async def test_questionnaire_gateway():
    """should be return status 200"""

    questionnaire_gateway = QuestionnaireGateway(5)
    async with questionnaire_gateway.get_async() as gateway:
        status, questionnaires = gateway

        assert status == 200
        assert isinstance(questionnaires, list)
