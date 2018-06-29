# LoPy Tutorials
The following tutorials demonstrate the use of the LoRa functionality on the LoPy. LoRa can work in 2 different modes; **LoRa-MAC** (which we also call Raw-LoRa) and **LoRaWAN** mode.

LoRa-MAC mode basically accesses de radio directly and packets are sent using the LoRa modulation on the selected frequency without any headers, addressing information or encryption. Only a CRC is added at the tail of the packet and this is removed before the received frame is passed on to the application. This mode can be used to build any higher level protocol that can benefit from the long range features of the LoRa modulation. Typical uses cases include LoPy to LoPy direct communication and a LoRa packet forwarder.

LoRaWAN mode implements the full LoRaWAN stack for a class A device. It supports both OTAA and ABP connection methods, as well as advanced features like adding and removing custom channels to support "special" frequencies plans like the those used in New Zealand.
