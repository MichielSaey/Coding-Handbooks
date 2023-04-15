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
* [Table alterations](#table-alterations)
  * [`UPDATE`](#update)
  * [`DELETE`](#delete)
* [Aggregate functions](#aggregate-functions)
  * [Examples of usage](#examples-of-usage)
  * [`CASE`](#case)
  * [`COALESCE`](#coalesce)
* [Constraints](#constraints)
* [Exercises](#exercises)
  * [1/4](#14)
  * [2/4](#24)
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



# Constraints

https://hyperskill.org/learn/step/9587

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























