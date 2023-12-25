# NexCoin

This project is a website built using Flask to showcase a simple banking system like adding coins to a user, transferring coins between users, and checking the balance of a user.

## Table of Contents

- [Getting Started](#getting-started)
- [Features](#features)
- [Usage](#usage)
- [Creating a NexCoin account](#creating-a-nexcoin-account)
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

## Usage

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

## Credits

- **Programmer:** Dark25 (Ruben Roy)

For any questions or feedback, feel free to contact the developer directly.

## License

NexCoin is open-source and is under the GNU GPL v3.0 License. See the [LICENSE](LICENSE) for more information.
