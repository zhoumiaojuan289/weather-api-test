#基于 Python + pytest + requests + unittest.mock，
# 独立完成天气接口自动化测试项目，覆盖正常返回、404错误、请求超时等场景，
# 使用 mock 实现无网络依赖的稳定测试，代码托管于 GitHub

import pytest
from unittest.mock import patch,Mock
import requests

@patch("requests.get") #patch是根据给的路径，去替换这个位置上的对象
def test_weather_api(mock_get):
    #1.构造一个假的服务器响应，正常返回200
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "weatherinfo": {
            "city": "Shanghai",
            "temp1": "25℃",
            "temp2": "18℃",
            "weather":"小雨"
        }
    }
    mock_get.return_value = mock_response

    #2.调用天气API
    response = requests.get("http://kuaifangguoqingjiele.com")
    assert response.status_code == 200

    data = response.json()
    weather_info = data.get("weatherinfo")

    print(f"城市:{weather_info.get("city")}")
    print(f"温度:{weather_info.get("temp1")} - {weather_info.get("temp2")}")
    print(f"天气:{weather_info.get("weather")}")

    assert "city" in weather_info
    assert "temp1" in weather_info
    assert "temp2" in weather_info

    #定义一个失败场景，失败返回404
@patch("requests.get")
def test_weather_api_404(mock_get):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    
    response = requests.get("http://any_url.com")   
    assert response.status_code == 404
    print("接口返回404，符合预期")

    #3.pytest.raises测异常 实例化可以改状态码验证
@patch("requests.get")
def test_weather_api_timeout(mock_get):
    mock_get.side_effect = requests.exceptions.Timeout("请求超时")

    with pytest.raises(requests.exceptions.Timeout) as exc_info:
        requests.get("any-url.com")

        print(f"捕获到异常：{exc_info.value}")
        assert"请求超时" in str(exc_info.value)