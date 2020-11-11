# vivado_ver_open

After completing the setup below, double clicking a .xpr file will always open the project in the Vivado version it was created from.

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

## Setup

---

1. Setup the Environment variable(s) described above.
2. 