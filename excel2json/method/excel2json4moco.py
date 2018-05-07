# -*- coding: utf-8 -*-
# 这段代码主要的功能是把excel表格转换成utf-8格式的json文件
# lastdate:2018-05-07
# 实现功能：索引批量生成json，每个sheet定义表单格式
import os
import sys
import codecs
import xlrd  # http://pypi.python.org/pypi/xlrd

if len(sys.argv) != 2:
    print "argv count != 2, program exit"
    print "USAGE: a.py excelfilename"
    exit(0)
print "excel to json"
excelFileName = sys.argv[1]


def FloatToString(aFloat):
    if type(aFloat) != float:
        return ""
    strTemp = str(aFloat)
    strList = strTemp.split(".")
    if len(strList) == 1:
        return strTemp
    else:
        if strList[1] == "0":
            return strList[0]
        else:
            return strTemp


def table2jsn(table, jsonfilename):
    nrows = table.nrows
    ncols = table.ncols
    f = codecs.open(jsonfilename, "w", "utf-8")
    '''json
    f.write(u"{\n\t\"list\":[\n")
    for r in range(nrows - 1):
        f.write(u"\t\t{ ")
        for c in range(ncols):
            strCellValue = u""
            CellObj = table.cell_value(r + 1, c)
            if type(CellObj) == unicode:
                strCellValue = CellObj
                cellValue = table.cell_value(0, c)
            elif type(CellObj) == float:
                strCellValue = FloatToString(CellObj)
            else:
                strCellValue = str(CellObj)
                cellValue = table.cell_value(0, c)
            print(strCellValue)
            strTmp = u"\"" + table.cell_value(0,c) + u"\":" + strCellValue
            if c < ncols - 1:
                strTmp += u", "
            f.write(strTmp)
        f.write(u" }")
        if r < nrows - 2:
            f.write(u",")
        f.write(u"\n")
    f.write(u"\t]\n}\n")
    '''
    #u自定义
    f.write(u"[\n\t{\n\t\t\"request\":\n\t\t{\n")
    f.write(u"\t\t\t")
    for c in range(ncols):
        strCellValue = u""
        CellObj = table.cell_value(2, c)
        if type(CellObj) == unicode:
            strCellValue = CellObj
        elif type(CellObj) == float:
            strCellValue = FloatToString(CellObj)
        else:
            strCellValue = str(CellObj)
        #print(strCellValue) #项值
        strTmp = u"\"" + table.cell_value(1, c) + u"\":" + strCellValue
        if c < ncols - 1:
            strTmp += u",\n\t\t\t"
        f.write(strTmp)
    f.write(u"\n")
    f.write(u"\t\t},\n")
    f.write(u"\t\t\"response\":\n\t\t{\n")
    f.write(u"\t\t\t")
    for d in range(ncols):
        strCellValue = u""
        CellObj = table.cell_value(5, d)
        if type(CellObj) == unicode:
            strCellValue = CellObj
        elif type(CellObj) == float:
            strCellValue = FloatToString(CellObj)
        else:
            strCellValue = str(CellObj)
        # print(strCellValue) #项值

        u'空值项不写入json'
        if table.cell_value(4, d) != u"":
            strTmp = u"\"" + table.cell_value(4, d) + u"\":" + strCellValue
        else:
            strTmp = u""
        if d < ncols - 1:
            if table.cell_value(4, d+1) != u"":
                strTmp += u",\n\t\t\t"
            else:
                strTmp += u""
        f.write(strTmp)

    f.write(u"\n\t\t}\n")
    f.write(u"\t}\n]")
    f.close()
    print "Create ", jsonfilename, " OK"
    return


data = xlrd.open_workbook(excelFileName)
table = data.sheet_by_name(u"tablelist")
rs = table.nrows
for r in range(rs - 1):
    print table.cell_value(r + 1, 0), "==>", table.cell_value(r + 1, 2)
    desttable = data.sheet_by_name(table.cell_value(r + 1, 0))
    destfilename = table.cell_value(r + 1, 2)
    table2jsn(desttable, destfilename)

print "All OK"