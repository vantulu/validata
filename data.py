
from datetime import datetime
from dateutil import parser
from typing import Union

def cleanse(assignment: Union[str, dict], extract: str) -> str:

    """
    Takes an assignment (either a string or dictionary) and reformats the key or string extracting a list of characters in a single string given in the function.
    """

    if type(assignment) == str:

        result = "".join([char for char in assignment if char not in extract])
        return result

    elif type(assignment) == dict:

        new_dict = {}

        for key, value in assignment.items():

            new_key = "".join([char for char in key if char not in extract])
            new_dict[new_key] = value

        return new_dict

    else: 

        raise TypeError(f'variable assignment required string or dictionary: was given {type(assignment)}')

def reformat(assignment: Union[str, dict], object: str, format: str) -> str:

    """
    Reformats a given string based on input arguments.
    Arguments: date, temperature
    """

    if type(assignment) == str:

        if object == 'date':

            date = datetime.strptime(assignment, format)
            formatted_date = date.strftime(format)
            return formatted_date

        elif object == 'temperature':

            if format == 'metric':

                metric_obj = (int(assignment) - 32) * 5/9
                return str(round(metric_obj))
            
            elif format == 'imperial':

                imperial_obj = (int(assignment) * 9/5) + 32
                return str(round(imperial_obj))

    elif type(assignment) == dict:

        if object == 'date':

            formatted_dict = {}

            for key, value in assignment.items():
                
                try:
                    
                    date_obj = parser.parse(key)    
                    formatted_date = date_obj.strftime(format)
                    formatted_dict[formatted_date] = value

                except ValueError:

                    print(f"unable to parse the date '{key}'")
                    continue

            return formatted_dict

        elif object == 'temperature':

            if format == 'metric':

                formatted_dict = {}
    
                for key in assignment:
                    
                    fahrenheit = (assignment[key] * 9/5) + 32
                    celsius = assignment[key]
                    
                    formatted_dict[key] = {

                        'Fahrenheit': fahrenheit,
                        'Celsius': celsius

                    }
                
                return formatted_dict

# types: temperatures
# time format: "%Y-%m-%d"

reformat('')
