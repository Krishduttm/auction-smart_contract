from brownie import Auction, accounts, config, network
import brownie
from web3 import Web3
import time

myAwesomeGasLimit = 50000


def deploy_Auction():
    account1 = get_account(0)
    auction = Auction.deploy({"from": account1})
    account2 = get_account(1)
    account3 = get_account(2)
    txn = auction.start({"from": account1})
    txn.wait(1)
    # txn = auction.pay(Web3.toWei(1, "ether"), {"from": account1})
    # print("Bidding...")
    # txn.wait(1)
    # print("Bidding done!")
    val1 = Web3.toWei(0.01, "ether")
    txn = auction.pay({"from": account2, "value": val1})
    print("Bidding...")
    txn.wait(1)
    print("Bidding done!")
    # time.sleep(20)
    val2 = Web3.toWei(0.02, "ether")
    txn = auction.pay({"from": account3, "value": val2})

    print("Bidding...")
    txn.wait(1)
    print("Bidding done!")
    time.sleep(10)
    txn = auction.HighestBidder({"from": account1})
    print(f"This is the highest funder! => {auction.highestFunder()}")
    txn = auction.withdraw({"from": account1})
    txn.wait(1)
    print("Bids successfully transferred!")


def get_account(_index=None):
    if network.show_active() == "development":
        return accounts[_index]
    else:
        return accounts.add(config["wallets"]["from_key" + str(_index)])


def main():
    deploy_Auction()
