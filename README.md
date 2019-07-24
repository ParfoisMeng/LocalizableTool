# Localizable Tool 使用说明

Android 开发国际化可视化工具，可将 `strings.xml` 与 Excel 互相转换。

> 1. 核心 Python 脚本代码来自 Github 开源项目 [Localizable.strings2Excel](https://github.com/CatchZeng/Localizable.strings2Excel) ，在其基础上做了一定的修改以适配 Python3。
> 2. 可视化界面使用 [PyQt5](https://pypi.org/project/PyQt5/) 编写。
> 3. 本工具的开发是边学边写，所以内部代码写的很渣。

- - - - - 


#### 页面说明

![App截图](https://raw.githubusercontent.com/ParfoisMeng/LocalizableTool/master/screenshot/1.png)

上图各标识点说明：
1. 选择是 Xml2Xls(`strings.xml`转Excel) 还是 Xls2Xml(Excel转`strings.xml`) ，默认为前者。
2. 选择源文件夹。如果是 Xml2Xls 则选择来源的 Xml 相关文件夹路径(应包含 values/values-en 等文件夹)，如果是 Xls2Xml 则选择来源的 Excel 相关文件夹路径(应包含一个或多个文件夹)。
3. 选择目标文件夹。如果是 Xml2Xls 则选择生成目标 Excel 的路径，如果是 Xls2Xml 则选择生成目标 Xml 的路径。
4. 选择 Single(单文件) 还是 Multiple(多文件) 模式。Xml2Xls 在 Single 模式下会生成以语种为列名的单个 Excel 文件，在 Multiple 模式下会生成对应语种的多个 Excel 文件；Xls2Xml 与 Xml2Xls 对应，Single 模式需要选择以语种为列名的单个 Excel 文件，Multiple 需要选择对应语种的多个 Excel 文件。
5. 生成的脚本语言。使用此可视化工具时可以不用关注。
6. 复制 5 中的脚本语言到剪贴板。使用此可视化工具时可以不用关注。
7. 执行转换。