CREATE TABLE deliveryservice(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
price DOUBLE NOT NULL
);


CREATE TABLE productcategoty(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL
);


CREATE TABLE loyality(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
discount DOUBLE NOT NULL,
requiredsum DOUBLE NOT NULL
);


CREATE TABLE product(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
description TEXT,
name TEXT NOT NULL,
price DOUBLE NOT NULL,
category INTEGER NOT NULL,
image TEXT NOT NULL,
FOREIGN KEY(category) references productcategoty(id)
);

CREATE TABLE client(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
password TEXT NOT NULL,
firstname TEXT NOT NULL,
lastname TEXT NOT NULL,
email TEXT NOT NULL,
phone TEXT NOT NULL,
loyalitylevel INTEGER NOT NULL,
FOREIGN KEY(loyalitylevel) REFERENCES loyality(id)
);

CREATE TABLE delivery(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
serviceid INTEGER NOT NULL,
deliveryaddress TEXT NOT NULL,
FOREIGN KEY (serviceid) REFERENCES deliveryservice(id)
);


CREATE TABLE "order"(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
createtime INSUGNED BIG INT NOT NULL,
clientid INTEGER NOT NULL,
deliveryid INTEGER NOT NULL,
discount DOUBLE NOT NULL,
FOREIGN KEY(clientid) REFERENCES client(id),
FOREIGN KEY(deliveryid) REFERENCES delivery(id)
);


CREATE TABLE orderitem(
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
productid INTEGER NOT NULL,
amount INTEGER NOT NULL,
orderid INTEGER NOT NULL,
FOREIGN KEY(productid) REFERENCES product(id),
FOREIGN KEY(orderid) REFERENCES "order"(id)
);


INSERT INTO deliveryservice(name, price) values
('Нова пошта', '70' ),
('Укрпошта', '55'),
('Justin', '65');

INSERT INTO productcategoty(name) VALUES
('Корм для котів'),
('Корм для собак'),
('Корм для птахів'),
('Шампуні для котів');

INSERT INTO loyality(discount,requiredsum) VALUES
(0, 0),
(0.02, 7000),
(0.05, 15000),
(0.07, 23000),
(0.1, 30000);

INSERT INTO product(description,name , price , category , image) VALUES
('Для стерилізованих кішок та кастрованих котів, 2кг', 'Royal Canin Sterilised',539, 1, 'https://petslike.net/media/cache/app_shop_product_large_thumbnail/2c/34/92783fc1b1d17e0d6c26c40a8e23.jpeg'),
('Для собак середньої породи, 3кг', 'Brit Premium Adult M', 369.48,  2, 'https://pethouse.ua/assets/images/prods/britpremium/0000053171.jpg'),
('Для волнистих папуг, 500г', 'Папужка енергія',37, 3, ''),
('Шампунь для кішок та котят, 200мл', 'Beaphar Bio', 400  , 4, 'https://korm.com.ua/images/thumbnails/800/600/detailed/5671/t1228990max.jpg'),
('Для дорослих котів сіамскої породи, 10кг', 'Royal Canin Siamese Adult', 2430  , 1, 'https://content.rozetka.com.ua/goods/images/big/262363999.jpg'),
("Для дорослий йоркширських тер'єрів, 7.5 кг", 'Royal Canin Yorkshire Terrier Adult', 1813.5, 2, 'https://pethouse.ua/assets/images/prods/royalcanin/0000003221.jpg'),
('Основний корм для комахо-їдних птахів, 1кг', 'Padovan GRANPATEE INSECTES', 1899, 3, 'https://ezoo.com.ua/image/cache/1c/y/634c8d2a-8a15-11e6-8784-10feed0861cb-500x500.jpg');

INSERT INTO client(firstname, lastname, email, phone, loyalitylevel, password) VALUES
('test1', 'test1', 'test1@gmail.com', '38000000001', 1, 123123),
('test2', 'test2', 'test2@gmail.com', '38000000002', 1, 123123);


