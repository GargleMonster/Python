#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  missing_num.py
#  
#  Copyright 2021 garglemonster <garglemonster@garglemonster>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

def getmissingnumber(lst):
	print(set(range(lst[len(lst)-1])[1:]))
	print(set(lst))
	return set(range(lst[len(lst)-1])[1:]) - set(lst)
	
def main(args):
	l = list(range(1,10))
	print(l)
	l.remove(5)
	print(getmissingnumber(l))
	
	return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
