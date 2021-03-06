#!/usr/bin/python

__author__ = 'hcaesar'

# Shows how to use the evaluation script of the Stuff Segmentation
# Challenge.
#
# This script takes ground-truth annotations and result
# annotations of a semantic segmentation method and computes
# several performance metrics. See *cocostuffeval.py* for more
# details.
#
# Microsoft COCO Toolbox.      version 2.0
# Data, paper, and tutorials available at:  http://mscoco.org/
# Code written by Piotr Dollar and Tsung-Yi Lin, 2015.
# Licensed under the Simplified BSD License [see coco/license.txt]

from pycocotools.coco import COCO
from pycocotools.cocostuffeval import COCOStuffeval

def pycocostuffEvalDemo(dataDir='../..', dataType='train2017', resType='examples'):
    '''
    Shows how to use the main evaluation script of the Stuff Segmentation Challenge.
    :param dataDir: location of the COCO root folder
    :param dataType: identifier of the ground-truth annotation file
    :param resType: identifier of the result annotation file
    :return: None
    '''

    # Define paths
    annFile = '%s/annotations/stuff_%s.json' % (dataDir, dataType)
    resFile = '%s/results/instances_stuff_%s_results.json' % (dataDir, resType)

    # Initialize COCO ground-truth API
    cocoGt = COCO(annFile)

    # Initialize COCO result API
    cocoRes = cocoGt.loadRes(resFile)

    # Run evaluation on the example images
    imgIds = sorted(set([a['image_id'] for a in cocoRes.anns.values()]))
    cocoEval = COCOStuffeval(cocoGt, cocoRes)
    cocoEval.params.imgIds = imgIds
    cocoEval.evaluate()
    cocoEval.summarize()

if __name__ == "__main__":
    pycocostuffEvalDemo()
