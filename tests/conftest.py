import pytest
from unittest.mock import Mock
#插入fixture，模拟成功返回的响应
@pytest.fixture
def mock_success_response():
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "weatherinfo":{
            "city":"shanghai",
            "temp1":"25℃",
            "temp2":"18℃",
            "weather":"小雨"
        }
    }
    return mock_response
    #return None #改坏测试fixture，返回None，模拟失败的情况
    