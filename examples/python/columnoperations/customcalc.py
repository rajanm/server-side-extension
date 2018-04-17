from forex_python.converter import CurrencyRates
import logging
import logging.config
import csv
import os
import sqlite3

class customcalc:

    c = CurrencyRates()
    # Get a key for forex_python after June 2018 due to changes in fixer.io.
    usd_to_inr_rate = c.get_rate('USD', 'INR')
    usd_to_gbp_rate = c.get_rate('USD', 'GBP')
    user_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'users.csv')

    def __init__(self):
        ''' Constructor for this class. '''
    os.makedirs('logs', exist_ok=True)
    log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logger.config')
    logging.config.fileConfig(log_file)
    logging.info('Custom Calc Logging enabled')

    @staticmethod
    def multiply(numbers):
        total = 1
        for x in numbers:
            total *= x
        return total

    @staticmethod
    def multiplyrows(numbers):
        total = 0
        # numbers[0] corresponds to col1 passed to SSE
        # numbers[1] corresponds to col2 passed to SSE
        total = numbers[0] * numbers[1]
        return total

    @staticmethod
    def convertusdtoinr(numbers):
        total = 0
        # numbers[0] corresponds to col1 passed to SSE
        total = numbers[0] * customcalc.usd_to_inr_rate
        return total

    @staticmethod
    def convertusdtogbp(strings,numbers):
        logging.info('userid passed to convertusdtogbp method {}'.format(strings))
        total = 0

        readFile = open(customcalc.user_file, 'r')

        # Set up CSV reader and process the header
        csvReader = csv.reader(readFile)
        header = next(csvReader)
        userIdIndex = header.index("userid")
        userRoleIndex = header.index("userrole")

        # sample logic
        # Qlik Sense Desktop passes Persona\Me when built in function OSUser() is used
        # Qlik Sense Enterprise passes domain user ID when built in function OSUser() is used
        # Below logic is used for testing in Qlik Sense Desktop
        # Loop through the lines in the file and get each user detail
        for row in csvReader:
            userId = row[userIdIndex]
            userRole = row[userRoleIndex]
            if userId == strings:
                total = numbers * customcalc.usd_to_gbp_rate
        return total

    @staticmethod
    def getuserrole(strings):
        logging.info('userid passed to getuserrole method {}'.format(strings))
        returnRole = 'Unknown User Role'

        readFile = open(customcalc.user_file, 'r')

        # Set up CSV reader and process the header
        csvReader = csv.reader(readFile)
        header = next(csvReader)
        userIdIndex = header.index("userid")
        userRoleIndex = header.index("userrole")

        # sample logic
        # Qlik Sense Desktop passes Persona\Me when built in function OSUser() is used
        # Qlik Sense Enterprise passes domain user ID when built in function OSUser() is used
        # Below logic is used for testing in Qlik Sense Desktop
        # Loop through the lines in the file and get each user detail
        for row in csvReader:
            userId = row[userIdIndex]
            userRole = row[userRoleIndex]
            if userId == strings:
                returnRole =  userRole
                break
        return returnRole

    @staticmethod
    def getresults(query):
        logging.info('query passed to getresults method {}'.format(query))
        conn = sqlite3.connect('customer.db')
        logging.info('Opened database successfully')

        cursor = conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()

        logging.info('results from getresults method {}'.format(rows))
        logging.info('Operation done successfully')
        conn.close()

        return rows
