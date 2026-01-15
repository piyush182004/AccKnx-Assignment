
The objective of this problem is used to save the book information data in the sqlite.I am assuming the as said in the problem to use any external Rest API,I will use publicly available api of the OpenLibrary as the information required is available there and also for the information i used some search engines instead of blind copy paste.I will break the problem codebase into multiple modules
the pipeline that this follows is fetches data,stores it in database and then displays
api_client.py:- connecting external api and normalising the information in data manner
database.py-managing database operations
main.py-the main module controlling flow of operation

