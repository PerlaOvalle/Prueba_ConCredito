CREATE TABLE grades(
  id int not null AUTO_INCREMENT,
  name varchar(225),
  grade double,
  PRIMARY KEY(id)
  )

INSERT INTO grades(name,grade)VALUES
 ('Aitor',100),
 ('Adrian',98.4),
 ('Angel',98),
 ('Adriana',90),
 ('Alexis',90),
 ('Adolfo',78),
 ('Andres',78),
 ('Alvaro',70),
 ('Antonio',67),
 ('Alejo',56),
 ('Edgar',100),
 ('Emanuel',20);

select * from grades ORDER BY grade DESC LIMIT 10