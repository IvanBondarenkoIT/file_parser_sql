import re

VALIDATION_PATTERNS = {
    "First Name": r'[A-Za-z]+',
    "Last Name": r'[A-Za-z]+',
    "SSN": r'\d{3}-?\d{2}-?\d{4}',
    "Address": r'.+',
    "Company": r'.+',
    "Department": r'.+',
    "Position": r'.+',
    "Zip": r'\d{2,5}-?(\d{4})?',
    "Mobile number": r'\d?-?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}',
}
"""`userid`, `name`, `username`, `password`, `email`, `permission`, `mobile`,  `sex`, `country`, `birth`"""


class DataInterpreter:
    def __init__(self):
        #("userid", "name", "username", "password", "email", "permission", "mobile",  "sex", "country", "birth")
        self.__result_dict = []
        self.__current_row = None
        self.__not_valid_data = []

    def add_data(self, data):
        if re.match(pattern=r"VALUES", string=str(data)):
            all_matches = re.findall(r"\(\d{2,5},\s.+\)", f"{str(data)}"[7:], re.IGNORECASE)
            for match in all_matches:
                self.add_row(match.split(","))
        """
        (29,	'mike',	'bigmoneyptc',	'34abf7b0443c1beca99d6e1053885d73',	'awesomeking2005@yahoo.com',	0,	'',	'United States',	0),,
        (30,	'Mark Crocker',	'exclusive',	'633db5c7f7ad9f2aaf3b75e06703984a',	'marka316@gmail.com',	0,	'',	'United States',	0),,
        (31,	'ted',	'tedbundy',	'7c46585a5fbb5084c8e3a6ff619c9131',	'sales@adswu.com',	0,	'',	'United States',	0),,
        """

    def add_row(self, data):
        print(data)
        for row in data:
            """name, date, nationality, address, tel, email"""
            self.__result_dict.append((self.validate(value=row[0], kay="name"),
                                       self.validate(value=row[1], kay="dob"),
                                       self.validate(value=row[2], kay="user_additional_info"),
                                       self.validate(value=row[3], kay="address"),
                                       self.validate(value=row[4], kay="tel"),
                                       self.validate(value=row[5], kay="usermail"),
                                       ))

    def validate(self, value, kay):
        """Return valid values or empty string"""
        if re.match(pattern=VALIDATION_PATTERNS.get(kay), string=str(value)):
            return value
        else:
            self.__not_valid_data.append(f"{kay}: {value}")
            return ""

    @property
    def get_final_values(self):
        return self.__result_dict

    @property
    def get_not_valid_data(self):
        return self.__not_valid_data
