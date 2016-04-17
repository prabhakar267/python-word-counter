# -*- coding: utf-8 -*-
# @Author: prabhakar
# @Date:   2016-04-16 21:03:43
# @Last Modified by:   Prabhakar Gupta
# @Last Modified time: 2016-04-18 00:47:19

import operator


def start(file_name):
	word_list = []
	fx = open(file_name, 'r')

	file_line_content = fx.readlines()

	for post_text in file_line_content:
		content = post_text
		
		words = content.lower().split()

		for each_word in words:
			word_list.append(each_word)

	clean_word_list(word_list)


def clean_word_list(word_list):
	clean_word_list = []

	for word in word_list:
		symbols = "~!@#$%^&*()_{}[]:\";'\|,./<>?`-='"

		for i in range(0, len(symbols)):
			word = word.replace(symbols[i], '')

		if len(word) > 0:
			clean_word_list.append(word)

	create_frequency_dictionary(clean_word_list)


def create_frequency_dictionary(word_list):
	word_count = {}

	for word in word_list:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1


	for key,value in sorted(word_count.items(), key=operator.itemgetter(0)):
		print(key, value)


filename = r"text-file"
start(filename)