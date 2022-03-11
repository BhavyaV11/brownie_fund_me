from brownie import accounts, network, FundMe, config, MockV3Aggregator
from scripts.helpful_scripts import deploy_mocks, get_account, local_blockchain_env


def deploy_fund_me():
    if network.show_active() not in local_blockchain_env:
        price_feed_add = config["networks"][network.show_active()]["eth_usd_price_feed"]
        publish_flag = False
    else:
        deploy_mocks()
        price_feed_add = MockV3Aggregator[-1].address
        publish_flag = False

    fund_me = FundMe.deploy(
        price_feed_add,
        {"from": get_account()},
        publish_source=publish_flag,
    )
    print(f"Contract deployed at {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
