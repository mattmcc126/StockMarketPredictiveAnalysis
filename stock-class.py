"""

-Some psuedocode and  to get an initial idea of 
how I want my stock data class to be set up

-This is only class implementation of the individual stocks and
their functions

-Algorithims pretaining to strategic trading will not be contained here

---------------------------------------------------------------------------------

Additional considerations for implementation:

Type Hinting
 - add type hints for readability
 - will prob be helpful for debugging

Date Handling
 - use datetime objs for good handing 
 - will prevent problems with string dates being incorrect

Data validation
 - should use data validation inside the add stock function
 - this will prevent NAN or unreal/incorrect values from being updated/passed

Other functions
 - remove stock function?
 - get latest price function?
 - get price range function?

Naming tuples for better readability?

Error handling
 - create some custom exceptions for error handling
 - USE THIS, extremely good practice, not everything runs perfectly always

"""

# Import date/time? Will this be useful?

# Class : Stock data
    
    # Constructor for class
        # def "__init__(self):"
        # self to refer to instance being created

        # Initialize a dictionary attribue for the individual stock
        # self.stocks = {} || self.stocks = dict[...]
        # Stock symbols will be keys with data as the vals

    # Add stock function
        # def add_stock(self, symbol, data)
        # data will be a list of tuples
        # data could be something like below:
            # (date, open, high, low, close, volume)
        # this function should either add or update stock data
        # maybe make a different function for updating for simplicity
        # this will act as the setter method for this class

    # Get stock data function
        # def get_stock_data(self, symbol, start_date, end_date)
        # Retrieve stock data from a given symbol and date range
        # will probabaly have more parameters as I develop more
        # good function to def implement error handling
        # this function will be the first returning values function
        # returns all data to a given function in the params between two dates

    # print symbols function?
    # other possible functions mentioned above
        

