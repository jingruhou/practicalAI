has_high_income = False
has_good_credit = True

has_criminal_record = True

if has_high_income and has_good_credit:
    print("Eligible for loan -- and operator")  # 贷款合格


if has_high_income or has_good_credit:
    print("Eligible for loan -- or operator")


if has_good_credit and not has_criminal_record:
    print("Eligible for loan -- not operation")
"""
    and:逻辑与 - 都是
    or:逻辑或 - 至少有一个
    not:逻辑非 - 不是
"""

