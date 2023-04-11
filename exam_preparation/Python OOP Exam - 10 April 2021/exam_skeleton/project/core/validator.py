class Validator:
    @staticmethod
    def validate_empty_string_raises_ve(string, message):
        if not string:
            raise ValueError(message)

    @staticmethod
    def validate_zero_negative_value_raises_ve(value, message):
        if value <= 0:
            raise ValueError(message)