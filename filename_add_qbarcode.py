#!/usr/bin/env python

import os
import sys

def getBarcodeAndFileNames(tsvFile):
        fileBarcodeMap = {}
        with open(tsvFile) as fh: content = fh.readlines()[1:]
        for line in content:
                splittedContent = line.split("\t")
                fileBarcodeMap[splittedContent[1]] = splittedContent[0]
        return fileBarcodeMap

def renameFileWithBarcode(rootDir, fileName, qbicCode):
        if not qbicCode:
                return
        # os.rename(os.join(rootDir,fileName), os.join(rootDir, "{0}_{1}".format(qbicCode, fileName)))
        print "renamed file to:{0}{1}_{2}".format(rootDir, qbicCode, fileName)

def moveFiles(rootDir, fileList, barcodeAndFilesMap):
        for afile in fileList:
                renameFileWithBarcode(rootDir, afile, barcodeAndFilesMap.get(afile))

def main(tsvFile):
        barcodeAndFilesMap = getBarcodeAndFileNames(tsvFile)
        for root, _, files in os.walk('./'):
                moveFiles(root, files, barcodeAndFilesMap)


if _name_ == "_main_":
        tsvFile = sys.argv[1]
        main(tsvFile)