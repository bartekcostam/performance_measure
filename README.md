# performance_measure

## Running the program
- Normal startup - type in terminal: ```python3 main.py``` <br />
- Test mode (url and xpath assured) - type: ```python3 main.py testing```
##
![Roadmap of our project](https://github.com/bartekcostam/performance_measure/assets/139556566/4c1353b4-7a54-4aac-b25a-d934d755a391)


##How to use it

Basic tab: 

-Run the program and provide url for certain page you want to test, keep in mind to add full url path with protocol (http,https)

-Set the number of tests you want to run (more -> better) by default it will run 5 times 

-Click 'start test' button to start testing, if all is good you should see a chrome window showing and disappearing during running tests

-If you want to hide chrome window then you can simpli select checkbox to run the tests in headless mode so all work will be done in the console but with the same results. 

On the left hand side you can select the speed of the internet you want to simulate during the test, it may be helpful. 

When all the test are finished you can click the button to see the diagram which gonna representate the avg times for selected page and the element of the page. 

Advance tab:

*You can set a DB connections there to make tests even better 
*Input box to run the sql query for coparing the data from DB and frontend of the page you testing

Additional tab: 

*Generate a bot to check if your pages are online and whats the conditions of the internet speed. 

*Install chrome extension to transfer xpath and url from the page you currently browsing

*