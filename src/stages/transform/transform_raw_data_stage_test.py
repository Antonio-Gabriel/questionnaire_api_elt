from .transform_raw_data import TransformRawData
from ...errors.transform_error import TransformError
from ..contracts.transform_contract import TransformContract
from ..contracts.mocks.extract_contract_mock import extract_contract_mock

def test_transform_questionnaires_raw_data_response():
    """should be return a transform contract transformed"""

    transform_raw_data_stage = TransformRawData()
    transform_response = transform_raw_data_stage\
        .transform(extract_contract_mock)

    isinstance(transform_response, TransformContract)


def test_transform_error():
    """should be return an error"""
    transform_raw_data = TransformRawData()

    try:
        transform_raw_data.transform("It's not run")
    except Exception as ex:
        assert isinstance(ex, TransformError)
