"""
 unlikely to be useful to others, except as example.

 this renamer
 takes px name     : CACN00_CWAO_081900__WZS_14623:pxatx:CWAO:CA:5:Direct:20081008190602
 add datetimestamp : CACN00_CWAO_081900__WZS_14623:pxatx:CWAO:CA:5:Direct:20081008190602:20081008190612

"""
import logging
import sys, os, os.path, time, stat
from sarracenia.flowcb import FlowCB

logger = logging.getLogger(__name__)

class RenameDMF(FlowCB):
    def __init__(self, options):
        self.o = options

    def after_accept(self, worklist):
        new_incoming = []
        for message in worklist.incoming:
            datestr = time.strftime(':%Y%m%d%H%M%S', time.localtime())
            message['new_file'] += datestr
            message['headers']['rename'] += datestr
            new_incoming.append(message)

        worklist.incoming = new_incoming


