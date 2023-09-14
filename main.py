# ========================================
# Programmer: Dark25 (Ruben Roy)
# License: Open-Source
# Note: Please keep this credit at the console message and please properly attribute it.
# ========================================

# this code will be fully documented and commented so new programmers can fully understand it

# import necessary libraries
from flask import Flask, request, render_template, abort, jsonify
from flask_cors import CORS

# initialize flask app and enable CORS
app = Flask(__name__)
CORS(app)

# function to read user details from the database (database.txt)
def read_database(user):
    # open the database file in read mode
    with open('database.txt', 'r') as file:
        for line in file.readlines():
            parts = line.split(' - ')
            # check if the username matches
            if parts[0] == user:
                if len(parts) == 3:
                    # return coins and passcode for the user
                    return int(parts[1]), parts[2].strip()
                else:
                    return int(parts[1]), None
    return 0, None

# function to update the coin count and/or passcode of a user
def write_coin(user, coins, passcode):
    data = []
    # read the current data
    with open('database.txt', 'r') as file:
        data = file.readlines()
        for i, line in enumerate(data):
            # find the user and update their details
            if line.split(' - ')[0] == user:
                data[i] = f'{user} - {coins} - {passcode}\n'
                break
        else:
            # if user doesn't exist, add a new entry
            data.append(f'{user} - {coins} - {passcode}\n')
    # write the updated data back to the database file
    with open('database.txt', 'w') as file:
        file.writelines(data)

# home route
@app.route('/')
def index():
    user = request.args.get('user')
    # if no user provided, render homepage
    if user is None:
        return render_template('homepage.html')
    passcode = request.args.get('pass')
    coins, stored_passcode = read_database(user)
    # handle various scenarios such as non-existing users or incorrect passcodes
    if coins == 0 and stored_passcode is None:
        abort(404)  # user account does not exist
    if not passcode:
        abort(403)  # passcode is required
    if passcode != stored_passcode:
        abort(401)  # incorrect passcode
    # render user's index page with their details
    return render_template('index.html', user=user, coins=coins)

# route to add a coin to the user's account
@app.route('/add_coin', methods=['POST'])
def add_coin():
    user = request.args.get('user')
    passcode = request.args.get('pass')
    coins, stored_passcode = read_database(user)

    # handle various scenarios related to passcode and user existence
    if not stored_passcode:
        abort(404, "User account does not exist")
    elif not passcode:
        abort(400, "Passcode is required")
    elif stored_passcode != passcode:
        abort(403, "Incorrect passcode")
    
    coins += 1  # increment coin count
    write_coin(user, coins, stored_passcode)  # save updated coin count

    return 'Success!', 200

# custom error handlers for different error codes
@app.errorhandler(404)
def user_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(403)
def passcode_required(e):
    return render_template('403.html'), 403

@app.errorhandler(401)
def incorrect_passcode(e):
    return render_template('401.html'), 401

# route to transfer coins from one user to another
@app.route('/transfer_coins', methods=['POST'])
def transfer_coins():
    data = request.get_json()
    sender = request.args.get('user')
    receiver = data.get('receiver')
    coins_to_transfer = int(data.get('coins', 0))

    # fetch details of both sender and receiver
    sender_coins, sender_passcode = read_database(sender)
    receiver_coins, receiver_passcode = read_database(receiver)

    # handle various scenarios related to user existence, balance, etc.
    if sender_coins == 0 and sender_passcode is None:
        return jsonify({'message': 'Sender account does not exist'}), 404
    if receiver_coins == 0 and receiver_passcode is None:
        return jsonify({'message': 'Receiver account does not exist'}), 404
    if sender_coins < coins_to_transfer:
        return jsonify({'message': 'Insufficient coins'}), 400
    if sender == receiver:
        return jsonify({'message': 'Sender and receiver accounts must be different'}), 400

    # perform the coin transfer and save updated balances
    sender_coins -= coins_to_transfer
    receiver_coins += coins_to_transfer

    write_coin(sender, sender_coins, sender_passcode)
    write_coin(receiver, receiver_coins, receiver_passcode)

    return jsonify({'message': 'Success!'}), 200

# route to fetch the balance of a user
@app.route('/get_balance')
def get_balance():
    user = request.args.get('user')
    passcode = request.args.get('pass')
    coins, stored_passcode = read_database(user)

    # handle various scenarios related to passcode and user existence
    if not stored_passcode:
        abort(404, "User account does not exist")
    elif not passcode:
        abort(400, "Passcode is required")
    elif stored_passcode != passcode:
        abort(403, "Incorrect passcode")

    return jsonify({'coins': coins}), 200

# function to display the programmer credit information
def display_credit():
    credit_info = {
        "Programmer": "Dark25 (Ruben Roy)",
        "License": "Open-Source",
        "Note": ("Please keep this credit at the console message and please properly attribute it.")
    }

    border_line = '-' * 50
    print(border_line)
    for key, value in credit_info.items():
        print(f"{key.ljust(15)}: {value}")
    print(border_line)

# main start
if __name__ == '__main__':
    display_credit()  # display the credit info
    app.run(host='0.0.0.0', port=8080)  # start the flask app
