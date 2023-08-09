create database if not exists app default character set utf8 collate utf8_general_ci;
use app;

CREATE TABLE users (
	id INT PRIMARY KEY AUTO_INCREMENT,
    fullname TEXT NOT NULL,
    username VARCHAR(50) NOT NULL,
    pass_word VARCHAR(100) NOT NULL
);
insert into users values (null,"Admin","admin","admin");
select * from users;

create table contact (
	cname text not null,
    ccontact varchar(50) not null,
    csubject varchar(30) not null,
    cmessage varchar(500) not null 
);
select * from contact;

create table newsletter (
	id int primary key auto_increment,
    email varchar(99) not null
);
select * from newsletter;

create table booknow (
	id int primary key auto_increment,
    fullname varchar(99),
    destination varchar(50),
    totalcost int,
    contactnumber bigint,
    address varchar(99)
);
select * from booknow;

create table er (
	id int primary key auto_increment,
    user_id int,
    edate varchar(20),
    etime varchar(20),
    ename text,
    eamount int,
    destination text,
    place text,
    ptype text,
    category text,
    foreign key (user_id) references users(id)
);
select * from er;
insert into er values (null,1,"01/01/2023","12:21","Biryani","1200","Karachi","Naseeb Biryani","Cash","Lunch");




/* Future work on the below code perspective*/
create table localplans (
	id int primary key auto_increment,
    destination text,
    image1 longblob,
    image2 longblob,
    image3 longblob,
    duration varchar(50),
    lp_description text,
    amount varchar(15)
);
select * from localplans;
insert into localplans
values (
    1,
    "Khyber Pakhtunkhwa",
    "C:/Project/static/img/Destinations/KPK/KPK.png",
    "C:/Project/static/img/Destinations/KPK/KPK2.png",
    "C:/Project/static/img/Destinations/KPK/KPK3.png",
    "10 Days and 10 Nights",
    "Captivating mountains, valleys, landscapes. Tourists adore culture, hospitality, adventure. Ideal for nature lovers, enthusiasts.",
    "Rs. 40,000"
),
(
    2,
    "Sindh",
    "C:/Project/static/img/Destinations/Sindh/Sindh.png",
    "C:/Project/static/img/Destinations/Sindh/Sindh2.png",
    "C:/Project/static/img/Destinations/Sindh/Sindh3.png",
    "10 Days and 10 Nights",
    "Sindh has historical and cultural wonders. Karachi's streets and Mohenjo-Daro's ruins invite exploration. Sindh offers heritage, cuisine, and Sindhi hospitality.",
    "Rs. 25,000"
),
(
    3,
    "Balochistan",
    "C:/Project/static/img/Destinations/Balochistan/Balochistan.png",
    "C:/Project/static/img/Destinations/Balochistan/Balochistan2.png",
    "C:/Project/static/img/Destinations/Balochistan/Balochistan3.png",
    "10 Days and 10 Nights",
    "A province in Pakistan, rugged beauty, cultural richness. Deserts, mountains, coastline, diverse landscapes. Explore archaeology, hospitality, traditions, cuisine.",
    "Rs. 30,000"
),
(
    4,
    "Punjab",
    "C:/Project/static/img/Destinations/Punjab/Punjab.png",
    "C:/Project/static/img/Destinations/Punjab/Punjab2.png",
    "C:/Project/static/img/Destinations/Punjab/Punjab3.png",
    "10 Days and 10 Nights",
    "Punjab, Pakistan, rich history, vibrant culture, fertile landscapes. Badshahi Mosque, Lahore. Serene fields, rural countryside. Captivating tourists: landmarks, cuisine, people.",
    "Rs. 35,000"
),
(
    5,
    "Northern Areas",
    "C:/Project/static/img/Destinations/Northern_Pakistan/NA1.png",
    "C:/Project/static/img/Destinations/Northern_Pakistan/NA2.png",
    "C:/Project/static/img/Destinations/Northern_Pakistan/NA3.png",
    "10 Days and 10 Nights",
    "The Northern Areas of Pakistan feature stunning mountains, lakes, and cultures, attracting adventurers and nature lovers.",
    "Rs. 70,000"
);

create table interplans (
	id int primary key auto_increment,
    destination text,
    image1 longblob,
    image2 longblob,
    image3 longblob,
    duration varchar(50),
    lp_description text,
    amount varchar(15)
);
select * from interplans;
insert into interplans
values (
    1,
    "Singapore",
    "C:/Project/static/img/Destinations/Singapore/Singapore1.png",
    "C:/Project/static/img/Destinations/Singapore/Singapore2.png",
    "C:/Project/static/img/Destinations/Singapore/Singapore3.png",
    "5 Days and 5 Nights",
    "Captivating city-state in Southeast Asia. Delights visitors with charm. Modern skyscrapers, green spaces, cultural diversity.",
    "Rs. 700,000"
),
(
    2,
    "Malaysia",
    "C:/Project/static/img/Destinations/Malaysia/Malaysia1.png",
    "C:/Project/static/img/Destinations/Malaysia/Malaysia2.png",
    "C:/Project/static/img/Destinations/Malaysia/Malaysia3.png",
    "5 Days and 5 Nights",
    "Vibrant capital Malaysia. Bustling metropolis. Skyscrapers, markets, culture, food. Modernity, tradition, wonders, experiences.",
    "Rs. 500,000"
),
(
    3,
    "Thailand",
    "C:/Project/static/img/Destinations/Thailand/thailand1.png",
    "C:/Project/static/img/Destinations/Thailand/thailand2.png",
    "C:/Project/static/img/Destinations/Thailand/thailand3.png",
    "5 Days and 5 Nights",
    "Thailand, 'Land of Smiles' Southeast Asian country. Cultural heritage, stunning landscapes, delicious cuisine. Popular destination worldwide.",
    "Rs. 300,000"
),
(
    4,
    "United Arab Emirates",
    "C:/Project/static/img/Destinations/UAE/UAE.png",
    "C:/Project/static/img/Destinations/UAE/uae1.png",
    "C:/Project/static/img/Destinations/UAE/uae2.png",
    "5 Days and 5 Nights",
    "Captivating mountains, valleys, landscapes. Tourists adore culture, hospitality, adventure. Ideal for nature lovers, enthusiasts.",
    "Rs. 350,000"
),
(
    5,
    "Turkey",
    "C:/Project/static/img/Destinations/Turkey/Turkey1.png",
    "C:/Project/static/img/Destinations/Turkey/Turkey2.png",
    "C:/Project/static/img/Destinations/Turkey/Turkey3.png",
    "5 Days and 5 Nights",
    "Turkey: East-West blend. Ancient wonders, vibrant bazaars. Breathtaking landscapes, warm hospitality. Istanbul's Hagia Sophia, delicious cuisine. Stunning coastlines, rich culture.",
    "Rs. 650,000"
);
