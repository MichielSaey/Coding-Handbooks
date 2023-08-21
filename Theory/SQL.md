<!-- TOC -->
* [SQL](#sql)
  * [Comments](#comments)
* [Relational Data Model](#relational-data-model)
  * [Important terms](#important-terms)
  * [Rules and restrictions](#rules-and-restrictions)
  * [Integrety](#integrety)
  * [Relationships](#relationships)
* [Search a data base](#search-a-data-base)
  * [Order of evaluation of the statement](#order-of-evaluation-of-the-statement)
  * [`ORDER BY`](#order-by)
  * [`GROUP BY`](#group-by)
  * [`HAVING`](#having)
  * [Sub query](#sub-query)
* [Table alterations](#table-alterations)
  * [`UPDATE`](#update)
  * [`DELETE`](#delete)
  * [`TURNCATE`](#turncate)
  * [`INSET INTO`](#inset-into)
* [Aggregate functions](#aggregate-functions)
  * [Examples of usage](#examples-of-usage)
  * [`CASE`](#case)
  * [`COALESCE`](#coalesce)
  * [User defined variables](#user-defined-variables)
  * [Local variables](#local-variables)
  * [System variables](#system-variables)
  * [Views](#views)
  * [Triggers](#triggers)
  * [Constraints](#constraints)
* [Exercises](#exercises)
  * [1/4](#14)
  * [2/4](#24)
  * [3/4](#34)
<!-- TOC -->

# SQL

## Comments

Comments can be inserted on a separate line or within a Transact-SQL statement. Multiple-line comments must be indicated by /* and */. A stylistic convention often used for multiple-line comments is to begin the first line with /*, subsequent lines with **, and end with */. There is no maximum length for comments

# Relational Data Model

## Important terms

1. **Relation** - A Two dimensional table that represents table that represents some entity or relationship
2. **Entity** - Abstraction of a real life object like a car
3. **Relationship** - Defines how entities are connected
4. **Attribute** - A colum in a table
5. **Tuple** - Is a row in a table

## Rules and restrictions

1. There cannot be two relation with the same name in a database
2. All attributes within the same relation should have different names
3. there should only be one value in each cell
4. The order of the rows and columns is not important

## Integrety

**Entity integrity**: This means that you can not have two identical tuples(rows) in the table. To maintain this integrity we use **primary keys (PK)**. This PK is a field or a set of field that are used that is used to uniquely identify every record in the database.

**Referential integrity** accours when we have two connected relations. This relationship is provided a **foreign key(FK)**. A FK ina table is the reference to the PK of another table.

## Relationships

1. **one-to-one relationship (1-1)** - One row in the first table can be associated with no more than tuple of another relation.
2. **one-to-may relationship (1-M)** - Means that a row in the fist table can multiple assosiated rows in an other table
3. **many-to-many relationship (M-M)** - A set of tuples can have an associated set in another table (De Facto never happens, while use a central table to turn M-M into two 1-M)

# Indexes
Indexes organize data in a special way that significantly increases the speed of READ queries.

By default, databases either store entries of a dataset in an unordered way or order them according to some internal 
rule depending on an internal attribute. It would take too long to find one or more entries that match the given 
criteria if the amount of data is really huge. A database index represents a data structure that is formed from the 
values of one or more attributes and points to the corresponding entries of the data. It boosts the data-finding process
but requires some extra space to store this additional structure.

## Types of indexes

**Simple or compound**: The simple index is created by a single attribute. Whereas teh compount or composit index is 
built on top of two or more attributes of entries. It is also possible to use several simple and/or composite indexes 
together.

**Clustered and non-clustered**: The clustered index is an index that physically reorganizes the order in which the data 
entries are stored and gives the maximum speedup. Whereas a non-clustered index doesn't change the physical structure of 
a dataset, but only organizes references to the corresponding entries.

The **unique index** is used to ensure data integrity by prohibiting duplicate values in one or more attributes of data entries.

The **partial index** is created on a specific subset of data based on a given criterion.

## B-Tree Indexes

**B-Tree** is the most common type of index. When developers say "index", they often mean this type by default because 
it is supported by all popular databases and can be used in many different scenarios. As the name suggests, this index 
is based on a balanced tree that maintains data sorted according to a specified condition.

The top node is the root, and those below it are either child nodes or leaf nodes. We always start searching for our row 
from the root node. We compare if the value we’re searching for is less than or greater than the value in the node at 
hand. The result of the comparison tells us which way to go, left or right, depending on the result of our comparison. 
In the example above, all values lower than 1800 take us to the left, while values greater than 1800 take us to the 
right, and so on.

Moreover, B-Tree indexes are not limited to working with numbers only. They can be used with dates, times, strings, and 
other ordered data types. However, there is an important limitation when working with strings and B-Tree indexes: the 
equality operator works only from the leftmost part of a string (e.g. "c...", "ca..", "cat...") in alphabetical order. 
So, if you search for all strings that match the pattern like "..cat..", your index won't work. In this case, you should 
use an inverted Index.

## Hash Index

As you might have guessed, the hash index is based on a hash function. This function converts any database value to a 
numeric value called hash code. Once you have a query that uses comparison by this value, the database doesn't have to 
scan the entire dataset to find the match. Instead, it will calculate the hash of the value used in the query condition 
and directly access that place where data with the same hash is stored.

## Bitmap index

The bitmap index is a special type of index that is used when an attribute has a small number of distinct values 
compared to the total number of entries with this attribute. This situation is called low cardinality. There are just 
two possible boolean values false and true. Bitmap indexes are fast to create and don't require a lot of space if we 
compare them with B-Tree indexes. Some databases may create a bitmap index automatically for every query when it is 
needed.

## Inverted index

The inverted index is another type of index that is primarily used to find data in textual attributes or arrays. The 
typical scenario when you need to use this index is a full-text search. The key idea of an inverted index is to keep a 
special data structure that connects terms (words or values), which are used in search, to entries when the terms occur. 
The example below gives you an example of the index:

 * "green" -> [1, 2, 3]
 * "red" -> [2, 3, 5]
 * "summer" -> [1, 2, 6]

## Spatial index

The spatial index is an index used to speed up work with geometrical and geographical data (geospatial). Spatial indexes 
are usually used in navigation and geographic information databases. These indexes can quickly respond to queries such 
as "Find all museums within 5 km of a specific location". In practice, there are different data structures that can be 
used to organize spatial indexes; one of them is R-Tree.

# Search a data base

## Order of evaluation of the statement

1. FROM
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY

## `ORDER BY`

To specify the order of the reslulting rows you should use `ORDER BY` in the querry.
```sql
SELECT
    hotel_id,
    hotel_name,
    price_per_night,
    price_for_early_check_in,
    rating,
    stars
FROM
    hotels
ORDER BY
    price_per_night
```

This example can also sort for two night with early check in.

```sql
SELECT
    hotel_id,
    hotel_name,
    price_per_night,
    price_for_early_check_in,
    rating,
    stars
FROM
    hotels
ORDER BY
    price_per_night*2 + price_for_early_check_in
```
```sql
SELECT
    hotel_id,
    hotel_name,
    price_per_night,
    price_for_early_check_in,
    rating,
    stars
FROM
    hotels
ORDER BY
    rating DESC,
    price_per_night*2 + price_for_early_check_in
```
```sql
SELECT
    hotel_name,
    price_per_night*2 + price_for_early_check_in AS total_price,
    rating,
    stars
FROM
    hotels
ORDER BY
    total_price, 3 DESC
```

## `GROUP BY`
```sql
SELECT
    stock_name,
    MAX(price) AS maximum
FROM
    stocks
GROUP BY
    stock_name;
```
| stock_name | maximum |
|------------|---------|
| WTI        | 89.8    |
| FB         | 63.7    |
| DJI        | 52.7    |

## `HAVING`

Queries with a GROUP BY statement are regular in a way that they allow to filter rows with WHERE statement and to order them with ORDER BY statement. There is another clause that is especially helpful with grouping tasks – HAVING. If WHERE accepts conditions on values that certain cells have, HAVING does the same but for values of already computed aggregations. For example, let's select "stock-datetime" pairs with maximum price above 50:

```sql
SELECT
    stock_name,
    datetime,
    MAX(price) AS maximum
FROM
    stocks
GROUP BY
    stock_name,
    datetime
HAVING
    MAX(price) > 50;
```

| stock_name | datetime         | maximum |
|------------|------------------|---------|
| WTI        | 2020-05-17 11:00 | 89.8    |
| FB         | 2004-05-28 21:09 | 63.7    |
| DJI        | 1998-03-31 04:18 | 52.7    |

## Sub query

````sql
SELECT
    username,
    sign_up_date 
FROM
    registered_users 
WHERE
    sign_up_date = (
        SELECT 
            MIN(sign_up_date) 
        FROM 
            registered_users
    ); 
````

````sql
SELECT *, 
    (SELECT 
         name 
     FROM 
         users_info 
     WHERE 
         username = registered_users.username) AS name 
FROM
    registered_users
````

````sql
SELECT 
    id,
    product 
FROM
    new_orders AS newor 
WHERE unit_price < (
    SELECT 
        AVG(unit_price) 
    FROM 
        new_orders
    WHERE 
        product_category = newor.product_category);
````

Sub-query in update statement

````sql
UPDATE
    students 
SET
    exams_passed = TRUE 
WHERE 
    name in (
        SELECT
            name
        FROM
            exam_results 
        WHERE
            math_exam_mark >= 18
            AND english_exam_mark >= 18
        ); 
````

Sub-query nested in the INSERT statement

````sql
INSERT INTO employees 
VALUES (
    'Tomas Hedwig', 
    (SELECT salary FROM employees WHERE name = 'Ann Reed'), 
    (SELECT id FROM departments WHERE department = 'PR')
)
````

Sub-queries nested in the DELETE statement

````sql
DELETE FROM orders
WHERE customer_id = (SELECT customer_id FROM customers WHERE name = 'Ann Smith')
````

# Table alterations

## `UPDATE`

Changes department_id from whole set to 14
```sql
UPDATE employees
SET department_id = 14;
```
Update id and increase sallery
```sql
UPDATE employees
SET department_id = 14,
salary = salary + 10000;
```
## `DELETE`

DELETE is a Data Manipulation Language (DML) command. We use it to remove a tuple or several tuples from the relation, or just eliminate a tuple. To filter the tuples you want to delete, you need to apply the WHERE clause. If you do not specify any selection, DELETE removes or eliminates the entire tuple. Let's memorize the syntax of the command below:

````sql
delete from table_name where [condition]
````

## `TURNCATE`

`TRUNCATE` is a command similar to `DELETE`, it is used to remove tuples. But unlike the `DELETE`, `TRUNCATE` eliminates all data from a table, including tuples and attribute values. However, the table structure is kept in the database, so if needed, you can recreate the deleted tuples.
`TRUNCATE` does not function with the `WHERE` clause

````sql
TRUNCATE TABLE products
````

## `INSET INTO`

Let's move the information from the column customer to the column user, from email to user_email and from zip_code to zip_code. We can use the INSERT INTO SELECT statement to do it.

````sql
INSERT INTO unsers (user, user_email, zip_code)
SELECT * FROM customers
````

````sql
INSERT INTO users
SELECT 
    supplier,
    supplier_email,
    zip_code,
    city
FROM
    suppliers
WHERE
    supplier = 'Tomato Inc'
````

# Aggregate functions

When you need to combine the data of multiple cells, you can use aggregate functions.

Here is a list of aggregate functions:
* MIN
* MAX
* AVG
* COUNT
* SUM

## Examples of usage
```sql
SELECT MAX(price)
FROM stocks;
```

```sql
SELECT SUM(yesterday_deals)
FROM stocks;
```

```sql
SELECT
    AVG(price) AS avg_price,
    AVG(yesterday_deals) AS avg_deals
FROM
    stocks
WHERE
    price > 40;

DISTINCT allows you to omit all duplicate values.
```
    
SELECT COUNT(DISTINCT yesterday_deals)
FROM stocks;

## `CASE`
The `CASE` expression helps us get different result based on stated conditions. in this example we will be working in folowing dataset.

| name         | age |
|--------------|-----|
| Tamara Fetch | 25  |
| Thomas Jones | 17  |
| Ann Hardy    | 14  |
| Robert Stark | 20  |

Lets say we want to label this list with `adult` and `minor` coresposponding to their age.

````sql
select 
    name,
    case 
        when age >= 18 then `adult`
        else `minor`
    end as age_status
````
| name         | sge_status |
|--------------|------------|
| Tamara Fetch | adult      |
| Thomas Jones | minor      |
| Ann Hardy    | minor      |
| Robert Stark | adult      |       

below follow more examples

````sql
SELECT 
    client_id, 
    name, 
    CASE city 
        WHEN 'New-York' THEN 'USA'
        WHEN 'London' THEN 'UK' 
        WHEN 'Moscow' THEN 'Russia'
        END AS country 
FROM
    clients;
````

## `COALESCE`

The COALESCE function receives a list of values and returns the first non-null value in this list. If all the values in the list are NULL, the COALESCE statement will return NULL.

```sql
select coalesce(null, null, 'Alice', null, 1) as first_non_null
```

| first_non_null |
|----------------|
| Alice          |

The following code section replaces null values with the text 'No department'

```sql
SELECT 
    name, 
    COALESCE(department, 'No department') AS department 
FROM 
    employees; 
```

## User defined variables

In MySQL, we can use both `SET` and `SELECT` commands to declare the variable. The assignment operator also has no restrictions: we can use either = or :=, depending on the situation. The user-defined variable can be any data type: integer, decimal, string, boolean, and so on.

````sql
SET @name = 'MySql';
    
SELECT @name
````

````sql
SELECT @max_price := MAX(price) FROM products;

SELECT * FROM products
WHERE price = @max_price;
````

## Local variables

The variables we discussed in the previous paragraph can be used in any part of the program. In contrast to that, local variables can only be used in a specific block of code, and cannot be accessed outside of this block of code. Local variables also have their own peculiarities.

````sql
DECLARE a INT;
DECLARE b INT;
DECLARE c INT DEFAULT 30;

SET a = 5;
SET b = 10;

SELECT a + b + c;
````

## System variables
System variables are variables that have already been created by the DBMS itself. They store the data we need to work with the database. Each system variable in MySQL has a default value, and these system variables are used to configure the way the database operates.

````sql
SHOW VARIABLES;
````

## Views

````sql
CREATE VIEW favorite_books AS
SELECT 
    author_name, 
    book_name
FROM 
    books
WHERE 
    plot_score = 5;
````

````sql
CREATE VIEW sales_by_film_category
AS
SELECT
   c.name AS category,
   SUM(p.amount) AS total_sales
FROM payment AS p
   JOIN rental AS r ON p.rental_id = r.rental_id
   JOIN inventory AS i ON r.inventory_id = i.inventory_id
   JOIN film AS f ON i.film_id = f.film_id
   JOIN film_category AS fc ON f.film_id = fc.film_id
   JOIN category AS c ON fc.category_id = c.category_id
GROUP BY c.name;
````

## Triggers

A trigger is a database object that is associated with the database table. Accordingly, when you delete a table, all triggers associated with it will also be deleted.

A trigger is a stored procedure that you create and specifically place inside your table. After that, it will independently execute the created operations inside the database. It will be automatically activated when the defined in your trigger event arrives in the database table.

Triggers have the following advantages. As they are self-executing from within the database, they are often used to save incoming information to multiple database locations. Also, they may be recording and logging user actions, and checking rules for incoming data into database tables.

Because triggers run on their own, you need to keep check of what triggers are in your database and what they do, as it's almost impossible to track their actions from the outside.

See an overview of all triggers.

````sql
SHOW TRIGGERS;
````

To drop a trigger:

````sql
DROP TRIGGER big_salary;
````

The following trigger will update a variable everytime it is updated:

````sql
CREATE TRIGGER additional_salary
BEFORE INSERT ON employee 
FOR EACH ROW 
SET @sum = @sum + NEW.salary;
````

Every time a new employe is inserted it will check if the salary is valled.

````sql
CREATE TRIGGER big_salary
BEFORE INSERT ON employee
FOR EACH ROW PRECEDES additional_salary
IF NEW.salary>5000 THEN SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'Salary has exceeded the allowed amount of 5000.00';
END IF;
````

Archiving deleted data

````sql
CREATE TABLE fired_employee (ID INT, name VARCHAR(20), fire_date DATE);

CREATE TRIGGER save_fire_employee
    AFTER DELETE
    ON employee
    FOR EACH ROW
BEGIN
    INSERT INTO fired_employee VALUES (OLD.id, OLD.name, CURDATE());
    SET @sum = @sum - OLD.salary;
END;

DELETE FROM employee WHERE id = 1;
````

````sql
CREATE TRIGGER upd_check_salary
BEFORE UPDATE ON employee
FOR EACH ROW
BEGIN
    IF NEW.salary < 0 THEN
        SET NEW.salary = 0;
    ELSEIF NEW.salary > 5000.00 THEN
        SET NEW.salary = 5000.00;
    END IF;
END;
````

## Constraints

https://hyperskill.org/learn/step/9587

## Window functions

Working with a database, you may need to analyze some data. Your employer might ask you to create a list of those who overperform in your company or to make a sales report with three-month rolling averages. You can use some external tools, such as Excel or Python. Or you can use the built-in SQL functionality. In this topic, we will learn, how to do these tasks with MySQL window functions.

To understand the window function concept, imagine that MySQL has completed all of the query steps, including joining, grouping, and sorting. So, the result set is ready to be returned. What if we tried to stop the query execution at this point, aggregate some data, and analyze it? Of course, you can do this using the GROUP BY construction. However, it means a lot of restrictions: you will get only the unique values of the required columns, so the result will be fewer rows than the original table. Window functions record the result in separate columns and don't change the number of rows. Also, it gives you some useful tools, like an opportunity to set the order of rows bypass.

Let's take a closer look at some simple examples. In the query below, you "open the window" through the OVER() statement and summarize the number of sold tickets.

```sql
SELECT
    film_name,
    film_genre,
    ticket_number,
    SUM(ticket_number) OVER() AS sum
FROM 
    film_sales;
```

| film_name          | film_genre | ticket_number | sum |
|--------------------|------------|---------------|-----|
| The Lion King      | cartoon    | 3             | 18  |
| Shrek              | cartoon    | 4             | 18  |
| Back to the Future | fiction    | 2             | 18  |
| Inception          | fiction    | 6             | 18  |
| Intouchables       | drama      | 3             | 18  |

As you can see, it is the total amount in the sum column for the whole table. If you want to calculate tickets for each genre separately, you may use the PARTITION BY construction inside the OVER clause, like this:

````sql
SELECT
    film_name,
    film_genre,
    ticket_number,
    SUM(ticket_number) OVER(PARTITION BY film_genre) AS sum
FROM 
    film_sales;
````

| film_name          | film_genre | ticket_number | sum |
|--------------------|------------|---------------|-----|
| The Lion King      | cartoon    | 3             | 7   |
| Shrek              | cartoon    | 4             | 7   |
| Back to the Future | fiction    | 2             | 8   |
| Inception          | fiction    | 6             | 8   |
| Intouchables       | drama      | 3             | 3   |

Apparently, the window functions can be compared with aggregate functions. The difference is that, after dividing into sets, window functions still process and return each row separately. In contrast, aggregate functions do not return all rows but only the results of groups.

What kind of parameters can we clarify in the OVER() clause?


`OVER([partition_clause] [order_clause] [frame_clause])`
* `partition_clause` points to the column, by which values of the query rows are divided into groups. if this parameter is not specified, rows are considered as one big group.
* `order_clause` indicates in what order the rows inside the partition should be placed while executing a window function. While it is unfortunate that exactly the same syntax is used for different purposes, be careful: if you want to have a certain order in the final result, you still need to use ORDER BY clause at the end of the query.
* `frame_clause` restricts the window borders relative to the position of the current row. For instance, you can calculate the rolling sum, taking the current, previous, and next rows. You can read more here.

**What can we do with window functions?** For a start, you can generate different rankings. By using row_number(), you can simply number the rows in each division. rank() assigns the same numbers to equal values with gaps, dense_rank() does that without gaps. This is easier to understand if you look at the example below, where we select the students with the best exam results and their numbers in the overall rating:

````sql
SELECT 
    name,
    exam_score,
    row_number() OVER() AS row_number,
    rank() OVER() AS rank,
    dense_rank() OVER() AS dense_rank
FROM
    report_journal
ORDER BY exam_score
````

| name  | exam_score | row_number | rank | dense_rank |
|-------|------------|------------|------|------------|
| Mark  | 100        | 1          | 1    | 1          |
| Emma  | 99         | 2          | 2    | 2          |
| Harry | 99         | 3          | 2    | 2          |
| Maria | 98         | 4          | 4    | 3          |
| Paul  | 97         | 5          | 5    | 4          |

Also, you can aggregate data, using min, max, avg, and other functions, but instead of placing it in the GROUP BY clause, you can put it in the OVER() clause. A simple example was at the top of this topic. According to it, here is how you can calculate the rolling sum, using FRAME clause (pay attention, the semantic part goes right away, without any keyword):

````sql
SELECT
    film_name,
    film_genre,
    ticket_number,
    SUM(ticket_number) OVER(PARTITION BY film_genre ROWS BETWEEN CURRENT ROW AND 1 FOLLOWING) AS sum 
FROM
    film_sales;
````

| film_name          | film_genre | ticket_number | sum |       |
|--------------------|------------|---------------|-----|-------|
| The Lion King      | cartoon    | 3             | 7   | = 3+4 |
| Shrek              | cartoon    | 4             | 4   | = 4   |
| Back to the Future | fiction    | 2             | 8   | = 2+6 |
| Inception          | fiction    | 6             | 15  | = 6+9 |
| Harry Potter       | fiction    | 9             | 9   | = 9   |



# Exercises

## 1/4

Find students who are in 3rd grade and have 5 points for all their courses.
The output should consist of the student names only in alphabetical order.
```sql
select
    Students.name
from main.Students
inner join Student_Subject subject
    on Students.student_id = subject.student_id
where
    Students.grade = 3
group by
    Students.name,
    Students.grade
having
    min(subject.result) >= 5proper
order by
    Students.name
```
## 2/4

Find four students with the most achievement points and list their names in alphabetical order with their scores.
The student's year is not critical.
The output should have only the name and the bonus point column.
The output should be in descending order of the bonus point column.

```sql
select
    Students.name,
    sum(A.bonus) as `bonus point`
from
    main.Students
inner join Student_Achievement SA
    on Students.student_id = SA.student_id
inner join Achievement A
    on SA.achievement_id = A.achievement_id
group by
    Students.name
order by
    sum(A.bonus) desc
limit 4
```

## 3/4

If the student's average is over 3.5 points for courses, output above average in the best column.
Otherwise, print below average. Order the results in alphabetical order by name.

```sql
select
    Students.name,
    case
        when avg(ss.result) > 3.5 then 'above average'
        else 'below average'
    end as `best`
from
    Students
inner join Student_Subject SS
    on Students.student_id = SS.student_id
group by
    Students.name
order by
    Students.name asc
```























