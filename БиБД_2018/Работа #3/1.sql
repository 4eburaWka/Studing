--create table Table_4 (
--	"� ������" INTEGER PRIMARY KEY,
--	"������������" VARCHAR(50),
--	"�� ���������" VARCHAR(5),
--	"����" INTEGER,
--);

--INSERT INTO Table_4 ("� ������", "������������", "�� ���������", "����") values
--	(1, 'iPhone', '$', 1000),
--	(2, 'Xiaomi', '$', 10),
--	(3, 'Samsung', '$', 1200),
--	(4, 'Redmi', '$', 5),
--	(5, 'Oppo', '$', 600)
--;

select * from Table_4;

select top 3 "������������" from Table_4 order by "������������";

select ������������ from Table_4 where ���� > 100;

select ������������ from Table_4 where ���� between 500 and 1001;

select sum(����) from Table_4;

select min(����) from Table_4;
 
select ������������ from Table_4 where ������������ like 'i%';

update Table_4 set ������������ = 'Huawei' where ������������ = 'Redmi';
select * from Table_4;

--delete from Table_4;
select * from Table_4;
