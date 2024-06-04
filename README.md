# D2L Fusion 2024 Schedule 

This is a combination or processes using data pulls, reassembling and building a final Excel file.  We are a Microsoft school and I planned this project around that.  I wanted a way for my co-worker and I to plan out which sessions to attend at Fusion and then have an easy way to add it to our calendar.  

## Scripts

I first used a script to scrub the data from the website, then assembled it into an Excel file.  I used another script to remove the AM/PM from the times because only the end letters were being pulled.  For instance 2:15 - 2:55PM would create a calendar item for 2:15am-2:55pm.  I was not able to write a script to adjust for that, I tried many different ways and it wasn't working. Instead of fixing it, the best option was to strip them all out and then add them back using a different code.  I did have to make a couple of manual changes to the file when there was session that spaned between AM and PM but those were minimal.  Once all the AM and PM tags were added, I reran the create-outlook-link file which was 99% was accurate.  Some links do not include the session details and the location isn't imported.  We will call it a work-in-progess script. 

### 1. d2l-session.py
### 2. strip am and pm.py
### 3. add am and pm.py
### 4. create-outlook-link.py
