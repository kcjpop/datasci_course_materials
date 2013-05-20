-- select count() from (select docid from Frequency group by docid having sum(count) > 300);
--
-- problem 3
--
-- create view v1 as select a.*
-- from (select * from Frequency where docid = '10080_txt_crude') as a,
-- (select * from Frequency where docid = '17035_txt_earn') as b
-- where a.term = b.term
-- union
-- select b.*
-- from (select * from Frequency where docid = '10080_txt_crude') as a,
-- (select * from Frequency where docid = '17035_txt_earn') as b
-- where a.term = b.term;
--
-- select v1.docid, v1t.term, sum(v1.count * v1t.count) from v1, v1t where v1.term = v1t.term group by v1.docid, v1t.docid;


create view f as SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count;

create view f1 as select a.*
from Frequency as a, (select * from f
where docid = 'q') as b
where a.term = b.term
union
select b.*
from Frequency as a, (select * from f
where docid = 'q') as b
where a.term = b.term;

select f1.docid, sum(f1.count * f1t.count) from f1, f1t where f1.term = f1t.term and f1t.docid = 'q' group by f1.docid, f1t.docid order by sum(f1.count * f1t.count);