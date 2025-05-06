CREATE DATABASE IF NOT EXISTS bdaws;
use bdaws;

create table usuarios(
id int primary key auto_increment,
nome varchar(100) not null,
email varchar(100) not null,
filme varchar(250) not null,
nota varchar(10) not null,
opiniao varchar(300) not null
);
