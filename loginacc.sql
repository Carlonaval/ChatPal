create database loginacc;

CREATE TABLE loginacc.accounts(
	accounts_id INT NOT NULL,
    email VARCHAR(45) NOT NULL,
    password VARCHAR(45) NOT NULL,
    PRIMARY KEY (accounts_id)
);

INSERT INTO loginacc.accounts(accounts_id,email,password)
VALUES('1','cbnaval@mymail.mapua.edu.ph','carlson01');
INSERT INTO loginacc.accounts(accounts_id,email,password)
VALUES('2','ejmariano@mymail.mapua.edu.ph','ezekiel02');
INSERT INTO loginacc.accounts(accounts_id,email,password)
VALUES('3','hassison@mymail.mapua.edu.ph','herschel03');
INSERT INTO loginacc.accounts(accounts_id,email,password)
VALUES('4','knaesima@mymail.mapua.edu.ph','katreen04');
INSERT INTO loginacc.accounts(accounts_id,email,password)
VALUES('5','melmagmoyao@mymail.mapua.edu.ph','mikaella05');
