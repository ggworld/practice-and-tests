--Write a query that lists all colleges that have at least one student with a ranking between 1
--and 3 (both inclusive), for the year 2015. The query should return:
--The college name.
--The rank of their best ranking student for 2015.
--The number of students who had rankings between 1 and 3 (both inclusive) for the---
--year 2015.
--Rank 1 is the best rank, rank 2 the second-best, and so on. More than one student can tie
--for a rank in a year.


 select c.name Name, min(ranking) TopRank,count(r.studentId) NumberOfStudents
 from colleges c left join students s on c.id = collegeId
 left join rankings r on r.studentId = s.id
 and year=2015 and ranking between 1 and 3
 group by c.name 
 having NumberOfStudents > 0
 order by 2 
