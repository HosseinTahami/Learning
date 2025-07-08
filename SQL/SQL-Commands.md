# SQL Commands

## DCL: Data Control Language
- Grant
- Revoke

## DDL: Data Definition Language
- CREATE
- ALTER
- DROP
- RENAME
- TRUNCATE
- COMMENT

## DQL: Data Query Language
- SELECT

## DML: Data Modification Language
- INSERT
- UPDATE
- DELETE
- MERGE
- CALL
- EXPLAIN PLAN
- LOCK TABLE


## Functions

- AGGREGATE Functions:<br>
Run against all the data and produce one output.

- SCALAR Functions<br>
Run against each individual row.

    1- **CONCAT:**<br>
        Concat to columns together and show it as a new column.

    ```SQL
        SELECT emp_no,
            CONCAT(first_name, ' ', last_name) AS "NAME"
        FROM employees;
    ```