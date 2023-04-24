import pytest

from .http_requester import HttpRequester
from ..gateway.questionnaire_gateway import QuestionnaireGateway


@pytest.mark.asyncio
async def test_http_questionnaires_request():
    """should be return a questionnaire json"""

    http_requester = HttpRequester(QuestionnaireGateway)
    response = await http_requester.get_questionnaires()

    assert isinstance(response, list)
