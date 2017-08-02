# -*- coding: utf-8 -*-

from neo.io.basefromrawio import BaseFromRaw
from neo.rawio.winedrrawio import WinEdrRawIO

class WinEdrIO(WinEdrRawIO, BaseFromRaw):
    __prefered_signal_group_mode = 'split-all'
    def __init__(self, filename):
        WinEdrRawIO.__init__(self, filename=filename)
        BaseFromRaw.__init__(self, filename)
