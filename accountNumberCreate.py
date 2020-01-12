import random

def accountNumberC():
    countryCode="PL"
    tCheckSum="00"
    bankNumber = "2500000"
    CheckSumOfBankNumber=0
    for i in bankNumber:
        CheckSumOfBankNumber += int(i)
    bankNumberFull = bankNumber+str(CheckSumOfBankNumber)
    customerInvoice = str(random.randint(0000000000000000, 9999999999999999))
    beforeIBAN=countryCode+tCheckSum+bankNumberFull+customerInvoice


    IBANTemp1 = beforeIBAN[0:4]
    beforeIBAN = beforeIBAN.replace("PL00", "")
    IBANTemp2 = beforeIBAN+IBANTemp1
    IBANTemp3 = IBANTemp2.replace("PL","2521")
    IBANTemp4 = int(IBANTemp3) % 97
    IBANTemp5=0
    if IBANTemp4<10:
        IBANTemp5=IBANTemp4+10 
    IBANTemp6 = 98-IBANTemp5
    checkSum = str(IBANTemp6)
    IBAN=countryCode+checkSum+bankNumberFull+customerInvoice
    print(IBAN)
    return IBAN

accountNumberC()