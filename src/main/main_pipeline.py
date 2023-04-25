from ..stages.load.load_data import LoadData
from ..stages.transform.transform_raw_data import TransformRawData
from ..stages.extract.extract_questionnaires import ExtracQuestionnairesStage
from ..stages.contracts.mocks.extract_contract_mock import extract_contract_mock

from ..drivers.http_requester import HttpRequester
from ..gateway.questionnaire_gateway import QuestionnaireGateway

from ..database.tables_statements import TableStatements
from ..services.implementation.answers_implementation import AnswersImplementation
from ..services.implementation.questions_implementation import QuestionsImplementation



class MainPipeline:
    def __init__(self) -> None:        
        self.__extract_stage = ExtracQuestionnairesStage(
            HttpRequester(QuestionnaireGateway(10))
            )
        self.__transform_raw_data = TransformRawData()
        self.__load_data = LoadData(AnswersImplementation(), QuestionsImplementation())

    def run_pipeline(self) -> None:
        """run pupeline"""
        TableStatements.create_table()
        # extract_contract = self.__extract_stage.extract()
        transformed_data_contract = self.__transform_raw_data\
                                        .transform(extract_contract_mock)
        self.__load_data.load(transformed_data_contract)
