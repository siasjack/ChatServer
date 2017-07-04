# -*- coding:utf-8 -*-
__author__ = 'watsy'

import json
from protocol import Protocol
def is_json(myjson):
	if isinstance(myjson,str):
		try:
			json.loads(myjson,encoding='utf-8')
		except ValueError:
			return False
		return True
	else:
		return False



class TCPStreamPackage(object):

    def __init__(self , callback):
        super(TCPStreamPackage , self).__init__()

        self.datas = ''
        self._package_decode_callback = callback

    def add(self, data):
		print("getdata:",data)
		if is_json(data):
			package = Protocol.checkPackage(data)

			if self._package_decode_callback:
				self._package_decode_callback(package)
		else:
			print("not json data!!ignore")


