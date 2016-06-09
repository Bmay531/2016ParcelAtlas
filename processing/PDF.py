###-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      BMay
#
# Created:     23/11/2015
# Copyright:   (c) BMay 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import arcpy, os

arcpy.env.workspace = ws = "C:\Data\MXDs\Production"

mxd_list = arcpy.ListFiles("*.mxd")

print mxd_list

for mxd in mxd_list:

    current_mxd = arcpy.mapping.MapDocument(os.path.join(ws, mxd))
    pdf_name = mxd[:-4] + ".pdf"
    arcpy.mapping.ExportToPDF(current_mxd, pdf_name)

del mxd_list
