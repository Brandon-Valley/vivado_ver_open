# vivado_ver_open

After completing the setup below, double clicking a .xpr file will always open the project in the Vivado version it was created from.

This repository uses the [Semantic Versioning Scheme](https://semver.org/).

## Required Software

---

* Python 3.7+
* Vivado (any version)

## Environment variables

---

### **Vivado .bat Path**

The script needs to know the location of the .bat file of the Vivado version the .xpr was created from.

For example, if the file was created in Vivado version 2018.3, it will expect an environment variable called `VIVADO_BAT_PATH_2018_3` to point to the Vivado 2018.3 .bat file.  The path to which may resemble `C:/Xilinx/Vivado/2018.3/bin/vivado.bat`  

Create one of these system environment variables for each installed Vivado version.

## Windows 10 Setup

---

1. Setup the environment variable(s) described above.
2. Set **open_file_in_correct_vivado_version.bat** as the default program to open .xpr files
   1. Find a .xpr file, (created in any Vivado version)
   2. Right click
   3. Open with
   4. Choose another app
   5. Check the **Always use this app to open .xpr files** checkbox
   6. Scroll down and click **More Apps**
   7. Scroll down and click **Look for another app on this PC**
   8. Give the full path to **open_file_in_correct_vivado_version.bat**
   9. **Open**
3. Now, double clicking a .xpr file will always open the project in the Vivado version from which it was created. However, now your .xpr file icon is messed up, so we'll fix that using **FileTypesMan.exe**
    1. Open **file_types_manager\FileTypesMan.exe**
    2. Follow the steps in [this article](https://www.howtogeek.com/75983/stupid-geek-tricks-how-to-modify-the-icon-of-an-.exe-file/) to set the icon for all .xpr files to **imgs\vivado_logo.ico**
    3. After completing the steps outlined in the above article, you must close **FileTypesMan.exe** for the changes to take effect
