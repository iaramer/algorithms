"""
Back to card numbers
Card number may have from 12 to 19 digits, usually they have 16. You have list of card numbers. For each card number
print its issuer (like Visa or Mastercard).

You can create dict-helper and fill it using this table:
https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN)

To test your code, generate card numbers randomly ("random" package's docs will help you) and run checks for them.
"""

import requests

binlist_url = "https://lookup.binlist.net/"


def find_card(iin):
    """
    Takes in IIN number, and returns the issuer using the binlist.net API
    Input: IIN number, int or string
    Output: credit card issuer
    """

    iin = str(iin)

    response = requests.get(binlist_url + iin)

    # Check for a 404 status code
    if response.status_code == 404:
        return 'Not found'

    return response.json()


def identify_card_issuer(card_num):
    """
    Determines the card issuer using an IIN database
    Input: Card number, int or string
    Output: Card issuer information, dictionary (spec by binlist.net)
    """
    card_num = str(card_num)

    # IIN on the credit card being searched
    card_iin = card_num[:6]

    return find_card(card_iin).get('scheme')


if __name__ == '__main__':
    print(identify_card_issuer('4571652041253210'))
