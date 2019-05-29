# python-Debugging-skills
整理一些python调试相关的方法, 列举出一些各个场景下使用的例子。

## 调试方法

| 名称     | 描述                                            | 详情                                                         |
| -------- | ----------------------------------------------- | ------------------------------------------------------------ |
| pdb      | 通过设置断点一步步调试. 有点像命令行版的vs调试. | [链接](https://www.ibm.com/developerworks/cn/linux/l-cn-pythondebugger/index.html) |
| **pudb** | 带界面的调试器. 调试脚本非常方便~               | [链接](debugging/pudb.md)                                    |
| **wdb**  | web debugger                                    | [链接](https://github.com/Kozea/wdb)                         |
|          |                                                 |                                                              |

## 代码



| 文件名               | 描述               | 路径                                           |
| -------------------- | ------------------ | ---------------------------------------------- |
| main.py              | 测试调试           | [main](code/main.py)                           |
| multiprocess_main.py | 测试pudb多进程调试 | [multiprocess_main](code/multiprocess_main.py) |
|                      |                    |                                                |

