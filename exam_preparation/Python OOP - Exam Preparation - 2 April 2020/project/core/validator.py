class Validator:
    @staticmethod
    def check_if_negative_value(value, message):
        if value < 0:
            raise ValueError(message)

    @staticmethod
    def check_if_empty_string(value, message):
        if not value:
            raise ValueError(message)