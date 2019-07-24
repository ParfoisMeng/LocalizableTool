#!/usr/bin/python
# -*- coding: UTF-8 -*-

import xlrd


class XlsFileUtil:
    'xls file util'

    def __init__(self, filePath):
        self.filePath = filePath
        # get all sheets
        self.data = xlrd.open_workbook(filePath)

    def getAllTables(self):
        return self.data.sheets()

    def getTableByIndex(self, index):
        if 0 <= index < len(self.data.sheets()):
            return self.data.sheets()[index]
        else:
            print("XlsFileUtil error -- getTable:index")

    def getTableByName(self, name):
        return self.data.sheet_by_name(name)
