import os
import re
import time

def getFormerID():
    id = input("Please enter your former ID:\n请输入您之前的ID：")
    return id

def getLaterID():
    id = input("Please enter the ID you want to change to:\n请输入您想更改成的ID：")
    return id

def getUUID(id):
    findUUID = re.compile(r'"name":"'+id+'","uuid":"(.*?)","expiresOn"')
    f = open("usercache.json", "r")
    text = f.readline()
    print(text)
    UUIDtable = re.findall(findUUID, text)
    UUID = UUIDtable[0]
    print(UUID)
    return UUID

def delDat(UUID):
    try:
        os.remove('./world/playerdata/' + UUID + '.dat')
    except FileNotFoundError:
        pass
    try:
        os.remove('./world/playerdata/' + UUID + '.dat_old')
    except FileNotFoundError:
        pass
    return 0

def rewriteDat(formerUUID,laterUUID):
    try:
        os.rename('./world/playerdata/' + formerUUID + '.dat', './world/playerdata/' + laterUUID + '.dat')
    except FileNotFoundError:
        print("Didn't find user " + formerUUID + "\nPlease make sure you entered the right id")
        print("没有找到账户 " + formerUUID + "\n请确保你输入了正确的id。")
        return 1
    try:
        os.rename('./world/playerdata/' + formerUUID + '.dat_old', './world/playerdata/' + laterUUID + '.dat_old')
    except FileNotFoundError:
        print("Didn't find user " + formerUUID + "\nPlease make sure you entered the right id")
        print("没有找到账户 " + formerUUID + "\n请确保你输入了正确的id。")
        return 1
    return 0

def main():
    print("Please make sure that you have already entered the server with your new id, otherwise this program may not work!\n请确保您已使用您想更改的ID进入过服务器，否则该程序可能无法正常运行！")
    formerID = getFormerID()
    laterID = getLaterID()
    formerUUID = getUUID(formerID)
    laterUUID = getUUID(laterID)
    delDat(laterUUID)
    status = rewriteDat(formerUUID, laterUUID)
    if(status == 0):
        print("\nSuccess!")
    elif(status == 1):
        print("\nFailed...")
    input()

    return 0

if __name__ == "__main__":
    main()