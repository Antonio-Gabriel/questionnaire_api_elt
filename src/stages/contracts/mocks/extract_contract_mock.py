from datetime import date

from ..extract_contract import ExtractContract
from ....drivers.mocks.questionnaire_mock import get_questionnaires_mock

extract_contract_mock = ExtractContract(
    raw_information_content=get_questionnaires_mock()    
)
