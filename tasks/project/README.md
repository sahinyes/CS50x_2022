
# cs50 Final
#### Video Demo:  https://youtu.be/bjUrVMhJPCw

## Description
This was my final project for Harvard CS50. I upgraded the finance application, which was
in the previous assignment, with additional features.For example, when the application is run, it will prepare graphics for the users at certain time intervals in the background. The admin also check the current account status of the users from the panel or can view the general stock status in the accounts graphically. I have briefly explained all the added features below.

## Features
#### On the user side:
- Register: Any person can register to make a new account. Previously taken usernames cannot be register.
- Quote: Users can quote a price for stocks. Not valid stocks names will redirect you to `apology` page.
- Buy: Users can buy shares with current prices.
- Sell: Users can sell their stocks at the current price.
- History: Users can view all histories.
- Send Money: Users can send money to other users. It will print the sent amount and current balance on the screen
- Add Money: Users can add money to themselves. There is no limit.
- User Panel: Users can change their own password on the panel. The two new passwords entered must be the same. After successful change, it will automatically logout for new login.
- Exchange Market: They can follow live stock market movements. There are 4 graphics about stocks prices. They will refresh automatically around 1-2 min. Don't forget to refresh the page.

#### On the admin side:

- Admin Panel: Admin panel consists of 4 parts. These are Register, set money and delete boxes. This allows you quickly manage all processes from a single window. 4th part is "user table". This table allows you to overview the changes you have made at all times.
- Interactions: Admin can monitor all purchasing transactions. So admin can detect also abnormal conditions in this page.
- Statistics: Presents graphs showing which shares and how much in general user account. So that the admin can have an idea about the general financial situation. Graphics can be export also to use elsewhere.

## Installation
1. Clone the code.
1. Run the command `pip install -r requirements.txt` in the app directory.
2. Export your api key from `iexcloud.io` (for register: [iex cloud](https://iexcloud.io/cloud-login#/register)) (You cannot run this application without an api key)
3. Run command `flask run` on cli in the app directory.
4. Go to this page in your browser `http://127.0.0.1:5000/` (by default this)
4. Default credentials `admin:admin`


## Overviews
