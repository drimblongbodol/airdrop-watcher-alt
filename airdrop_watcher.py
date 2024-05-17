import requests
import time

ETHERSCAN_API_KEY = "YourApiKeyToken"
TX_LIMIT = 50

def fetch_erc20_transfers(address):
    url = (
        f"https://api.etherscan.io/api"
        f"?module=account&action=tokentx"
        f"&address={address}"
        f"&startblock=0&endblock=99999999"
        f"&sort=desc"
        f"&apikey={ETHERSCAN_API_KEY}"
    )
    response = requests.get(url)
    data = response.json()
    if data["status"] != "1":
        print("⚠️  API error:", data.get("message"))
        return []
    return data["result"][:TX_LIMIT]

def analyze_airdrops(transfers, target_address):
    target_address = target_address.lower()
    seen_tokens = set()
    print(f"\n🎯 Scanning last {TX_LIMIT} ERC-20 transfers to {target_address}...\n")

    for tx in transfers:
        if tx["to"].lower() != target_address:
            continue  # Only track inbound

        token_symbol = tx["tokenSymbol"]
        token_contract = tx["contractAddress"]
        amount = int(tx["value"]) / (10 ** int(tx["tokenDecimal"]))
        sender = tx["from"]
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(int(tx["timeStamp"])))

        if token_contract not in seen_tokens:
            print(f"🎁 New token received!")
            print(f"    Token: {token_symbol}")
            print(f"    From: {sender}")
            print(f"    Amount: {amount:.4f}")
            print(f"    Time: {timestamp}")
            print(f"    Contract: {token_contract}\n")
            seen_tokens.add(token_contract)

def main():
    address = input("Enter wallet address: ").strip()
    if not address.startswith("0x") or len(address) != 42:
        print("❌ Invalid Ethereum address.")
        return

    transfers = fetch_erc20_transfers(address)
    if transfers:
        analyze_airdrops(transfers, address)
    else:
        print("No token transfers found or API error.")

if __name__ == "__main__":
    main()
