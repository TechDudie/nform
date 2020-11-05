def word_form(num):
    ones = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    eleven = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eightteen","nineteen"]
    tens = ["ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
    hundred = int(((num % 1000) - (num % 100)) / 100)
    if num == 0:
        return "zero"
    if hundred == 0:
        one = num % 10
        if num > 10 and num < 20:
            return eleven[num - 11]
        if one == 0:
            ten = num / 10
            return tens[int(ten - 1)]
        if num < 10:
            return ones[one]
        ten = (num - one) / 10
        return tens[int(ten - 1)]  + "-" + ones[one]
    else:
        part = ""
        one = num % 10
        if num > 10 and num < 20:
            part += eleven[num - 11]
            return ones[hundred] + "-hundred " + part
        if (num - hundred * 100) == 0:
            return ones[hundred] + "-hundred "
        if (num - hundred - one) / 10 != 0 and one == 0:
            return ones[hundred] + "-hundred and " + ones[one]
        if (num - hundred * 100) < 10:
            part += ones[one]
            return ones[hundred] + "-hundred " + part
        ten = int(((num - one) / 10) % 10)
        part += tens[int(ten - 1)]  + "-" + ones[one]
        return ones[hundred] + " hundred " + part
