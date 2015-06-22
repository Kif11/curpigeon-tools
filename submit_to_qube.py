import sys

sys.path.append('C:/Program Files/pfx/qube/api/python')

import qb

job = {
    'prototype': 'maya',
    'name': 'python callback test',
    'package': {
    'cmdline': 'hostname',
    },
    'callbacks': [
        {
            'language': 'python',
            'triggers': 'done-job-self',
            'code': '''
try:
    import sys
     
    fh = open('c:/temp/err.txt', 'w')
    fh.close()
     
    fh = open('c:/temp/foo.txt', 'w')
    fh.write('Hello from job id %s\\n' % qb.jobid())
    fh.write('sys.version : %s\\n' % sys.version)
    fh.write('sys.version info : %s\\n' % '.'.join([str(x) for x in sys.version_info]))
    fh.write('sys.executable : %s\\n' % sys.executable)
    fh.close()
except Exception, e:
    fh = open('c:/temp/err.txt', 'w')
    fh.write('Error from job id %s\\n' % qb.jobid())
    fh.write('%s\\n' % e)
    fh.close()
'''
            }
        ]
    }
print '%(id)s: %(name)s' % qb.submit(job)[0]