#Federal Income Tax Bracket Calculator
income = float(input('Enter your total income this year: '))

if income <= 11000:
    owed_taxes = income * 0.10
elif income <= 44725:
    owed_taxes = (income - 11000) * 0.12 + 1100
elif income <= 95375:
    owed_taxes = (income - 44725) * 0.22 + .1*11000 + 0.12*(44725-11000)
elif income <= 182100:
    owed_taxes = (income - 95375) * 0.24 + .1*11000 + 0.12*(44725-11000) + .22*(95375-44725)
elif income <= 231250:
    owed_taxes = (income - 182100) * 0.32 + .1*11000 + 0.12*(44725-11000) + .22*(95375-44725) + .24*(182100-95375)
elif income <= 578125:
    owed_taxes = (income - 231250) * 0.35 + .1*11000 + 0.12*(44725-11000) + .22*(95375-44725) + .24*(182100-95375) + .32*(231250-182100)
else:
    owed_taxes = (income - 578125) * 0.37 + .1*11000 + 0.12*(44725-11000) + .22*(95375-44725) + .24*(182100-95375) + .32*(231250-182100) + .35*(578125-231250)

print(f'You owe ${owed_taxes:.2f} this year.')
