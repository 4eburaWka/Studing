--create table Table_4 (
--	"№ товара" INTEGER PRIMARY KEY,
--	"наименование" VARCHAR(50),
--	"ед измерения" VARCHAR(5),
--	"цена" INTEGER,
--);

--INSERT INTO Table_4 ("№ товара", "наименование", "ед измерения", "цена") values
--	(1, 'iPhone', '$', 1000),
--	(2, 'Xiaomi', '$', 10),
--	(3, 'Samsung', '$', 1200),
--	(4, 'Redmi', '$', 5),
--	(5, 'Oppo', '$', 600)
--;

select * from Table_4;

select top 3 "наименование" from Table_4 order by "наименование";

select наименование from Table_4 where цена > 100;

select наименование from Table_4 where цена between 500 and 1001;

select sum(цена) from Table_4;

select min(цена) from Table_4;
 
select наименование from Table_4 where наименование like 'i%';

update Table_4 set наименование = 'Huawei' where наименование = 'Redmi';
select * from Table_4;

--delete from Table_4;
select * from Table_4;
