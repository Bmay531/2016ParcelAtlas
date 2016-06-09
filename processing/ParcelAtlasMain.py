#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      BMay
#
# Created:     09/06/2016
# Copyright:   (c) BMay 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Import Modules
import MxdFunctions
import arcpy, os
from arcpy import env
arcpy.env.overwriteOutput = True
fileDir = os.path.dirname(os.path.realpath('__file__'))
print fileDir
PfileDir = os.path.join(fileDir, "../build")
print PfileDir

#Specify the map document
mapPath = os.path.join(fileDir,"AC_ParcelAtlas.mxd")
mxd = arcpy.mapping.MapDocument(mapPath)

# Main Variables #
ws = fileDir
# Data source for the map books #
gdb = "C:\\AC\\Data\\Geodatabases\\AC_Cadastral.gdb"
# List of Unit Numbers #
DocA = os.path.join(fileDir,"Lists\\Unum.csv")
# List of Unit Names #
DocB = os.path.join(fileDir,"Lists\\U_nits.csv")
# List of Locator Frame bounding coordinates
DocC = os.path.join(fileDir, "Lists\\UnitExtent.csv")

# Target FC and FDS vars assigned
fc1 = "AC_Splits2016"
fc2 = "AC_Road_ROWs_Simple"
fc3 = "AC_Subcode"
fc4 = "Orig"
fds1 = "AC_Merge"
fds2 = "Units_Orig"

# Layer wild cards in the template mxd #
LayerKey1 = "Index"

# strings for FC naming #
string1 = "_Index"

# Path for new PDF
OutPath = os.path.join(PfileDir, "Trial1")

# Define local functions
def group(t,n):
    for i in range(0, len(t),n):
        val = t[i:i+n]
        if len(val)==n:
            yield tuple(val)
################################################################################
# Main Starts here
################################################################################
# Create tuple list of units
with open (DocA, 'r') as a:
    ListA = a.read().rstrip()
    ListA = ListA.splitlines()
with open (DocB, 'r') as b:
    ListB = b.read().rstrip()
    ListB = ListB.splitlines()
with open (DocC, 'r') as c:
    stringC = c.read().rstrip()
    # convert to one line string
    SC = stringC.replace("\n",",")
    # convert one line list into 4 item tuples
    NewTup = list(group(SC.split(','),4))
    # unzip each element of the tuples into separate lists
    xMin = list(zip(*NewTup)[0])
    yMin = list(zip(*NewTup)[1])
    xMax = list(zip(*NewTup)[2])
    yMax = list(zip(*NewTup)[3])
Tuple1 = zip(ListA, ListB, xMin, yMin, xMax, yMax)
print Tuple1

mxd.dataDrivenPages.refresh()

"""
# Iterate list to produce tax maps
for tup in Tuple1:

    # Refresh DDP
    mxd.dataDrivenPages.refresh()
    print "     Unit Number / Name to be processed into a tax map book:    "
    print tup
    # Unit Number assigned
    unum = tup[0]
    # Unit Name assigned
    uname = tup[1]
    unumx = "01"
    xMi = float (tup[2])
    yMi = float (tup[3])
    xMa = float (tup[4])
    yMa = float (tup[5])
    print xMi
    print "Data for unit:   " + uname + " is now being processed"

    # Refresh DDP
    mxd.dataDrivenPages.refresh()

    # Set extent of locator frame
    MxdFunctions.MxdLocExtent(mxd,xMi, yMi, xMa, yMa)

    # Refresh DDP

    mxd.dataDrivenPages.refresh()

    #Export new mxd to PDF
    MxdFunctions.MxdExport(mxd,OutPath)

    del mxd"""