fr = '/Users/kellymarchisio/angec_final/data/full-test/europarl-v7.fr-en.short.fr'
en = '/Users/kellymarchisio/angec_final/data/full-test/europarl-v7.fr-en.short.en'

def count_unique_words(file):
	with open(file) as f:
		words = set()
		for line in f:
			for word in line.split():
				words.add(word)
		return len(words)

print 'words in FR'
print count_unique_words(fr)

print 'words in EN'
print count_unique_words(en)