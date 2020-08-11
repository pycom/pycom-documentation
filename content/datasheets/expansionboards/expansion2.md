---
title: "Expansion Board 2.0"
aliases:
    - datasheets/boards/expansion2.html
    - datasheets/boards/expansion2.md
    - product-info/boards/expansion2
    - chapter/datasheets/boards/expansion2
---
**Store**: Discontinued, See [Expansionboard 3.0](../expansion3)

![](/gitbook/assets/expansion2.png) 


## Datasheet

The datasheet of the Expansion Board is available as a [PDF File](/gitbook/assets/expansion2-specsheet.pdf)

[ROHS certification](/gitbook/assets/RoHs_declarations/RoHS-for-Expansion-Board(8286-00033P)-20190523.pdf)


## Pinout

The pinout of the Expansion Board is available as a [PDF File](/gitbook/assets/expansion2-pinout.pdf)


![](/gitbook/assets/expansion2-pinout-1.png)

{{% hint style="danger" %}}
Be gentle when plugging and unplugging from the USB connector. Whilst the USB connector is soldered and is relatively strong, if it breaks off it can be very difficult to fix.
{{% /hint %}}

## Notes 
### Battery Charger

The Expansion Board features a single cell Li-Ion/Li-Po charger. When the board is being powered via the micro USB connector, the Expansion Board will charge the battery \(if connected\). When the `CHG` jumper is present, the battery will be charged at `450mA`. If this value is too high for your application, removing the jumper lowers the charge current to `100mA`.
