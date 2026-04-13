-- Drop tables if they exist to reset the database
DROP TABLE IF EXISTS Transactions;
DROP TABLE IF EXISTS Categories;
DROP TABLE IF EXISTS Accounts;
DROP TABLE IF EXISTS Users;

-- Create Users table
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);

-- Create Accounts table
CREATE TABLE Accounts (
    account_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    account_name TEXT NOT NULL,
    balance REAL DEFAULT 0.0,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Create Categories table
CREATE TABLE Categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Create Transactions table
CREATE TABLE Transactions (
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    transaction_date DATE NOT NULL,
    description TEXT,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id),
    FOREIGN KEY (category_id) REFERENCES Categories(category_id)
);

-- Populate Users
INSERT INTO Users (username, email) VALUES ('john_doe', 'john@example.com');
INSERT INTO Users (username, email) VALUES ('jane_smith', 'jane@example.com');

-- Populate Accounts
INSERT INTO Accounts (user_id, account_name, balance) VALUES (1, 'Checking Account', 1500.00);
INSERT INTO Accounts (user_id, account_name, balance) VALUES (1, 'Savings Account', 5000.00);
INSERT INTO Accounts (user_id, account_name, balance) VALUES (2, 'Business Account', 10000.00);

-- Populate Categories
INSERT INTO Categories (category_name, description) VALUES ('Income', 'Salary or other earnings');
INSERT INTO Categories (category_name, description) VALUES ('Expenses', 'Daily spending');
INSERT INTO Categories (category_name, description) VALUES ('Investments', 'Stock or asset purchases');
INSERT INTO Categories (category_name, description) VALUES ('Transfers', 'Internal transfers');

-- Populate Transactions
INSERT INTO Transactions (account_id, category_id, amount, transaction_date, description) VALUES (1, 1, 2000.00, '2025-09-01', 'Salary deposit');
INSERT INTO Transactions (account_id, category_id, amount, transaction_date, description) VALUES (1, 2, -500.00, '2025-09-05', 'Groceries');
INSERT INTO Transactions (account_id, category_id, amount, transaction_date, description) VALUES (2, 3, -1000.00, '2025-09-10', 'Stock purchase');
INSERT INTO Transactions (account_id, category_id, amount, transaction_date, description) VALUES (3, 1, 5000.00, '2025-09-15', 'Client payment');
INSERT INTO Transactions (account_id, category_id, amount, transaction_date, description) VALUES (1, 4, -200.00, '2025-09-20', 'Transfer to savings');
INSERT INTO Transactions (account_id, category_id, amount, transaction_date, description) VALUES (2, 4, 200.00, '2025-09-20', 'Transfer from checking');