#!/usr/bin/env python
# -*- coding: utf-8 -*-
import jieba


inp = open('word', 'rb')
out = open('data','wb')
for line in inp:
	x = line.split('{}')
	t = ""
	for y in range(len(x)):
		words = jieba.cut(x[y] , cut_all = False)
		tmp = ""
		for word in words:
			tmp = tmp + ' ' + word.strip()
		t = t + tmp
		if y < len(x)-1:
			t = t + ' {}'	
	out.write((t + '\n').encode('utf-8'))
 
