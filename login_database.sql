create database if not exists login;

CREATE TABLE if not exists login.accounts(
	accounts_id INT NOT NULL auto_increment,
    email VARCHAR(45) NOT NULL,
    password VARCHAR(45) NOT NULL,
    PRIMARY KEY (accounts_id)
);

INSERT INTO login.accounts(accounts_id,email,password)
VALUES('1','cbnaval@mymail.mapua.edu.ph','carlson01'),
('2','ejmariano@mymail.mapua.edu.ph','ezekiel02'),
('3','hassison@mymail.mapua.edu.ph','herschel03'),
('4','knaesima@mymail.mapua.edu.ph','katreen04'),
('5','melmagmoyao@mymail.mapua.edu.ph','mikaella05');

