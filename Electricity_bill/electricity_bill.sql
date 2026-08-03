create database Electricity_Bill;
show databases;
 use Electricity_Bill;

create table consumers(
	consumer_no varchar(20) primary key,
	consumer_name varchar(100) not null,
    address varchar(200) not null,
    mobile varchar(10),
    email varchar(100),-- 
    division varchar(100),
    sanctioned_load decimal(5,2),
    meter_no varchar(50),
    connection_date date
    );
 describe  consumers;

 create table bills(
 	bill_no varchar(30) primary key,
     consumer_no varchar(20) not null,
     bill_month varchar(20),
     bill_date date not null,
     due_date date not null,
     units decimal(10,2) not null,
     previous_due decimal(10,2),
     current_bill decimal(10,2),
     payable_amount decimal(10,2) not null,
     
 
    foreign key (consumer_no) references consumers(consumer_no)
 	);

  
-- alter table bills modify bill_month varchar(20) not null;
alter table bills modify previous_due decimal(10,2) not null,
				  modify current_bill decimal(10,2) not null;

    describe bills;

alter table  consumers
 modify mobile varchar(10) not null,
 modify email varchar(100) not null, 
 modify division varchar(100) not null,
 modify sanctioned_load decimal (5,2) not null,
 modify meter_no varchar(50) not null,
 modify connection_date date not null;
describe consumers;

 insert into consumers
 ( 
 consumer_no,consumer_name,address,mobile,email,
 division,sanctioned_load,meter_no,connection_date
 ) values
 (
  'C1001','Akshay Guru','VM impreza building, near old MLA quarters, Hyderguda, Himayathnagar, Hyderabad, Telangana 500029, India','7905287474',
   'akshay123@gmail.com', 'Hyderabad Central',4.0,'MTR1001','2024-01-15'
   ),
 (
 'C1002','Shivam kumar','H.No. 8-2-120/5, Srinagar Colony Main Road, Srinagar Colony, Hyderabad, Telangana - 500073','9236816717',
 'shivam@gmail.com','Hyderabad Central',4.0,'MTR1002','2023-02-15'
   ),
   (
   'C1003','Arjun Rawat','Flat No. 302, Sai Residency, Kukatpally Housing Board Colony, Kukatpally, Hyderabad, Telangan','9206816717',
 'rawat123@gmail.com','Saroor Nagar',5.0,'MTR1003','2022-01-15'
   ),
   (
   'C1004','Allu Arjun','Flat No. 204, Green Meadows Apartment, Madhapur, Hyderabad, Telangana - 500081','9306823417',
 'alluarjun@gmail.com','Habsiguda',5.0,'MTR1004','2024-06-15'),
  (
   'C1005','Rupesh bhradwaj','H.No. 1-98/7/2, Chanda Naik Nagar, Gachibowli, Hyderabad, Telangana - 500032','8310682341',
 'alluarjun@gmail.com','Medchal',5.0,'MTR1005','2024-01-15');
 



    