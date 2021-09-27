### The Playground

This interface is a place where you can test the API without setting the environment.
**Queries** and **Mutations** will already be at your disposal to be used and tested.
![](/gitbook/assets/open-api/graphql/open-api-graphql.png)



### How to Access it

Once you have run your stack, you can access it through **https://open-api.pybytes.pycom.io/graphql**

### Authentification 

At the bottom of the page you will have a bottom bar with the **Query Variables** and the **HTTP Headers**. You can click on it to open it.
![](/gitbook/assets/open-api/graphql/header-bar-closed.png)

Once it is open go to the **HTTP Headers** section.
![](/gitbook/assets/open-api/graphql/header-bar-open.png)

This is where you are gonna use your **Token** to authentificate yourself.

First between curly brackets enter **"authorization": "bearer "**.
Do not forget to put a **space** after **bearer** then paste your **Token**.
![](/gitbook/assets/open-api/graphql/header-bar-filled.png)