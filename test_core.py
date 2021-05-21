import pytest
import requests

from cathay.sample.customer import Customer
from cathay.sample.core import CustomerDataProcess
from decimal import Decimal, ROUND_DOWN

INIT_MONEY=100.0

class TestCoreSuites_01:
##########################################################################################
#
# 假設這位客戶, 名字是 Test User, 帳號為100-1100, 一開始帳戶會先存100元, 要測試下面項目:
    test_user = Customer('Test User', '100-1100')
    test_user.deposit(INIT_MONEY)
#
# 1. 之後存款 1000 元, 確認帳戶總金額為 1100 元
    def test_A(ACTMONEY) :
        assert (ACTMONEY == 1100)

    test_user.deposit(1000)
    test_A(test_user.balance)

# 2. 下一步提款 500 元, 確認帳戶總金額為 600 元
    def test_B(ACTMONEY):
        assert (ACTMONEY == 600)

    test_user.withdraw(500)
    test_B(test_user.balance)

# 3. 假設銀行年利率是10%, 經過一年之後確認帳戶餘額為660元
    def test_C(ACTMONEY):
        assert (int(ACTMONEY) == 660)

    CustomerDataProcess().add_interest(test_user, 0.1)
    test_C(test_user.balance)

# 4.之後提款 700 元, pytest 預期會接到 RuntimeError
    @pytest.mark.xfail(raises="RuntimeError: balance not enough")
    def test_whatever(test):
        test.withdraw(700)

    test_whatever(test_user)

# 第二題
class TestCoreSuites_02:
#1.
    response = requests.get('https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/user_info?userid=A123456789')
# 伺服器回應的狀態碼
    assert response.status_code == 200
    print(response.status_code)
#2.
    r = requests.get('https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/company_info?companyid=1')
    assert response.status_code == 200
    print(response.status_code)
##########################################################################################
