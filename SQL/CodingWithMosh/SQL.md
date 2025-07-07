# SQL: 

`SQL` stands for **Structured Query Language**. This language is to query or modify our data.
Like many other languages `SQL` is Declerative which means we don't care about how, we care about what.

</br>

<img src="images/1.png">
<br>

## Declarative VS IMPERATIVE

### Declarative
<img src="images/Declarative.png">

### Impearative
<img src="images/Imperative.png">

## DBMS

`DBMS` stands for **Database Management System**.
- **Relational:** Datas are structured in to tables.
    - MySQL
    - PostgreSQL
    - Oracel

- **Non Relational:** (NoSQL)
    - Document
        - MongoDB
        - CouchDB
        - FireBase

    - Key Value    
        - Redis

    - Graph
        - Neo4J
        - GraphQL

    - Wide Columnar
        - Cassandre

<br>

## SQL Keywords:

- **USE**

    Choose a database with this keyword.

    - Example:

        ```SQL
        USE store_database;
        ```
<br>

- **SELECT**

    Select the columns form the table we want.

    - Example:

        ```SQL
        SELECT first_name, last_name FROM customers;
        ```

        ```SQL
        SELECT
            first_name,
            last_name,
            point * 10,
        FROM customers;
        ```
<br>

- **FROM**

    Choose the table which you want.

    - Example:

        ```SQL
        SELECT * FROM customers;
        ```
<br>

- **WHERE**

    return the results which saticfy the statment infront of ` WHERE`.

    - Example:

        ```SQL
        SELECT * FROM customers WHERE customer_id = 1;
        ```
<br>

- **ORDER BY**

    Order our output base on what we want.

    - Example:

        ```SQL
        SELECT * FROM customers ORDER BY first_name;
        ```
<br>

- **AS**

    Shows the selected columns as the way you want.

    - Example:

        ```SQL
        SELECT 
            (points * 10) AS 'discount_factor'
        FROM customers 
        ORDER BY first_name;
        ```

<br>

- **DISTINCT**

    This will remove the duplicates.

    - Example:

        ```SQL
        SELECT DISTINCT city
        FROM customers;
        ```
<br>

- **AND / OR / NOT**

    `AND` is always higher than `OR`, so it will be executed faster.

    - Example:

        ```SQL
        SELECT * 
        FROM cutomers
        WHERE points > 100 
        OR birth_date >= '1999-01-01';
        ```

        ```SQL
        SELECT *
        FROM order_items
        WHERE order_id = 6 
        AND unit_price * quantity > 30;
        ```

<br>

- **IN**

    `AND` is always higher than `OR`, so it will be executed faster.

    - Example:

        ```SQL
        SELECT * 
        FROM cutomers
        WHERE city NOT IN ('VA', 'FL', 'GA');
        ```

<br>

- **BETWEEM**


    - Example:

        ```SQL
        SELECT * 
        FROM cutomers
        WHERE points BETWEEN 1000 AND 2000
        ```

<br>

- **LIKE**

    we ukse `LIKE` operator to match patterns.

    - Example:

        Customers with b in the start of their name !
        ```SQL
        SELECT * 
        FROM cutomers
        WHERE last_name LIKE 'b%';
        ```

        Customers with letter b in their names.
        ```SQL
        SELECT * 
        FROM cutomers
        WHERE last_name LIKE '%b%';
        ```

        Customers with 5 letter length last name and ends with letter y.
        ```SQL
        SELECT * 
        FROM cutomers
        WHERE last_name LIKE '_____y';
        ```
        ```SQL
        SELECT *
        FROM customers
        WHERE address LIKE '%AVENUE%' OR 
            address LIKE '%TRAIL%';
        ```