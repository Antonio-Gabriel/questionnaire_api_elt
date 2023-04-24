import pytest

from ...drivers.http_requester import HttpRequester
from ..contracts.extract_contract import ExtractContract
from .extract_questionnaires import ExtracQuestionnairesStage
from ...gateway.questionnaire_gateway import QuestionnaireGateway


@pytest.mark.asyncio
async def test_extract_questionnaires_from_requester_stage():
    """should be return extract contract with data in"""
    
    http_requester = HttpRequester(QuestionnaireGateway)
    extract_stage = ExtracQuestionnairesStage(http_requester)
    extract_response = await extract_stage.extract()

    assert isinstance(extract_response, ExtractContract)
