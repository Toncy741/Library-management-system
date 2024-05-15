-- Create the database
CREATE DATABASE library;

-- Use the library database
USE library;

-- Create the Branch table
CREATE TABLE Branch (
    Branch_no INT PRIMARY KEY,
    Manager_Id INT,
    Branch_address VARCHAR(50),
    Contact_no VARCHAR(50)
);
INSERT INTO Branch (Branch_no, Manager_Id, Branch_address, Contact_no)
VALUES
(1, 101, '42 MG Road, Ernakulam, Kerala', '0484123456'),
(2, 102, '15 Convent Road, Thrissur, Kerala', '0487654321'),
(3, 103, '27 Chittoor Road, Kochi, Kerala', '0484987654'),
(4, 104, '108 NH Bypass, Kozhikode, Kerala', '0495321456'),
(5, 105, '69 Bund Road, Thiruvananthapuram, Kerala', '0471654987'),
(6, 106, '31 Mahatma Gandhi Road, Kollam, Kerala', '0474123789'),
(7, 107, '18 Mission Quarters Road, Kottayam, Kerala', '0481456123'),
(8, 108, '56 Marine Drive, Alappuzha, Kerala', '0477789456'),
(9, 109, '83 Kaloor-Kadavanthra Road, Ernakulam, Kerala', '0484123789'),
(10, 110, '24 Baker Road, Pathanamthitta, Kerala', '0468456123');

-- Create the Employee table
CREATE TABLE Employee (
    Emp_Id INT PRIMARY KEY,
    Emp_name VARCHAR(50),
    Position VARCHAR(30),
    Salary int,
    Branch_no INT,
    FOREIGN KEY (Branch_no) REFERENCES Branch(Branch_no)
);
INSERT INTO Employee (Emp_Id, Emp_name, Position, Salary, Branch_no)
VALUES
 (1001, 'toncy vj', 'Manager', 80000, 1),
    (1002, 'babu tj', 'Assistant Manager', 60000, 2),
    (1003, 'neethu roy', 'Clerk', 40000, 1),
    (1004, 'chinnu alaxender', 'Manager', 70000, 4),
    (1005, 'Emu sajan', 'Cleaning', 30000, 1),
    (1006, 'nithin', 'Librarian', 40000, 1),
    (1007, 'tony joseph', 'Assistant Manager', 650000, 7),
    (1008, 'Michael Alex', 'Clerk', 40000, 2),
    (1009, 'Sony Mathews', 'Clerk', 40000, 1),
    (1010, 'vibi varghese', 'Clerk', 40000, 1);

-- Create the Books table
CREATE TABLE Books (
    ISBN VARCHAR(20) PRIMARY KEY,
    Book_title VARCHAR(50),
    Category VARCHAR(30),
    Rental_Price int,
    Status VARCHAr(30),
    Author VARCHAR(50),
    Publisher VARCHAR(50)
);
INSERT INTO Books (ISBN, Book_title, Category, Rental_Price, Status, Author, Publisher)
VALUES
('984764', 'The Lean Startup', 'Business', 28, 'yes', 'Eric Ries', 'Crown Business'),
('789547', ' A Brief History of Humankind', 'History', 22.99, 'no', 'Yuval Noah Harari', 'Harper'),
('412536', 'The Hunger Games', 'Fiction', 34, 'yes', 'Suzanne Collins', 'Scholastic Press'),
('748123', 'The Power of Habit', 'Self-Help', 19.99, 'no', 'Charles Duhigg', 'Random House'),
('102354', 'The Life-Changing Magic of Tidying Up', 'Self-Help', 16.99, 'yes', 'Marie Kondo', 'Ten Speed Press'),
('887421', ' A Brief History of Tomorrow', 'History', 29, 'yes', 'Yuval Noah Harari', 'Harper'),
('884512', 'Catching Fire', 'Fiction', 14.99, 'no', 'Suzanne Collins', 'Scholastic Press'),
('024536', 'The Power of Habit', 'Self-Help', 26, 'yes', 'Charles Duhigg', 'Random House'),
('78910', ' belive in yourself', 'Self-Help', 18.99, 'yes', 'Marie Kondo', 'Ten Speed Press'),
('362419', '21 Lessons for the 21st Century', 'History', 22.99, 'no', 'Yuval Noah Harari', 'Harper');

-- Create the Customer table
CREATE TABLE Customer (
    Customer_Id INT PRIMARY KEY,
    Customer_name VARCHAR(50),
    Customer_address VARCHAR(50),
    Reg_date DATE
);
INSERT INTO Customer (Customer_Id, Customer_name, Customer_address, Reg_date)
VALUES
(1, 'minnu alaxander','123 tower road kollam','2021-05-11'),
(2, 'anu sn', ' nh bypass city tower','2024-05-12'),
(3, 'toncy vj', 'srenarayanapuram temple road','2020-05-13'),
(4, 'tony vj','convent roaD254','2021-05-14'),
(5, 'manu varghese','mahanmagandhi road ekm','2018-05-15'),
(6, 'vibi varghese','gandhi tower near moham hospital','2023-05-16'),
(7, 'chinnu alaxander','marine mall kollam','2019-05-17'),
(8, 'ancy john','gandhi bavan thankey','2023-05-18'),
(9, 'ponnu simon','bakary road punnapuzha','2022-05-19'),
(10, 'neethu cy','st jude church ekm','2023-05-20');
  


