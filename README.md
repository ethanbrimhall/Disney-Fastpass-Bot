# Disney-Fastpass-Bot

This code automates the task of finding a fastpass on the Disney World website for any of the 4 Orlando parks.

User Steps:
1. First you select a park
2. Then you select a ride
3. Then you select a time
4. Then you pick AM or PM
5. After that it take you in to the site, using chromedriver
6. Then it signs you in, selects everyone in your party, and takes you to the date screen
7. Manually pick a date, then sit back and watch it go to work
8. It searches for the ride until it finds it, by going through morning, afternoon, then evening time frames

For more information on how it works visit: https://www.youtube.com/watch?v=KRa-ZjGLppg&t=9s

HOW TO RUN THE CODE:

Before running the code, you must put your username and password into the code, there will be comments to help
Next you must put the guest id of each person in the code as well...
...To do that you must go to the "Create FastPass+ Party" page and inspect element
Find and click on each guest's name with inspect element and click copy their xpath and paste in the code
After that you are finished and can run the code
