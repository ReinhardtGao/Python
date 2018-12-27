def espp(basepay, house_funding, rentfee):
    espp_rate = 0.15
    espp_contribution = basepay * espp_rate
    welfare_rate = 0.175
    afterwelfarepay = basepay * (1 - welfare_rate) + house_funding
    aftertaxpay = afterwelfarepay - 0.063 * (basepay + house_funding)
    onhandpay = aftertaxpay - espp_contribution
    print("Your actual income after ESPP is RMB {0}".format(onhandpay))
    value = onhandpay - rentfee
    print('After stored the fee for house, you will still have RMB {0}'.format(value) + " this month")


if __name__ == '__main__':
    b = 11153.85
    h = 892.08
    r = 2765.00
    espp(b, h, r)
