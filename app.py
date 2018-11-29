# -*- coding: utf-8 -*-

import sys
import os
import re
import subprocess
import time

# 起始日期
since = "2018-11-26"
# 提交者名称
author = "xiejunzhao"
# 本地repo路径
repoPaths = [
    "F:\\xjzspace\\gitlab\\liujiaoxiaochu20480yn0dj",
    "F:\\xjzspace\\gitlab\\dafuweng0yn0td"
]
# log命令
gitLogCmd = "git log --since=\"" + since + \
    "\" --author=\"" + author + "\" --no-merges"

temp = '''
周一：	{}

周二：	{}

周三：	{}

周四：	{}

周五：	{}

周六：	{}

周日：  {}

总结：

'''


logMap = {}


def execCmd(cmd):
    p = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, encoding="utf-8")
    return p.stdout.readlines()


def setLog(repoPath):
    os.chdir(repoPath)
    lines = execCmd(gitLogCmd)
    res = "".join(lines).split("commit")

    for log in res:
        info = log.split("\n")
        if len(info) < 3:
            continue

        date = info[2].split(" ")[3]
        logs = [i.strip() for i in info[3:-1] if len(i) > 0]
        dateLogs = logMap.get(date)
        if dateLogs:
            logMap[date] += logs
        else:
            logMap[date] = logs


def main():
    for path in repoPaths:
        setLog(path)

    mondayLogs = "\n\t\t".join(logMap.get("Mon", ""))
    tuesdayLogs = "\n\t\t".join(logMap.get("Tue", ""))
    wednesdayLogs = "\n\t\t".join(logMap.get("Wed", ""))
    thursdayLogs = "\n\t\t".join(logMap.get("Thu", ""))
    fridayLogs = "\n\t\t".join(logMap.get("Fri", ""))
    saturdayLogs = "\n\t\t".join(logMap.get("Sat", ""))
    sundayLogs = "\n\t\t".join(logMap.get("Sun", ""))

    res = temp.format(mondayLogs, tuesdayLogs, wednesdayLogs,
                      thursdayLogs, fridayLogs, saturdayLogs, sundayLogs)

    dateStr = time.strftime("%Y_%m_%d", time.localtime())
    fileName = dateStr + ".txt"

    curPath = "\\".join(__file__.split("\\")[0:-1])
    os.chdir(curPath)

    with open(fileName, "w", encoding='utf-8') as nf:
        nf.write(res)

    print("success!")


main()
