#!/usr/bin/env python 
# Copyright (c) 2009-2019 Quan Xu <qxuchn@gmail.com>
#
# This module is free software. You can redistribute it and/or modify it under 
# the terms of the MIT License, see the file COPYING included with this 
# distribution.

from __future__ import print_function
import sys
import os

import ananse.influence 
import ananse.config as cfg

def influence(args):
    config = cfg.MotifConfig()
    params = config.get_default_params()

    if not os.path.exists(args.outfile):
        print("File %s does not exist!" % args.outfile)
        sys.exit(1)

    params = {
        "outfile": args.outfile,
        "expression": args.expression,
        "fin_expression": args.fin_expression,
        "Gbf": args.Gbf,
        "Gaf": args.Gaf,
        "plot": args.plot,
    }

    a = ananse.influence.Influence(Gbf = args.Gbf, Gaf = args.Gaf, outfile= args.outfile, expression=args.expression, edges=10000)    
    a.run_influence(args.plot, args.fin_expression)
