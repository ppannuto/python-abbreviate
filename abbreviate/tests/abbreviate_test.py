import unittest

import re

import abbreviate

class BasicsTest(unittest.TestCase):
	def setUp(self):
		self.abbr = abbreviate.Abbreviate()

	def test_basic_abbreviaions(self):
		basics = [
				[
					"The quick brown fox jumped over the lazy dog",
					"The quick brown fox jumped over the lazy dog",
					],
				[
					"The Sunday sad bar closed on monday not tuesday this week",
					"The Sun sad bar closed on mon not tue this week",
					],
				[
					"Christmas in July is the best holiday",
					"Christmas in Jul is the best holiday",
					],
				]
		for s in basics:
			self.failUnlessEqual(self.abbr.abbreviate(s[0]), s[1])

	def test_aggressive_length(self):
		phrases = [
				"The quick brown fox jumped over the lazy dog",
				"The Sunday sad bar closed on monday not tuesday this week",
				"Christmas in July is the best holiday",
				]
		print("")
		for p in phrases:
			a = self.abbr.abbreviate(p, target_len=35)
			print("\t{}\n\t{}\n".format(p, a))

	def test_custom_length_function(self):
		def len_fn(t):
			return len(t) + len(re.split('[A-Z]', t))
		phrases = [
				"The quick brown fox jumped over the lazy dog",
				"The Sunday sad bar closed on monday not tuesday this week",
				"Christmas in July is the best holiday",
				]
		print("")
		for p in phrases:
			a = self.abbr.abbreviate(p, target_len=35, len_fn=len_fn)
			print("\t{}\n\t{}\n".format(p, a))

if __name__ == '__main__':
	unittest.main()
