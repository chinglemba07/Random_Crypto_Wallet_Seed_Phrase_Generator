# Random_Crypto_Wallet_Seed_Phrase_Generator
A python program designed to generate a random 12-word seed phrase for the recovery of a crypto wallet.

This Python program generates a random 12-word seed phrase that can be used for recovering a crypto wallet. 
A seed phrase, also known as a mnemonic phrase, is a series of words that serves as a human-readable representation of a cryptographic key.
It acts as a backup for your wallet, allowing you to regain access to your funds in case of loss, theft, or device failure.

The program reads from a wordlist file (wordlist.txt) that contains a collection of words based on the BIP39 standard, 
ensuring compatibility with popular crypto wallets. It categorizes the words into four groups based on their length: 4, 5, 6, and 7 characters.

The program selects random words from each group to create a unique seed phrase. 
To ensure that no word is repeated within the seed phrase, 
the program keeps track of previously selected words for each word length category.

After generating the seed phrase, the program displays it on the console. 
It is crucial to immediately store the seed phrase in a secure location, 
such as a hardware wallet, offline storage, or a physical backup. 
Safeguarding the seed phrase is vital to prevent unauthorized access to your funds.

# Please note the following:

This program does not store or transmit any sensitive information. 
The responsibility lies with the user to handle and store the seed phrase securely.
To enhance security, it is recommended to run this program on an offline machine that is not connected to the internet.
It is advisable to review and verify the wordlist used in the program, 
ensuring it aligns with the BIP39 standard and includes appropriate and commonly accepted words.
This program is provided as-is without any warranties. Use it at your own risk.

# Requirements:

Python 3.x

# Usage:

> Ensure the wordlist file (wordlist.txt) is in the same directory as the Python program.
> Run the program in Python.
> The program will generate a random 12-word seed phrase and display it on the console.
> Immediately record and securely store the seed phrase in multiple locations.
> Avoid sharing the seed phrase with anyone and keep it offline to prevent unauthorized access to your wallet.
