# Nexcoin

This project is a website built using Flask to showcase a simple banking system like adding coins to a user, transferring coins between users, and checking the balance of a user.

## Table of Contents

- [Getting Started](#getting-started)
- [Features](#features)
- [File Structure](#file-structure)
- [Usage](#usage)
- [Creating a NexCoin account](#creating-a-nexcoin-account)
- [Contributing](#contributing)
- [To Do](#to-do)
- [Credits](#credits)

# Getting Started

Before running the project, make sure you have Flask and Flask-CORS installed. You can install them using pip:
```
pip install Flask Flask-CORS
```

## Features

1. **User Management:** Add coins to users, transfer coins between users, and retrieve the coin balance of a user.
2. **Error Handling:** Custom error handlers are implemented for various error codes such as 404, 403, and 401.
3. **Data Storage:** User data like username, coins, and passcodes are stored in a simple text-based database `database.txt`.

## File Structure

- **app.py:** This file contains the Flask application and all the routes.
- **database.txt:** This is a simple text-based database to store user information.
- **templates/:** This directory contains all HTML templates used for rendering pages.

## URL Usage

1. **Home Route (`/`):** Takes an optional `user` parameter. If provided, the server fetches user details. Else, it renders the homepage.
2. **Add Coin Route (`/add_coin`):** Used to add a coin to the user's account. Requires `user` and `pass` parameters.
3. **Transfer Coins Route (`/transfer_coins`):** Allows for transferring coins between users. Requires `user` parameter and a JSON body with `receiver` and `coins` fields.
4. **Get Balance Route (`/get_balance`):** Fetches the balance of a user. Requires `user` and `pass` parameters.

## Starting The Application

Before running the project, make sure you have Flask and Flask-CORS installed. You can install them using pip:
```
pip install Flask Flask-CORS
```
To start the project, just start the python file. Then, once everything has loaded correctly, head [here](http://127.0.0.1:8080) to see your newly started website!

## Creating a NexCoin Account

For developers or administrators wanting to set up accounts in the `database.txt`, follow the guide below. This might be useful for initial setup or for administrative tasks.

### Adding Accounts to `database.txt`

1. **Open `database.txt`:** Access the `database.txt` file, which is the basic database for Nexcoin.

2. **Format the Entry:** Each account is represented as a single line in the `database.txt` file, following the format:

```
{username} - {coins} - {password}
```
Replace `{username}`, `{coins}`, and `{password}` with the appropriate values. For instance:
```
JohnDoe - 0 - Password123
```
This example creates an account for a user named "JohnDoe" with an initial balance of 0 coins and a password "Password123".

3. **Restart the Application:** If the Flask application is running, restart it to ensure it picks up the changes made to the `database.txt` file.

Note: Ensure that usernames are unique. Duplicate usernames might cause unexpected behavior. Always back up `database.txt` before making changes, especially in a production environment.

## Contributing

If you're interested in contributing, please follow these steps:

1. Fork the Replit project.
2. Make your changes.

## To-Do
- [X] Add Error Pages
- [ ] Add encryption to passwords in database

## Credits

- **Programmer:** Dark25 (Ruben Roy)
- **License:** MIT
- **Note:** Please keep this credit at the console message and please properly attribute it.

For any questions or feedback, feel free to contact the developer directly.
