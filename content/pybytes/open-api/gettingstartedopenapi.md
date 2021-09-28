### Creating Personal Access Token (PAT)

1. Log into [Pycom](https://sso.pycom.io/) and go to the Account Settings.

![](/gitbook/assets/open-api/token/login-settings.png)



2. Open the Token tab and add a new Token.

![](/gitbook/assets/open-api/token/token-page.png)



3. In the Add Token modal window, you have to select the **scopes** which you would like to access with the Pybytes Open APIs.


    ### Capabilities
    You will have the choice between different access level.
    You will also need to select a Read-only or Write-only accessibility level for each data type.
    You may set the **Read** and **Write** Scope for a **User**, **Devices**, **Network Settings**, **Projects** or 
    **Releases**.
    This will determine what a User, Device, Network, Setting, Project or Release can and can't do when logged in with the particular Token.

![](/gitbook/assets/open-api/token/token-settings.png)



### Security
Bear in mind! Each **Token** is unique and can be exposed only once after generation. So be sure that you copied the Token and saved it. Otherwise, you would need to repeat the creation of the PAT again.

![](/gitbook/assets/open-api/token/token-security.png)


