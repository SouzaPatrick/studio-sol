from flask import Flask, request, jsonify

from validate_password import (
    validate_min_special_chars,
    validate_min_size,
    validate_no_repeted,
    validate_min_digit,
    validate_min_low_case,
    validate_min_upper_case
)

app = Flask(__name__)


@app.route("/verify", methods=['POST'])
def verify():
    # Extract request data
    data: dict = request.get_json()

    password: str = data.get('password')
    rules: dict = data.get('rules')

    # Validate extracted data
    no_match: list = []
    for rule in rules:
        match rule.get('rule'):
            case 'minSize':
                if not validate_min_size(value=rule.get('value'), password=password):
                    no_match.append('minSize')
            case 'minSpecialChars':
                if not validate_min_special_chars(value=rule.get('value'), password=password):
                    no_match.append('minSpecialChars')
            case 'noRepeted':
                if not validate_no_repeted(password=password):
                    no_match.append('noRepeted')
            case 'minDigit':
                if not validate_min_digit(value=rule.get('value'), password=password):
                    no_match.append('minDigit')
            case 'minUppercase':
                if not validate_min_upper_case(value=rule.get('value'), password=password):
                    no_match.append('minUppercase')
            case 'minLowercase':
                if not validate_min_low_case(value=rule.get('value'), password=password):
                    no_match.append('minLowercase')

    return jsonify({
        "verify": False if no_match else True,
        "noMatch": no_match
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
