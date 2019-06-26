# Amazon IoT

Whenever one of your integrated devices sends a message to our broker, we republish the binary payload to the endpoint specified for its integration.

## Integrate your devices <a id="integrate-your-devices"></a>

1. Go in the sidebar, click on _New Integration_ and then on _Amazon Web Services_

![](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LIL0iGdl11z7Jos_jpX%2F-LQ-UAflx-H1r4pkZhzv%2F-LQ-Uat_I9wiYDBCpz_K%2F01_aws_integration.png?alt=media&token=ed8a7737-e0e8-42fc-83a5-8fddffaa3316)

1. Fill in the form choosing an [AWS region](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) and your AWS credentials. You can optionally choose to save them inside the local storage for future use. Once you're done, click _Login_

![](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LIL0iGdl11z7Jos_jpX%2F-LQ-UAflx-H1r4pkZhzv%2F-LQ-UkDEF_fpCDq7bw2Y%2F02_aws_integration.png?alt=media&token=7f9ab8ae-fc98-47fb-a84a-681a0b83d008)

1. In this step, you have to specify the [AWS group](https://docs.aws.amazon.com/iot/latest/developerguide/thing-groups.html) name \(just alphanumeric letter, dashes and underscore are allowed\), the custom topic and the devices you want to bind to AWS. When you're ready, click _Create_

![](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LIL0iGdl11z7Jos_jpX%2F-LQ-UAflx-H1r4pkZhzv%2F-LQ-Uo4CkJdFy3JPbh91%2F03_aws_integration.png?alt=media&token=a3589c47-c77c-4f91-9675-a25ba6d89208)

1. If everything's worked as expected, you should be able to see a summary of your integration like the following:

![](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LIL0iGdl11z7Jos_jpX%2F-LQ-UAflx-H1r4pkZhzv%2F-LQ-UqcDBS4h1BTCqWiZ%2F04_aws_integration.png?alt=media&token=3847a597-83b1-4ddd-a2c9-7d3f6948c4d3)

1. The corresponding AWS Thing and AWS Group has been created as well, you just have to [log in to the console](https://console.aws.amazon.com/console/home?nc2=h_ct&src=header-signin) and choose the same region of your devices from the topbar. You'll be able to explore groups and things' details.

![](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LIL0iGdl11z7Jos_jpX%2F-LQY9TjXsTcZzaZ7pMS0%2F-LQY9Yf2cyvfHAJYQcUM%2F05_aws_integration.png?generation=1541409488774926&alt=media)

1. The device's name is specified as an attribute of the thing.

![](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LIL0iGdl11z7Jos_jpX%2F-LQY9TjXsTcZzaZ7pMS0%2F-LQY9Yf5HQWCqCsWEQwo%2F06_aws_integration.png?generation=1541409488706134&alt=media)

## Final considerations <a id="final-considerations"></a>

In order to save the data received by AWS, [you must set up a rule](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html). You can also test that everything's working with the [AWS IoT MQTT client](https://docs.aws.amazon.com/iot/latest/developerguide/view-mqtt-messages.html). Please notice that it's not possible to download the private key from AWS once it has been generated, by the way we securely store it inside our database. We may consider to allow its download in the future, so that you could also directly send your device to AWS, by passing Pybytes.

**Warning**: do not delete AWS things or groups directly from AWS user interface, otherwise the integration with Pybytes will stop working. Always use Pybytes interface to delete AWS things or groups.

