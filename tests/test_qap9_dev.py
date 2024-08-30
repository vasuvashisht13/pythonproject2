# test_parabank.py
from pylenium.driver import Pylenium


from pylenium.driver import Pylenium

def test_login(py: Pylenium):
    # Visit the Parabank website
    py.visit('https://parabank.parasoft.com/parabank/index.htm')

    # Perform login
    py.get('input[name="username"]').type('vasu')
    py.get('input[name="password"]').type('Fin@555666111')
    py.get('input[value="Log In"]').click()

    # Wait for the element to contain the expected text
    py.get('div#leftPanel').should(lambda el: 'Accounts Overview' in el.text())


#
# def test_account_summary(py: Pylenium):
#     # Visit the account summary page
#     py.visit('https://parabank.parasoft.com/parabank/overview.htm')
#
#     # Wait for the account summary table to appear and assert it contains "Account Summary"
#     py.get('table#accountTable').should(lambda el: 'Account Summary' in el.text())
#
#
# def test_transfer_funds(py: Pylenium):
#     # Visit the transfer funds page
#     py.visit('https://parabank.parasoft.com/parabank/transfer.htm')
#
#     # Perform fund transfer
#     py.get('input[name="amount"]').type('100')
#     py.get('select[name="fromAccount"]').select('12345')  # Example account number
#     py.get('select[name="toAccount"]').select('67890')    # Example account number
#     py.get('input[value="Transfer"]').click()
#
#     # Assert successful transfer by checking the confirmation message
#     py.get('div#transactionResults').should(lambda el: 'Transfer Complete!' in el.text())


# # test_cases.py
# def test_account_summary(logged_in_pylenium: Pylenium):
#     # Visit the account summary page
#     logged_in_pylenium.visit('https://parabank.parasoft.com/parabank/overview.htm')
#
#     # Wait for the account summary table to appear and assert it contains "Account Summary"
#     logged_in_pylenium.get('table#accountTable').should(lambda el: 'Account Summary' in el.text())
#
# def test_transfer_funds(logged_in_pylenium: Pylenium):
#     # Visit the transfer funds page
#     logged_in_pylenium.visit('https://parabank.parasoft.com/parabank/transfer.htm')
#
#     # Perform fund transfer
#     logged_in_pylenium.get('input[name="amount"]').type('100')
#     logged_in_pylenium.get('select[name="fromAccount"]').select('12345')  # Example account number
#     logged_in_pylenium.get('select[name="toAccount"]').select('67890')    # Example account number
#     logged_in_pylenium.get('input[value="Transfer"]').click()
#
#     # Assert successful transfer by checking the confirmation message
#     logged_in_pylenium.get('div#transactionResults').should(lambda el: 'Transfer Complete!' in el.text())



def test_account_summary(logged_in_pylenium: Pylenium):
    # Visit the account summary page
    logged_in_pylenium.visit('https://parabank.parasoft.com/parabank/overview.htm')

    # Wait for the account summary table to be visible and assert it contains "Account Summary"
    logged_in_pylenium.get('table#accountTable', timeout=10).should(lambda el: 'Account Summary' in el.text())


def test_transfer_funds(logged_in_pylenium: Pylenium):
    # Visit the transfer funds page
    logged_in_pylenium.visit('https://parabank.parasoft.com/parabank/transfer.htm')

    # Wait for the transfer form elements to be visible
    py = logged_in_pylenium
    py.get('input[name="amount"]', timeout=10).should_be_visible()
    py.get('select[name="fromAccount"]', timeout=10).should_be_visible()
    py.get('select[name="toAccount"]', timeout=10).should_be_visible()

    # Perform fund transfer
    py.get('input[name="amount"]').type('100')
    py.get('select[name="fromAccount"]').select('12345')  # Example account number
    py.get('select[name="toAccount"]').select('67890')  # Example account number
    py.get('input[value="Transfer"]').click()

    # Assert successful transfer by checking the confirmation message
    py.get('div#transactionResults', timeout=10).should(lambda el: 'Transfer Complete!' in el.text())
