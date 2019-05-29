# wdb


## 安装

```shell
pip install wdb.server
```

运行`wdb.server.py`看安装书否正常. 如果遇到下面错误:

```python
TypeError: fetch() got multiple values for argument 'raise_error'
```

说明`tornado`版本不对, 比如我这里显示的是`tornado==6.0.2`,换个低版本:

```python
pip install tornado==5.1.1
```



## 启动

启动server

```
wdb.server.py
```

启动调试脚本

```
python -m wdb your_file.py
```

打开浏览器,输入`http://localhost:1984/`



但是实际试了几次,`python -m wdb your_file.py`并没有停下来.

