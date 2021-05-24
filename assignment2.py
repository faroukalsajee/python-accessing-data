import re


def get_data(text_file):
    """Opening the listings.txt file and get rows from it and save it in text variable."""
    with open(text_file, 'r') as f:  # opening file using with will automatically close it
        text = f.readlines()  # reading lines and storing them in text as list
        text = [x.rstrip() for x in text]  # striping \n the new line string from right of the sentences
    return text


text = get_data("listings.txt")  # getting lines


def get_listing(MLS):
    """Writing dictionary in report file and choose the row with MLS variable"""
    w = open("report.txt", "a")  # opening file
    listing_tuple = (
        "MLS", "address", "price", "bedrooms", "bathrooms", "property_type", "active_listing_days")  # making the tuple
    res = dict()  # initializing the dictionary
    for row in text:  # looping through lines
        data = re.split(",(?! )", row)  # spliting the line using comma and not followed by space
        if len(data) != len(listing_tuple):  # if lengths don't match
            w.write("This Row Have additional comma")  # then must be an additional comma in the line
            w.write("\n")  # new line
        if data[0] == MLS:  # Checking to match MLS
            for i, n in enumerate(listing_tuple):  # enumerate is returing the index and the element of the list
                res[n] = data[i]  # mapping the key of the dictionary with the value of the data is the order of data is
                # the same in lines and lisitng tuple MLS is the first element and in the lines the value of MLS
            break
    w.write("***Details of the MLS {} are:  ".format(MLS))
    w.write("\n")
    w.write(str(res))  # making the dictionary as string to be written.
    w.write("\n")
    w.close()


def search_by_city_and_bedroom_number(city_name, number_of_bedroom):
    """Writing Rows which have n bedrooms or more and in m city."""
    w = open("report.txt", "a")
    res = ""
    w.write("***Listings of properties in {} and has {} bedrooms".format(city_name, number_of_bedroom))
    w.write("\n")
    for row in text:
        data = re.split(',(?! )', row)
        try:
            if int(data[3]) >= number_of_bedroom and city_name in data[
                1]:  # checking if the fourth value of data aka number of bedrooms and the city name is matching the
                # input
                res = row
                w.write(res)
                w.write("\n")
        except:
            continue
    w.close()


def search_by_price_range(min_price, max_price):
    """Writing Rows which its price between minimum and maximum price inclusive."""
    w = open("report.txt", "a")
    res = ""
    w.write("***Listings of properties with price between {} and {} ".format(min_price, max_price))
    w.write("\n")
    for row in text:
        data = re.split(',(?! )', row)
        try:
            if int(data[2]) >= min_price and int(
                    data[2]) <= max_price:  # checking if the price in the inclusive range of [min_price,max_price]
                res = row
                w.write(res)
                w.write("\n")
        except:
            continue
    w.close()


def search_by_city_and_property_type(city_name, property_type):
    """Writing Rows which hace specific city name and property type."""
    w = open("report.txt", "a")
    res = ""
    w.write("***Listings of {} in {} ".format(property_type, city_name))
    w.write("\n")
    for row in text:
        data = re.split(',(?! )', row)
        try:
            if property_type in data[5] and city_name in data[
                1]:  # checking type and city name similar to search_by_city_and_bedroom_number function
                res = row
                w.write(res)
                w.write("\n")
        except:
            continue

    w.close()


def reduce_price():
    """Reducing price of data by 10000 that have 30 or more active days."""
    w = open("report.txt", "a")
    res = ""
    w.write("***Listings of properties with reduced prices ")
    w.write("\n")
    for row in text:
        data = re.split(',(?! )', row)
        try:
            if int(data[-1]) >= 30:  # if the active days is greater than or equal 30
                data[2] = str(int(data[
                                      2]) - 10000)  # reducing from the price 10000 , converting the price to int and returning it to string to be written in the file
                res = ",".join(
                    data)  # as we want the connected line not a list contating strings so joining the splitted row after modification
                w.write(res)
                w.write("\n")
        except:
            continue
    w.close()


def search_by_postal_code_range(starting_character, ending_number):
    """Searching by first letter of postal code and the ending number must be between input and 9."""
    w = open("report.txt", "a")
    w.write(" ***Listings that have a postal code that starts with {} and ends with {} or more : ".format(
        starting_character, ending_number))
    w.write("\n")
    for row in text:
        data = re.split(',(?! )', row)
        pattern = "{}".format(starting_character) + '[0-9]' + '[a-zA-Z0-9] [a-zA-Z0-9][a-zA-Z0-9]' + '[{}'.format(
            ending_number) + '-9]'  # here is tricky. we want the regex to be as follows if the start is V and the end is 5: V[0-9][a-zA-Z0-9] [a-zA-Z0-9][a-zA-Z0-9][5-9] so we splitted the regex into strings and used format method to replace the 5 and v to make them variables reacting to the input of the function
        res = re.search(pattern, data[1])
        if res:
            w.write(row)
            w.write("\n")
    w.close()

