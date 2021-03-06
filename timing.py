#!/usr/bin/env python

import subprocess
import time

subprocess.check_call(['make'])
tic = time.time()
subprocess.check_call(['./fastSVM', 'tests/image1.jpg', 'packaged.gz', 'output.gz'])
toc = time.time()
print('Executed in %f seconds'%(toc - tic))