-- Create the IssueStatus table
CREATE TABLE IssueStatus (
    Issue_Id INT PRIMARY KEY,
    Issued_cust INT,
    Issued_book_name VARCHAR(50),
    Issue_date DATE,
    Isbn_book VARCHAR(30),
    FOREIGN KEY (Issued_cust) REFERENCES Customer(Customer_Id),
    FOREIGN KEY (Isbn_book) REFERENCES Books(ISBN)
);
INSERT INTO IssueStatus (Issue_Id, Issued_cust, Issued_book_name, Issue_date, Isbn_book)
VALUES
(1, 1, 'The Lean Startup', '2023-06-01', '984764'),
(2, 2, ' A Brief History of Humankind', '2023-05-05', '789547'),
(3, 3, 'The Hunger Games', '2023-06-10', '412536'),
(4, 4, 'The Power of Habit', '2023-05-15', '748123'),
(5, 5, 'The Life-Changing Magic of Tidying Up', '2023-05-20', '102354'),
(6, 6, 'A Brief History of Tomorrow', '2018-05-25', '887421'),
(7, 7, 'Catching Fire', '2023-05-30', '884512'),
(8, 8, 'The Power of Habit', '2023-06-04', '024536'),
(9, 9, 'belive in yourself', '2023-06-08', '78910'),
(10, 10, '21 Lessons for the 21st Century', '2023-06-12', '362419');

-- Create the ReturnStatus table
CREATE TABLE ReturnStatus (
    Return_Id INT PRIMARY KEY,
    Return_cust INT,
    Return_book_name VARCHAR(50),
    Return_date DATE,
    Isbn_book2 VARCHAR(20),
    FOREIGN KEY (Return_cust) REFERENCES Customer(Customer_Id),
    FOREIGN KEY (Isbn_book2) REFERENCES Books(ISBN)
);

INSERT INTO ReturnStatus (Return_Id, Return_cust, Return_book_name, Return_date, Isbn_book2)
VALUES
(1, 1, 'The Lean Startup', '2023-06-01', '984764'),
(2, 2, ' A Brief History of Humankind', '2023-05-05', '789547'),
(3, 3, 'The Hunger Games', '2023-05-10', '412536'),
(4, 4, 'The Power of Habit', '2023-05-15', '748123'),
(5, 5, 'The Life-Changing Magic of Tidying Up', '2023-05-20', '102354'),
(6, 6, 'A Brief History of Tomorrow', '2023-05-25', '887421'),
(7, 7, 'Catching Fire', '2023-05-30', '884512'),
(8, 8, 'The Power of Habit', '2023-06-04', '024536'),
(9, 9, 'belive in yourself', '2023-06-08', '78910'),
(10, 10, '21 Lessons for the 21st Century', '2023-06-12', '362419');


#1  Retrieve the book title, category, and rental price of all available books
SELECT Book_title, Category, Rental_Price
FROM Books
WHERE Status = 'yes';

#2 ist the employee names and their respective salaries in descending order of salary
SELECT Emp_name, Salary
FROM Employee
ORDER BY Salary DESC;

#3 retrieve the book titles and the corresponding customers who have issued those books:
SELECT b.Book_title, c.Customer_name
FROM Books b
JOIN IssueStatus i ON b.ISBN = i.Isbn_book
JOIN Customer c ON i.Issued_cust = c.Customer_Id;

#4 display the total count of books in each category:
SELECT Category, COUNT(*) AS Total_Books
FROM Books
GROUP BY Category;

#5 retrieve the employee names and their positions for the employees whose salaries are above Rs.50,000:
SELECT Emp_name, Position
FROM Employee
WHERE Salary > 50000;

#6  list the customer names who registered before 2022-01-01 and have not issued any books yet:
SELECT c.Customer_name
FROM Customer c
LEFT JOIN IssueStatus i ON c.Customer_Id = i.Issued_cust
WHERE c.Reg_date < '2022-01-01' AND i.Issued_cust IS NULL;

#7 display the branch numbers and the total count of employees in each branch:
SELECT Branch_no, COUNT(*) AS Total_Employees
FROM Employee
GROUP BY Branch_no;

#8 display the names of customers who have issued books in the month of June 2023:
SELECT c.Customer_name
FROM Customer c
JOIN IssueStatus i ON c.Customer_Id = i.Issued_cust
WHERE MONTH(i.Issue_date) = 6 AND YEAR(i.Issue_date) = 2023;

#9 retrieve book titles from the book table containing 'history':
SELECT Book_title
FROM Books
WHERE Book_title LIKE '%history%';

#10 retrieve the branch numbers along with the count of employees for branches having more than 5 employees:
SELECT Branch_no, COUNT(*) AS Employee_Count
FROM Employee
GROUP BY Branch_no
HAVING COUNT(*) > 5;


#11 retrieve the names of employees who manage branches and their respective branch addresses:
SELECT e.Emp_name, b.Branch_address
FROM Employee e
JOIN Branch b ON e.Branch_no = b.Branch_no
WHERE e.Position = 'Manager';

#12 display the names of customers who have issued books with a rental price higher than Rs. 25:
SELECT c.Customer_name
FROM Customer c
JOIN IssueStatus i ON c.Customer_Id = i.Issued_cust
JOIN Books b ON i.Isbn_book = b.ISBN
WHERE b.Rental_Price > 25;
