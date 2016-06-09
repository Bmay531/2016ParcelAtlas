#-------------------------------------------------------------------------------
# Name:         Mxd Functions
# Purpose:      Function to set locator frame coordinates
#               Function to export a DDP Mxd to PDF
#
# Author:      BMay
#
#-------------------------------------------------------------------------------
# Import Modules
import arcpy, os
from arcpy import env
arcpy.env.overwriteOutput = True

# Test Variables
gdb = "C:\\AC\\Projects\\2017TaxMaps\\source\\AC_Cadastral.gdb"
ws = "C:\\AC\\Projects\\2017TaxMaps\\build"


Ln = "AC_Splits2016"
uname = "Allegan_Twp"
unum = "02"
unumx = "01"
fld = "ExtraText1"
LayerKey = "Index"
string = "_Index"
fc1 = "AC_Splits2016"
fds1 = "AC_Merge"
Calcfld = "InUnit"
s1 = "Y"
s2 = "N"
#mxda = arcpy.mapping.MapDocument("C:\\AC\\Projects\\2017TaxMaps\\build\\01.mxd")
OutPath = "C:\\AC\\Projects\\2017TaxMaps\\buildTest\\TESTp1"


################################################################################
# Function to set locator frame coordinates
#   Note: The mxd locator frame must be set to automatic for this to work.
################################################################################
def MxdLocExtent(mxd, xMinVal, yMinVal, xMaxVal, yMaxVal):
    #ddp = mxd.dataDrivenPages
    DfLocator = arcpy.mapping.ListDataFrames(mxd,"")[2]
    print DfLocator
    newExtent = DfLocator.extent
    #print newExtent
    #newExtent = "12743225.06 433126.85 12775281.51 465361.67"

    newExtent.XMin = xMinVal
    newExtent.YMin = yMinVal
    newExtent.XMax = xMaxVal
    newExtent.YMax = yMaxVal
    DfLocator.extent = newExtent
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC()
    return mxd
    pass
if __name__ == '__main__':
    MxdLocExtent(mxd, xMinVal, yMinVal, xMaxVal, yMaxVal)





################################################################################
# Function to export a DDP Mxd to PDF
################################################################################
def MxdExport(mxd, OutPath):
    ddp = mxd.dataDrivenPages
    for pageNum in range(1, ddp.pageCount + 1):
        print "Looping"
        ddp.currentPageID = pageNum
        print "pageNum: \n"
        print pageNum
        ##ddp = mxd.dataDrivenPages
        pageID = ddp.pageRow.HOTLINK
        print "pageID: \n"
        print pageID

        OPath =os.path.join(OutPath,pageID)

        #Special handling of first page
        if pageNum == 1:
            Frame = arcpy.mapping.ListLayoutElements(mxd)[7]
            #DynTxt = arcpy.mapping.ListLayoutElements(mxd, "TEXT_ELEMENT", "ParcelPre")[0]
            DfList = arcpy.mapping.ListDataFrames(mxd,"")
            #print DynTxt.text
            #print DfList
            #DfLocator = DfList[2]
            DfLogo = DfList[1]
            #lyrList1 = arcpy.mapping.ListLayers(mxd,"",DfLocator)
            lyrList2 = arcpy.mapping.ListLayers(mxd,"",DfLogo)
            #for lyr in lyrList1:
                #Locator = lyr
                #Locator.visible = False
            for lyr in lyrList2:
                Logo = lyr
                Logo.visible = True

            #DynTxt.visible = False
            arcpy.mapping.ExportToPDF(mxd, OPath)
            #DynTxt.visible = True
            print "Index Printed"
            #Locator.visible = True
            Logo.visible = False
        else:
            pass
            arcpy.mapping.ExportToPDF(mxd, OPath)
            print "page : " + pageID + " printed"
    return mxd
    pass
if __name__ == '__main__':
    MxdExport(mxd,OutPath)


