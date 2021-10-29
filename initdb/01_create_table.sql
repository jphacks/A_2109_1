CREATE DATABASE IF NOT EXISTS main;
USE main;

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS article;
DROP TABLE IF EXISTS user_bookmarks;
DROP TABLE IF EXISTS user_likes;
DROP TABLE IF EXISTS user_pinned;

CREATE TABLE user
(
    ID          INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    name        varchar(255) NOT NULL,
    password    varchar(20) NOT NULL,
    mailAddress varchar(255) NOT NULL,
    image       TEXT
);

CREATE TABLE book
(
    ID          INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    title       varchar(255) NOT NULL,
    isbn        varchar(13) NOT NULL,
    author      varchar(255) NOT NULL,
    publishDate DATE,
    amazonLink  MEDIUMTEXT
);

CREATE TABLE article
(
    ID          INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    userId     INT NOT NULL,
    bookId      INT NOT NULL,
    context     TEXT NOT NULL,
    updatedDate DATE,
    chapter     INT,
    page        INT 
);

CREATE TABLE book_marks
(
    ID          INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    userID     INT NOT NULL,
    articleID   INT NOT NULL
);

CREATE TABLE user_likes
(
    ID          INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    userID     INT NOT NULL,
    articleID   INT NOT NULL
);

CREATE TABLE user_pinned
(
    ID          INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    userID     INT NOT NULL,
    BookID      INT NOT NULL
);
