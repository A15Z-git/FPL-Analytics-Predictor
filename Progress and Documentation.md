Progress:
3/26-I have done some basic stuff till now such as making the dataframe of relevant players, gathering top 11 players in the season, and top 11 per gameweek.
I have also so created a player class to contain relevant data.

I decided to include status column in my DataFrame. Did not include chance of playing since lot of rows had no entry and it seemed as tho status did enough.
Pricing details (from raw players) seem complicated so I will work on them later.

Defensive contributions do play a good role in the latest season however since it was JUST introduced I cannot apply it to previous seasons.
If I decide to implement it live I will use data from 25-26 to create a metric and implement it for 26-27. Skipping for now.

3-30 and parts of April I did some very minor stuff, such as analyzing the database in more detail, figuring out stats, and adding in player availability.


8/6-After long break I am back. I WILL have a working model by FPL start date.

After some thinking and cross checking (thanks Claude) I realized the optimal way to do my original plan would lead to something like (score = 0.4 × z(goals) + 0.4 × z(assists) + 0.2 × z(CS))

This is essentially a linear regression equation so it would be nice to how it compares to build in LR models (it might even be same idk).

I also scraped through the data and found some extra info I would need from extra csv outside my base. Some notes on a few variables I am unsure about

-The per 90 is annoying. Efficiency is important but results more so, as I do not really care about the most efficient players necessarily but the best players. However efficiency can be important as an player who is amazing but got injured mid season would still be really good. However, they may still be effected by injury so idk a lot to consider I cannot exactly quantify. If I do use efficiency I think I will have minimum standards for a player to pass my pick screening, but then that introduces problem of new transfers. My thought process is perhaps use player value as another metric that could pass the screening. A young rookie player who is getting more minutes is unlikely to become an immediate breakout star, but an expensive signing will surely get game time despite being new.
