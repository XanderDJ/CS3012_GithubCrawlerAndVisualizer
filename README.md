#CS3012 Final assigment
##Setup
make sure that the newest versions of python and node.js are installed.
<br />pip install pymongo
<br />pip install pygithub
<br />npm install express
<br /> make credentials.txt with github username on the first line and password on the second
##github crawler
The githubcrawler I created uses mongodb and starts from your own username.
It gathers all your collaborators and then starts from there.
after you've gathered enough usernames, you get all the repositories from them
after you've gathered all the repositories you gather the languages of these repositories.
>python GetUsersGithub.py
><br />python getRepositoriesFromUsers.py
><br />python getLanguagesOfRepository.py
><br />python getJSON.py to gather the necessary information for the charts

##visualisation

To run the visualisation, the only thing you have to do is to run the local server with node.js
