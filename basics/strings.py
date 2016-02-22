#!/usr/bin/python
#  -*- coding: utf-8 -*-
# Python Version: 2.7
#Sandbox for string package

import string
from datetime import datetime


def main():
    current_date = datetime.now()
    #use curly braces with ':' as first symbol
    str_ = 'Current date is {:%d.%m.%Y}, time is {:%H:%M:%S}'
    #put one argument twice
    #output current date and time
    print str_.format(current_date, current_date)

    #format numbers with comma
    numbers = int(string.digits)
    print '{:,}'.format(numbers)

    #format numbers with percentage with different decimal places
    points = 17
    total = 30
    print 'Correct answers percentage: {:.2%}'.format(points/float(total))
    print 'Correct answers percentage: {:.4%}'.format(points/float(total))

    #just simple template for some letter
    #mix of named and string arguments
    letter_text = 'Mr{!s}.{!s}, we\'re hope that you enjoyed your vacations at our hotel in {month_name}, {year_name}'
    print letter_text.format('s', 'Smith', month_name='March', year_name='2015')
    print letter_text.format('', 'Brown', month_name='January', year_name='2016')

    #centered string with A LOT of stars :D
    print '{:*^45}'.format('CONGRATULATIONS!')

    #another template
    temp = string.Template('Hello, $some_name!')
    print temp.substitute(some_name='John')

    #right use of $ symbol
    temp = string.Template('Our new $product_name just today for $$9.99!')
    print temp.substitute(product_name='soap')

    #And.. power of named arguments!
    temp = string.Template('Dear $name, I heard that you got $points_count points in your exam.\n'
                           'Congratulations and best wishes from your aunt $sender')
    print temp.substitute(sender='Mary', name='Kate', points_count=87)

    lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit'
    #capitalize each word in the string
    print string.capwords(lorem)

    #and well-known, the lovely one 'join'
    array_of_words = ["Hello,", "f*ing", "mad,", "but", "beautiful", "world!"]
    print string.join(array_of_words, sep=' ')

    #one more well-known, returns a list of words
    print lorem.split()

    #and without comma
    print lorem.replace(',', '').split()

    #one more old friend
    # index() raise ValueError if not found
    position = lorem.find('amet')
    print 'Position of substring "{!s}" is {:d}'.format('amet', position)


if __name__ == "__main__":
    main()