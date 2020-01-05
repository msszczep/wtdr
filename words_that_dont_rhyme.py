# A surprisingly complicated Python program to test for two words that
# don't rhyme. 
# 
# Requires the cmudict file from the Natural Language Toolkit (NLTK) residing in the present working directory.

from random import sample

class WordsThatDontRhyme():

     def __init__(self):
          self.vowels = ['AA', 'AH', 'EH', 'IH', 'OW', 'UH', 'AE', 'AO', 'AY', 'IY', 'ER', 'OY', 'UW']
          lines = open('cmudict-0.7b.txt', 'r')
          self.w = {} # words
          self.s = () # selection
          for line in lines:
               t = line[:-1].split(' ')
               try:
                    self.w[t[0]].append(t[2:])
               except: 
                    self.w[t[0]] = [t[2:]]

     def get_last_syllable_nucleus_coda(self, w):
          to_return = [] 
          for r in self.w[w]:
               temp = []
               r.reverse()
               for e in r:
                    temp.append(e)
                    if e[0:2] in self.vowels:
                          break
               temp.reverse()
               to_return.append(temp)
          return to_return 

     def check_rhyme(self):
          s1 = self.get_last_syllable_nucleus_coda(self.s[0])
          s2 = self.get_last_syllable_nucleus_coda(self.s[1])
          for c1 in s1:
               for c2 in s2:
                    if c1 == c2:
                         return True
          return False

     def select_words(self):
           self.s = sample(self.w, 2)

     def main(self):
          self.select_words()
          while self.check_rhyme() == True:
               self.select_words()
          return self.s
 
if __name__ == '__main__':
     w = WordsThatDontRhyme() 
     print w.main()
