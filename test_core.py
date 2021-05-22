import pytest
import requests

from cathay.sample.customer import Customer
from cathay.sample.core import CustomerDataProcess
from decimal import Decimal, ROUND_DOWN

INIT_MONEY = 100.0

class TestCoreSuites(object):
##########################################################################################
# 假設這位客戶, 名字是 Test User, 帳號為100-1100, 一開始帳戶會先存100元, 要測試下面項目:
    test_user = Customer('Test User', '100-1100')
    test_user.deposit(INIT_MONEY)

# 1. 之後存款 1000 元, 確認帳戶總金額為 1100 元
    def test_1A(self) :
        self.test_user.deposit(1000)
        assert(self.test_user.balance == 1100)

# 2. 下一步提款 500 元, 確認帳戶總金額為 600 元
    def test_1B(self):
        self.test_user.withdraw(500)
        assert (self.test_user.balance == 600)

# 3. 假設銀行年利率是10%, 經過一年之後確認帳戶餘額為660元
    def test_1C(self):
        CustomerDataProcess().add_interest(self.test_user, 0.1)
        assert (int(self.test_user.balance) == 660)

# 4.之後提款 700 元, pytest 預期會接到 RuntimeError
    def test_1D(self):
        with pytest.raises(SystemExit):
            self.test_user.withdraw(700)

# 第二題
#1.
    def test_2A(self):
        response = requests.get('https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/user_info?userid=A123456789')
        # 伺服器回應的狀態碼
        assert response.status_code == 200
#2.
    def test_2B(self):
        response = requests.get('https://cathay-ds-test.s3-ap-northeast-1.amazonaws.com/company_info?companyid=1')
        assert response.status_code == 403

##########################################################################################
