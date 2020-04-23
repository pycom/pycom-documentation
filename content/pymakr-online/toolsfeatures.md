---
title: "Tools/Features"
aliases:
    - pymakr/toolsfeatures.html
    - pymakr/toolsfeatures.md
    - chapter/pymakr/toolsfeatures
---

There are two different ways of opening Pymakr Online. Each way has some differences on the features and purposes. Read more at [How to Open Pymakr Online](/pymakr-online/how-to-open)

# Pymakr Online linked to a device

If you open Pymakr Online from a device page, Pymakr will be linked to that device.

_**Note: Your device needs to be online in order to be reachable by Pymakr Online**_

## Terminal

just like Pymakr Plugin, Pymakr Online also has a REPL (Read Evaluate Print Line) terminal. The REPL allows you to run code on your device, line by line. To begin coding, open Pymakr from a device (device's page > pymakr tab > open Pymakr button), go to the terminal and start typing your code. 


## Download a file

When Pymakr is loaded, the IDE will request the device its hierarchy (the folder structure). If you open a file that has never been opened in Pymakr Online before, that file's content will be downloaded and saved on the cloud, so the next time you open that same file, the content download won't be necessary, unless you want to. Maybe you changed that file's content in somewhere else and want to force a download to get the current content which is in the device. 

To download the file from the linked device, click on the download icon next to the file name at file tree.

![](/gitbook/assets/pymakr-online/pymakr-download-icon.jpg)

That will download the file content from the device and save it into the cloud.

![](/gitbook/assets/pymakr-online/last-update-one-day-ago.jpg)

*In this case, that file has been updated yesterday.*

![](/gitbook/assets/pymakr-online/last-update-few-seconds-ago.jpg)

*After downloading the main.py content from the device.*

## Upload a file

After making any changes in a file, you will be able to upload it into your device by clicking on "Save and Upload" link.

![](/gitbook/assets/pymakr-online/save-upload.jpg)


_**Note: That will upload only the current file.**_

After downloading or uploading a file, its content is stored on the cloud.

## Update Hierarchy

If you want to refresh your device's hierarchy in Pymakr, you should click on Refresh Hierarchy icon next to your device name. That will request the hierarchy from the device, creating or deleting folders according to your device's file hierarchy. 

![](/gitbook/assets/pymakr-online/pymakr-hierarchy.jpg)


# Pymakr Online not linked to a device

Pymakr Online can be opened without being linked to a device, from [Pymakr Online](https://www.pybytes.pycom.io/pymakr) initial page.

Since there's no device linked in this way of opening Pymakr Online, there are no device related actions here (download file, device activity indicator etc). Instead, you decide what you are going to do with your code: upload to a project, download a zip file or upload to a device.

Before exporting your project, you first need to import a project into Pymakr or start with a blank project:

## Import code into Pymakr Online

![](/gitbook/assets/pymakr-online/pymakr-online-initial-page.jpg)

*Pymakr Online initial page*

### 1. Blank project

This will open Pymakr Online with the essential files of Micropython project (main.py and boot.py).

### 2. Project/Release

1. After clicking on Project button, you will see this page, where you must choose one project:

![](/gitbook/assets/pymakr-online/pymakr-projects.jpg)

2. And finally, choose the release you want to work with. That will open Pymakr with the files of the selected release.

![](/gitbook/assets/pymakr-online/pymakr-releases.jpg)

### 3. Device

At this section you can import the code from a device and work with it in Pymakr Online. Note this won't have any connection to any device once it's loaded. 

1. Choose the device you want to work with: 

![](/gitbook/assets/pymakr-online/pymakr-devices.jpg)

2. If you already worked with that device in Pymakr Online, you can use the latest saved code on the cloud, so the device doesn't need to be online, or even turned on. That will instantly open Pymakr with that code.


![](/gitbook/assets/pymakr-online/pymakr-device-import-1.jpg)


If you want the current files from the device and you are not sure if the saved code on the cloud is up to date, you can download those files from the device by clicking on "Request files from device" button. That will bring you to another modal, which will show you the download progress.

![](/gitbook/assets/pymakr-online/pymakr-device-import-2.jpg)

Once the download has been completed, you can now work with the device's files in Pymakr Online:

![](/gitbook/assets/pymakr-online/pymakr-device-import-3.jpg)!


### 4. Zip file (soon)

Still under development, this feature allows you to upload a zip file of your project into Pymakr Online and start to work with it from there. 

### 5. Github Repository

1. Firstly, type the repository name you want to import your code from and press enter:

![](/gitbook/assets/pymakr-online/pymakr-github-import-1.jpg)!

2. Then select your repository by clicking on it.

![](/gitbook/assets/pymakr-online/pymakr-github-import-2.jpg)!

3. Select the branch 

![](/gitbook/assets/pymakr-online/pymakr-github-import-3.jpg)!

4. Wait for a few seconds until the download of the files from the selected branch is completed and then you can start working on Pymakr with those files!

![](/gitbook/assets/pymakr-online/pymakr-github-import-4.jpg)!

_**Note: There's a usage limit of the Github API. You won't be able to search a lot and select different repositories in the same day. Use this feature with moderation.**_


## Save/Export

To export your project, ensure that you have opened Pymakr Online from the Pymakr initial page (accessible from the sidebar menu) and not from the device page. For any option here, the size limit is 4MB. 

1. Click on Save/Export button.

![](/gitbook/assets/pymakr-online/pymakr-export.jpg)

2. Choose an option:

![](/gitbook/assets/pymakr-online/pymakr-export-modal.png)

* Upload to a project will be released soon.

* Create and Download a zip file from all of the files from your project.

![](/gitbook/assets/pymakr-online/pymakr-download-zip.jpg)

* You can also export to a device. This modal will open after clicking on "UPLOAD TO DEVICE" button. Note that your device needs to be online in order to receive the files from Pymakr Online.

![](/gitbook/assets/pymakr-online/pymakr-devices-list.jpg)

* Wait while Pymakr Online is uploading your project to the selected device.
![](/gitbook/assets/pymakr-online/pymakr-upload.jpg)

* Once the upload is done, your device will restart and load the new code.
![](/gitbook/assets/pymakr-online/pymakr-download-completed.jpg)





