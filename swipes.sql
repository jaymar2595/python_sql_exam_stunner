SELECT  first_name, last_name, swiped_on FROM `member` LEFT JOIN swipes ON member.member_id = swipes.member_id WHERE  swipes.granted = 1 and DATE(swiped_on)  ='2015-06-03'