import random
def accountNumberCheck(IBAN):
    IBANToCheck=IBAN
    IBANTemp1 = IBANToCheck[0:4]
    IBANToCheck = IBANToCheck.replace(IBANTemp1, "")
    IBANTemp2 = IBANToCheck+IBANTemp1
    IBANTemp3 = IBANTemp2.replace("PL","2521")
    IBANTemp4 = int(IBANTemp3) % 97
    if IBANTemp4 == 1:
        return True
