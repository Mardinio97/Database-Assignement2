
drop database if exists reddit3 ;

create  database  reddit3 ;

use reddit3;


DROP TABLE IF EXISTS `Subreddit`;

CREATE TABLE `Subreddit` (
  `id` varchar(250) primary key NOT NULL,
  `name` varchar(250) NOT NULL unique
) ;



DROP TABLE IF EXISTS `Link`;


CREATE TABLE `Link` (
  `id` varchar(250) primary key NOT NULL,
  `subreddit_id` varchar(250) NOT NULL,
 constraint FOREIGN KEY (subreddit_id)
     references subreddit(id) on delete cascade on update cascade
) ;


DROP TABLE IF EXISTS `Comment`;
DESCRIBE  subreddit ;




CREATE TABLE `Comment` (
  `id` varchar(250) PRIMARY KEY NOT NULL,
  `author` varchar(250) NOT NULL,
  `score` int(11) NOT NULL,
  `body` varchar(9900) NOT NULL,
  `subreddit_id` varchar(250) NOT NULL,
  `parent_id` varchar(250) NOT NULL,
  `created_utc` timestamp NOT NULL DEFAULT NOW()  ,
  `link_id` varchar(250) NOT NULL,
   constraint `FK_subreddit_id`  foreign key (subreddit_id)
       references Subreddit(id) on delete cascade on update cascade
) ;

CREATE INDEX COMMENT_idx ON Comment (author);
CREATE INDEX subreddit_idx ON comment (subreddit_id);
CREATE INDEX subredditID_idx ON subreddit (id);


/*
select  count(id) from comment where author = 'postullo';
select count(*) as commentsPerDay , created_utc as date from  comment, subreddit where created_utc ='2007-10-01 03:00:24' and  subreddit_id = 't5_2fwo'




SELECT author, COUNT(*) AS COUNTsubreddit_id
from COMMENT GROUP BY author HAVING COUNT(COUNTsubreddit_id)
= 1

DROP  PROCEDURE IF EXISTS usersHL;

DELIMITER ;

DELIMITER //

CREATE PROCEDURE usersHL()

BEGIN
 declare max int;
 declare min int;


set  max =(select   SUM(SCORE)
from comment
where row(author, score) in
(
    select author, MAX(score)
    from comment
    group by author
)
group by score order by score desc  limit 1);


set min = (select  SUM(SCORE)
from comment
where row(author, score) in
(
    select author, MAX(score)
    from comment
    group by author
)
group by score order by score asc limit 1);

 select concat('Min : ',min,' Max: ',max);


END //

call usersHL()

set @lowSubId = (select name from Subreddit
where id = (select subreddit_id from comment where score =
(SELECT MIN(score) as Minimum from Comment)));


set @maxSubId = (select subreddit_id from comment where score =
(SELECT MAX(score) as Maximum from Comment));


SELECT CONCAT('highest ', (name), ', lowest ', (select @lowSubId)) from subreddit  where id = (select @maxSubId);

show indexes from Comment;
show indexes from Subreddit;
show indexes from Link;
*/