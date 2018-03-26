#!/usr/bin/python3

"""
  on_heartbeat handler that runs a sanity check on all processes
  This plugin was designed to be used under sr_audit only

"""

class Hb_Sanity(object): 

    def __init__(self,parent):
        parent.logger.debug( "hb_sanity initialized" )
          
    def perform(self,parent):
        parent.logger.debug( "hb_sanity launching sr sanity" )
        subprocess.check_call(['sr','sanity'])
        return True

hb_sanity = Hb_Sanity(self)
self.on_heartbeat = hb_sanity.perform
