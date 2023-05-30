# Random_Crypto_Wallet_Seed_Phrase_Generator
A python program designed to generate a random 12-word seed phrase for the recovery of a crypto wallet.

This Python code generates random seed phrases for your wallet. It reads a wordlist from a file called wordlist.txt and categorizes the words based on their lengths. It then selects random words from each category to create a random seed phrase.

># Prerequisites
Before running the code, make sure you have the following:
* Python (version 3 or above) installed on your machine.
* A file named wordlist.txt containing a list of words, with each word on a separate line.

# Usage
* Place the wordlist.txt file in the same directory as the Python script.
* Run the Python script.

The script will generate a random seed phrase consisting of 12 words, with the words selected from different categories based on their lengths. The selected words will be displayed on the console.

>Note: Uncommenting the commented lines in the code will print additional information such as the number of words in each category.


Feel free to modify the code and adjust the word lengths or the number of words in the seed phrase according to your requirements.
# Example Output:

    > Random seed phrases for your wallet :
    ['abacus', 'canoed', 'musings', 'scribing', 'flit', 'crank', 'refuel', 'tory', 'feral', 'vintage', 'caverns', 'altars']

Remember to keep your seed phrase secure as it is crucial for wallet recovery and should not be shared with anyone.

>Disclaimer: This code is provided as a sample and should not be used for generating real seed phrases for wallets that hold valuable assets. It is recommended to use well-tested and trusted libraries or >tools specifically designed for seed phrase generation and wallet management.
