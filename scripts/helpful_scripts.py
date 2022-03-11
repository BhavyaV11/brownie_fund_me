from brownie import network, accounts, config, MockV3Aggregator
from web3 import Web3

decimals = 8
starting_price = 200000000000

forked_mainnet_env = ["mainnet-fork-dev", "mainnet-fork"]
local_blockchain_env = ["development", "ganache-local"]


def get_account():
    if (
        network.show_active() in local_blockchain_env
        or network.show_active() in forked_mainnet_env
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(decimals, starting_price, {"from": get_account()})
    print("Mocks Deployed")
