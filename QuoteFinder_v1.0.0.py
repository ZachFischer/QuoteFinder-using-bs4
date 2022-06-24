from bs4 import BeautifulSoup
import requests
import re

def get_quotes(name, rawname, quote_lim):

        url = f"https://www.brainyquote.com/authors/{name}-quotes"

        result = requests.get(url)

        doc = BeautifulSoup(result.text, 'html.parser')

        quotes = doc.find_all(class_ = re.compile('b-qt qt_*'), limit=quote_lim)

        quote_list = [''] + [ (str(quote.get_text())).strip() for quote in quotes ] + ['-']

        if quote_list != ['', '-']: return quote_list
        else: return [f'\nSorry, could not find any quotes from "{rawname}". Try checking for spelling errors.\n-']
    
while True:

        while True:
                try:
                        user_input = str(input("Who do you want to see quotes from?\n>"))
                        if user_input == '': raise ValueError
                except ValueError: print("Please enter a valid name, with only letters!")
                else: break

        while True:
                try:
                        quote_num = int(input("How many quotes would you like to generate? (enter as integer) \n>"))     

                except ValueError: print("Please enter a whole number!")
                else: break

        inputted_name = '-'.join( (user_input).lower().split() )
        quote_list = get_quotes(inputted_name, user_input, quote_num)

        for i in quote_list: print(i)

