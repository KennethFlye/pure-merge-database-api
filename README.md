# pure-merge-database-api
API that connects to a PostgreSQL database. The functionality is as follows: Get a specific article based on the articles Id and return it as a JSON object, get all articles and return them as a list of JSON objects, get the next group number that should be used in a merge by selecting the highest value usen in the group column and adding 1 to it, insert an article by sending a JSON object with the same variable names as the article class.

By using this API it makes it possible for multiple UI's to be connected to the same database and saves code duplication. 
