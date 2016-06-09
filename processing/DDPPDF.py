#-------------------------------------------------------------------------------
# Name:        Data Driven Pages PDF Printer
# Purpose:
#
# Author:      BMay
#
# Created:     23/11/2015
# Copyright:   (c) BMay 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


#You can also use python in conjunction with data driven pages to cycle through each page,
#and perform one of the many operations supported by arcpy.mapping. For example, you can update a layer?s
#symbology, update some layout text, and export or print each map.

import arcpy
import os

fileDir = os.path.dirname(os.path.realpath('__file__'))
print fileDir

#Specify the map document
mapPath = os.path.join(fileDir,"AC_ParcelAtlas.mxd")
mxd = arcpy.mapping.MapDocument(mapPath)

i= 0

#Export each of the data driven pages

for pageNum in range(1, mxd.dataDrivenPages.pageCount + 1):
    mxd.dataDrivenPages.currentPageID = pageNum
    i=i+1
    ddp = mxd.dataDrivenPages
    #pageID = ddp.getPageIDFromName(MAPPING_ID)
    pageID = ddp.pageRow.MAPPING_ID

    print pageID
    print "Exporting page {0} of {1}".format(str(mxd.dataDrivenPages.currentPageID), str(mxd.dataDrivenPages.pageCount))
    ##parcelnum = mxd.dataDrivenPages.pageRow.Name
    ##print parcelnum
    pdfLocation = os.path.join(fileDir, '../build')
    newPdf = os.path.join(pdfLocation, pageID + ".pdf")
    arcpy.mapping.ExportToPDF(mxd, newPdf)
    if i > 100:
        break
del mxd

