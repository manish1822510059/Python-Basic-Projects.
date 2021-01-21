import  random
when = ['A few year','Yesterday','Last night','A long time ago','On 20th jan']
who = ['a rabbit','an elephant','a mouse','a turtile','a cat']
name = ['Ali','Miriam','daniel','hoouk','starwalker']
residence = ['Barcelona','India','Germany','Venice','England']
went = ['cinema','University','seminar','School','Laundary']
happend = ['made a lot of friends','Eats a burger','Found  secret Key','Solved a mistery','Wrote a book']
print(random.choice(when) +' , '+ random.choice(who) +' that lived in '+random.choice(residence)+', when to the '+ random.choice(went)+' and '+random.choice(happend))