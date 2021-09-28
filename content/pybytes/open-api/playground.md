### The Playground

You can access the Open APIs playground following this link  **https://open-api.pybytes.pycom.io/graphql**.
This GraphQL interface will help you to test the Pybytes Open APIs.

Under the **DOCS tab** on the right part of the screen, you will find the list of Open APIs.
Under the **SCHEMA tab**, you will learn the general Scheme for the Pybytes Open APIs.

If you want to get more information about precesses in  GraphQL, please, visit this [link](https://graphql.org/learn/).

This interface is a place where you can test the API without setting the environment.
**Queries** and **Mutations** will already be at your disposal to be used and tested.
![](/gitbook/assets/open-api/graphql/open-api-graphql.png)

### How to test Open APIs 

First of all, you should authorize with the token that you saved during the [previous step](https://docs.pycom.io/pybytes/open-api/gettingstartedopenapi/).

1. On the playground open the HTTP Headers tab at the bottom of the screen 
![](/gitbook/assets/open-api/graphql/graphql-headers.png)


2.  Past the token string following this format 

	{ 

		"Authorization": " Bearer your Token" 

    } 


3. Now you can try to send the Query or Mutation request for a certain API function, for instance, getAllWifi query. 
After pressing the play **button** you will see the list of all wi-fi networks on the right frame of the playground   

![](/gitbook/assets/open-api/graphql/graphql-play.png)