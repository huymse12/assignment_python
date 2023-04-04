create database LAPTOP;
use LAPTOP;
create table LAPTOPBESTSELLER
(
    Name            nvarchar(500) not null,
    OldPrice        double not null,
    NewPrice        double,
    PercentDiscount double,
    BestSeller      bool   not null,
    ID              int AUTO_INCREMENT not null,
    PRIMARY KEY (ID)
);