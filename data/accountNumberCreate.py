import random

def accountNumberCreate():
    #Variables
    minRandom = 0000000000000000
    maxRandom = 9999999999999999
    countryCode = "PL"
    tCheckSum = "00"
    bankNumber = "2500000"
    CheckSumOfBankNumber=0

    for i in bankNumber:
        CheckSumOfBankNumber += int(i)
    bankNumberFull = bankNumber+str(CheckSumOfBankNumber)
    customerInvoice = str(random.randint(minRandom, maxRandom))
    beforeIBAN=countryCode+tCheckSum+bankNumberFull+customerInvoice
    beforeIBANT1 = beforeIBAN[0:4]
    beforeIBANT2 = beforeIBAN.replace(beforeIBANT1,"")
    beforeIBANT3 = beforeIBANT2+beforeIBANT1
    beforeIBANT4 = beforeIBANT3.replace(countryCode, "2521")
    beforeIBANT5 = int(beforeIBANT4) % 97
    beforeIBANT6 = 98-beforeIBANT5
    if beforeIBANT6<10:
        beforeIBANT6*=10
    checkSum = str(beforeIBANT6)
    IBAN=countryCode+checkSum+bankNumberFull+customerInvoice
    return IBAN

def accountNumberCheck(IBAN):
    IBANToCheck=IBAN
    IBANTemp1 = IBANToCheck[0:4]
    IBANToCheck = IBANToCheck.replace(IBANTemp1, "")
    IBANTemp2 = IBANToCheck+IBANTemp1
    IBANTemp3 = IBANTemp2.replace("PL","2521")
    IBANTemp4 = int(IBANTemp3) % 97
    if IBANTemp4 == 1:
        return True
