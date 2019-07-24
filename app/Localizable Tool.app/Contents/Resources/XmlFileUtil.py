#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import xml.dom.minidom

from python.Log import *


class XmlFileUtil:
    'android strings.xml file util'

    @staticmethod
    def writeToFile(keys, values, directory, filename):
        if not os.path.exists(directory):
            os.makedirs(directory)

        fo = open(directory + "/" + filename, "wb")

        fo.write("<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<resources>\n".encode())

        for x in range(len(keys)):
            if values[x] is None or values[x] == '':
                Log.error("Key:" + keys[x] +
                          "\'s value is None. Index:" + str(x + 1))
                continue

            content = "   <string name=\"" + keys[x].strip() + "\">" + values[x].strip() + "</string>\n"
            fo.write(content.encode())

        fo.write("</resources>".encode())
        fo.close()

    @staticmethod
    def getKeysAndValues(path):
        if path is None:
            Log.error('file path is None')
            return

        dom = xml.dom.minidom.parse(path)
        root = dom.documentElement
        itemlist = root.getElementsByTagName('string')

        keys = []
        values = []
        for index in range(len(itemlist)):
            item = itemlist[index]
            key = item.getAttribute("name")
            value = item.firstChild.data
            keys.append(key)
            values.append(value)

        return (keys, values)
