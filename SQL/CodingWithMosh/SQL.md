# SQL: 

`SQL` stands for **Structured Query Language**. This language is to query or modify our data.
Like many other languages `SQL` is Declerative which means we don't care about how, we care about what.

Before Data Base, we had `File Processing System` and it had lots of pros but it's cons were way more.
</br>

<img src="images/1.png">
<br>

## Database Models:
- **Hierarchical Model:** Known as One-To-Many, cause each child can only have one parent.
<img src="images/Hierarchical Model.png">
<img src="images/Hierarchical XML.png">

- **Networking Model:** Known as Many-To-Many, it's a more developed version of Hierarchical Model.
<img src="images/Networking Model.png">
<img src="images/Networking XML.png" >

- **Relational Model:** No more Parent-Child Structure, instead it's Table Structure.
<img src="images/Relational Model.png">

## DBMS: Data Base Management Software

Different companies create different softwares with various features to compeate with eachother.

- **CRUD Operations**
    - Create
    - Reade
    - Update
    - Delete

- **Manage Data**
- **Security & Permissions**
- **Transaction Management**


## Declarative VS IMPERATIVE

### Declarative:
<img src="images/Declarative.png">

### Impearative: 
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

## Retrive Data from ***One*** Table:

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

    Order the output base on what we want.

    - Example:

        ```SQL
        SELECT * FROM customers
        ORDER BY first_name;
        ```

        ```SQL
        SELECT * FROM customers
        ORDER BY first_name DESC, last_name DESC;
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

    We ukse `LIKE` operator to match patterns.

    - **Example:**

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

<br>

- **REGEXP**

    We use `REGEXP` for regex expressions.
    
        - ^ : Beginning

        - $ : End
        
        - | : Logical Or
        
        - [abcd] : one of these characters
        
        - [a-h]  : Range of characters
    
    - Example:

        ```SQL
        SELECT *
        FROM customers
        WHERE last_name REGEXP 'field'
        ```

- **IS NULL**

    To find the rows with a ` NULL` value.

    - Example:

        ```SQL
        SELECT * 
        FROM cutomers
        WHERE phone IS NULL
        ```


- **LIMIT**

    With `LIMIT` we set limitation for the number of results which we get from the query.

    - Example:

        ```SQL
        SELECT * 
        FROM customers
        LIMIT 10;
        ```
        The first number infront of `LIMIT ` is offset which means the number of rows to skip and the second of is the number of rows which we want.

        ```SQL
        SELECT * 
        FROM customers
        LIMIT 6, 3;
        ```

## Retrive Data from ***Multiple*** Table: