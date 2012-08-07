#!/usr/bin/env python

"""
Version information for the application.
"""

# Major version number
MAJOR = 1

# Minor version number
MINOR = 0

# Development stage
STAGES = {
    'alpha': 'a',
    'beta': 'b',
    'release candidate': 'rc',
    'release': 'r'
}

# Current development stage
STAGE = 'alpha'

# Deploy number for the current stage
DEPLOY = 1

# Full version tuple
VERSION_NUMBER = (MAJOR, MINOR, STAGE, DEPLOY)

# Textual representation of the version number
VERSION = '%d.%d%s%d' % (MAJOR, MINOR, STAGES[STAGE], DEPLOY)
