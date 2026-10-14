markdown
# 天气接口自动化测试test_weather.py

## 技术栈
- Python
- pytest
- requests
- unittest.mock

## 运行方式
pip install -r requirements.txt
python -m pytest tests/ -v
python -m pytest test_weather.py -v -s

## 测试覆盖
- 正常返回 200
- 404 错误场景
- 请求超时异常
- 使用 parametrize 覆盖多城市数据驱动测试（北京、上海、伦敦、纽约）

## 说明
使用 mock 实现无网络依赖的稳定测试
项目结构清晰，覆盖正常、失败、异常三类场景，并通过 parametrize 实现数据驱动。