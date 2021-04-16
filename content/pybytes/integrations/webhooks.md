---
title: "Webhooks"
aliases:
    - pybytes/integrations/webhooks.html
    - pybytes/integrations/webhooks.md
---

Whenever one of your integrated devices sends a signal to Pybytes, we perform an HTTP request defined by the user.
You can use some presets (`DEVICE_TOKEN`, `USER_ID`, etc), which will act like placeholders and will be dynamically replaced at the moment of performing the request with the relative content.

## Integrate your devices

1. In the sidebar, click on _Integrations_, _New Integration_ and then on _Webhook_

![New WebHook integration](/gitbook/assets/pybytes/integrations/webhook/select-webhook-integration.png)

1. Fill in the form specifying the following information: (for this example, you can leave the default settings)
    * The remote URL to which we will send the data, in this example, we will use a custom URL generated on [webhook.site](https://webhook.site/), paste `Your unique URL` in the textbox.
    * An event name
    * The HTTP method
    * The request format. Please note that we will pre-fill some headers whenever you change the format. The pre-filled headers are not modifiable.
    * You can optionally add some more headers and query parameters. There's also an eased interface for basic HTTP authentication.

2. We will take care of formatting the body accordingly to the chosen request format. In case you've chosen _Custom Body_, you'll have to define everything yourself. You'll also be able to manually insert the presets.

![Webhook definition](/gitbook/assets/pybytes/integrations/webhook/webhook-form.png)

3. Once you're done, you'll see a preview of the request at the bottom of the page. Remember to choose the devices you want to bind to this service.

4. If everything's worked as expected, you should be able to see a summary of your integration, similar to the following:

![Creation process result](/gitbook/assets/pybytes/integrations/webhook/webhook-inspector.png)

5. Setup the selected device to [Visualize signals](/pybytes/dashboard/) and view the webhook site you generated. If all went correctly, you should see the samples arrive there:

![](/gitbook/assets/pybytes/integrations/webhook/webhook-view.png)

Now you should be able to adjust the settings and forward the data to your own service or app and work with the Pybytes signals