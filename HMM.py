

import random
import argparse
import codecs
import os
import sys

import numpy

# Sequence - represents a sequence of hidden states and corresponding
# output variables.

class Sequence:
	def __init__(self, stateseq, outputseq):
		self.stateseq  = stateseq   # sequence of states
		self.outputseq = outputseq  # sequence of outputs
	def __str__(self):
		return ' '.join(self.stateseq)+'\n'+' '.join(self.outputseq)+'\n'
	def __repr__(self):
		return self.__str__()
	def __len__(self):
		return len(self.outputseq)

# HMM model
class HMM:
	def __init__(self, transitions:dict=None, emissions:dict=None):
		"""creates a model from transition and emission probabilities
		e.g. {'happy': {'silent': '0.2', 'meow': '0.3', 'purr': '0.5'},
			  'grumpy': {'silent': '0.5', 'meow': '0.4', 'purr': '0.1'},
			  'hungry': {'silent': '0.2', 'meow': '0.6', 'purr': '0.2'}}"""
		if emissions is None:
			emissions = {}
		if transitions is None:
			transitions = {}
		self.transitions = transitions
		self.emissions = emissions

	## part 1 - you do this.
	def load(self, basename: str):
		with open(basename + ".emit" ,"r") as f:
			for line in f:
				emits = line.strip().split(" ")
				if emits[0] not in self.emissions:
					self.emissions[emits[0]] = {}
				self.emissions[emits[0]][emits[1]] = float(emits[2])

		with open(basename + ".trans" ,"r") as f:
			for line in f:
				transms = line.strip().split(" ")
				if transms[0] not in self.transitions:
					self.transitions[transms[0]] = {}
				self.transitions[transms[0]][transms[1]] = float(transms[2])

	## you do this.
	def generate(self, n):
		transms = [random.choices(list(self.transitions["#"]), weights=self.transitions["#"].values())[0]]
		emits = [random.choices(list(self.emissions[transms[0]]), weights=self.emissions[transms[0]].values())[0]]

		for i in range(n - 1):
			transms.append(random.choices(list(self.transitions[transms[i]]), weights=self.transitions[transms[i]].values())[0])
			emits.append(random.choices(list(self.emissions[transms[i + 1]]), weights=self.emissions[transms[i + 1]].values())[0])

		return transms, emits

	def forward(self, sequence):
		pass
	## you do this: Implement the Viterbi algorithm. Given a Sequence with a list of emissions,
	## determine the most likely sequence of states.






	def viterbi(self, sequence):
		pass
	## You do this. Given a sequence with a list of emissions, fill in the most likely
	## hidden states using the Viterbi algorithm.


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument("basename")
	parser.add_argument("--generate")
	args = parser.parse_args()
	h = HMM()
	h.load(args.basename)
	if args.generate:
		chain = h.generate(int(args.generate))
		print(chain)