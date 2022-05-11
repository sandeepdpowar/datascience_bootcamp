# datascience_bootcamp
# Assignment - Module 1

## Overview of the project:

The purpose of this project is to analyze the Theatre campaign outcomes based on the launch dates and their funding goals.


## Analysis and Challenges:

### Overview:
The analysis done based on the **“Theatre_Outcomes_vs_Launch.png”** chart we can state that most of the Theatre campaigns were launched in the months of May-June, whereas Least number of Plays were launched in December months. 

Based on the analysis done on **“Outcomes_vs_Goals.png”** chart we can conclude that plays with Goal amounts less that 1000 were more successful, whereas campaigns with goals between 45000 to 49999 range were failed.

### Challenges:
Launch date data in the **‘Kickstarter’** data set was in in Unix date format it was needed to be converted to normal mm-dd-yy format to calculate the Theatre campaigns based on Launch dates, it was converted to regular date using excel formaula - “=(cell_number/86400)+DATE(1970,1,1)” 

## Results:
Theatre outcome by launch dates:
1. According to the **'Theatre_Outcomes_vs_Launch.png'** graph, the most theater campaigns were introduced in the months of May and June, with 67% of them succeeding, 31% failing, and 2% being cancelled. 
2. The least number of Theatre campaigns launched were in the month of December with stats - 37% percent successful, 35% Failed and 3% canceled.


## Outcomes based on Goals:
1. According to the **“Outcomes_vs_Goals.png”** chart maximum number of plays were between goals with range of <=$1000 and $9999, which also had good success rate and less failure rate.
2. The Plays count decreased as the goal amount increased, from the range $10000 to $50000 or more”, with less success rate and higher failure rate.


## Summary:
This analysis can conclude that Theatre which were launched during the months of May-June with highest number of success were with the goal amount between “<=$1000 to $9999”.
