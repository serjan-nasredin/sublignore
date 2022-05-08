#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sublime, sublime_plugin
import re, os, sys
import mimetypes as mime


class SublimeIgnore(sublime_plugin.Event):
	""" Sublime Text pattern exclusion file """

    MARKER = 'sublignore'

	def folder_exclude_patterns(self):
		pass

	def file_exclude_patterns(self):
		pass

	def binary_file_patterns(self):
		pass

	def index_exclude_patterns(self):
		pass

	def index_exclude_gitignore(self):
		pass

	def ignored_packages(self):
		pass

    def run(self):
        with open(file=f'.{MARKER}', mode='r', encoding="utf-8") as file:
            file.open()
