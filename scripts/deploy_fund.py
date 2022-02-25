from brownie import Pay, accounts, network, config
from web3 import Web3

amount = 1000000000000000000
index = None


def pay():
    account1 = get_account(index=0)
    pay = Pay.deploy({"from": account1})
    account2 = get_account(index=1)
    account3 = get_account(index=2)
    txn = pay.SendEth(Web3.toWei(0.1, "ether"), {"from": account1})
    print("Funding...")
    txn.wait(1)
    print("Funded!")
    txn = pay.SendEth(Web3.toWei(0.1, "ether"), {"from": account2})
    print("Funding...")
    txn.wait(1)
    print("Funded!")
    txn = pay.SendEth(Web3.toWei(0.2, "ether"), {"from": account3})
    print("Funding...")
    txn.wait(1)
    print("Funded!")
    txn = pay.HighestBidder({"from": account1})
    txn.wait(1)
    print(f"This is the highest funder! => {pay.highestFunder()}")


def get_account(index=None):
    if index:
        return accounts[index]
    else:
        return accounts.add(config["wallets"]["from_key" + str(index)])


def main():
    pay()
