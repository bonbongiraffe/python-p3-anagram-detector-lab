# your code goes here!

class Anagram : 
    def __init__( self, word ):
        self.word = word
    
    def get_word( self ):
        return self._word 

    def set_word( self, word ):
        if type(word) == str:
            self._word = word
        else:
            print("word must be a string")

    def match( self, word_list ):
        output_list = []
        for word in word_list:
            target_letter_list = [letter for letter in self.word]
            search_letter_list = [letter for letter in word]
            filtered_search_letter_list = []
            for letter in search_letter_list:
                if letter in target_letter_list:
                    filtered_search_letter_list.append(letter)
            if sorted(filtered_search_letter_list) == sorted(target_letter_list):
                output_list.append(word)
        return output_list
                
    word = property ( get_word, set_word )