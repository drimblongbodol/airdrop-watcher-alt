# Airdrop Watcher

This tool helps track **ERC-20 token transfers** to a given Ethereum wallet, useful for monitoring stealth airdrops.

## Features
- Fetches last 50 ERC-20 token transfers via [Etherscan API](https://etherscan.io/apis).
- Detects **new tokens** received by the wallet.
- Prints sender, amount, contract address, and timestamp.
- Simple CLI interface.

## Usage
1. Install requirements:
   ```bash
   pip install requests
