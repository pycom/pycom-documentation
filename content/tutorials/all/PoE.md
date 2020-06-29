---
title: "PoE"
aliases:
    - tutorials/all/PoE.html
    - tutorials/all/PoE.md
    - chapter/tutorials/all/PoE
---

![](/gitbook/assets/PoE-NI.png)

Before you use the PoE adapter for the first time, please make sure you follow the below instructions as failure to do so might damanage your devices!

The PyEthernet module offers an optional onboard Power over Ethernet (PoE) power supply circuit. This means that you can power your hardware with only an ethernet cable coming from a power injector or PoE enabled Ethernet switch. However, since the PoE is non-isolated, you must adhere to the following warning!

{{% hint style="danger" %}}
WARNING: Before you use the PoE adapter for the first time, please make sure you read and follow the below instructions as failure to do so might damanage your devices!
{{% /hint %}}

<h3>Setup Options</h3>

<table >
	<tbody>
		<tr>
			<td> Connectivity option</td>
			<td> Power over Ethernet</td>
			<td> Power over USB/Battery only</td>
		</tr>
		<tr>
			<td> USB-C cable connected to a PC with mains ground</td>
			<td> NOK</td>
			<td> OK</td>
		</tr>
    <tr>
			<td> USB-C charger not connected to mains ground</td>
			<td> OK</td>
			<td> OK</td>
		</tr>
    <tr>
			<td> USB-C cable connected to a Notebook without mains ground</td>
			<td> OK</td>
			<td> OK</td>
		</tr>
		<tr>
			<td> Battery</td>
			<td> OK</td>
			<td> OK</td>
		</tr>
		<tr>
			<td> oscilloscope / Logic Analyser / Other testequipment</td>
			<td> NOK</td>
			<td> OK</td>
		</tr>
	</tbody>
</table>

The PoE power supply integrated in the PyEthernet module has no galvanic isolation. This means that in accordance with
IEEE 802.3-2005 standard, you must <b>not</b> connect any other devices / cables / chargers if the GND connection is connected to mains earth.
This is typically the case with PCs, Oscilloscopes, Logic Analysers, current measurement devices etc.

Incorrect usages of Power over Ethernet can lead to unrecoverable damage of not only the PyEthernet module but all hardware connected to it.
