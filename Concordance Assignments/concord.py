import sys
import re


class concord:
    # constructor for concord class
    def __init__(self, input_file=None, output_file=None):
        self.input_file = input_file
        self.output_file = output_file
        # checks if a file has been given for concordance then writes to output
        if self.input_file_ != None and self.output_file != None:
            concordance = self.full_concordance()
            self.__write_to_output(concordance)

    # ensures provided test is of the correct: version prints error if it is not
    def __version_check(self,to_read):
        version = to_read.readline().strip()
        # checks that the first line is not white space
        if version != "":
            if int(version) != 2:
                print("Input is version", version, ", concord.py expected version 2")

    # gets all the words that shouldn't be indexed for the concordance
    def __get_exclusion_words(self, to_read):
        # reads and ignores the starting '''' line
        to_read.readline()
        exclusion_word_list =[]

        for line in to_read:
            line = line.rstrip()
            # catches the end of exclusion words and breaks loop
            if line == "\"\"\"\"":
                break
            # ensures there's an exclusion word on the line, moves on if not
            if line == "":
                continue
            exclusion_word_list.append(line.upper())

        return exclusion_word_list

    # gets all lines from input that need to be indexed
    def __get_lines(self, to_read):
        line_list = []

        for line in to_read:
            line = line.rstrip()
            # check if line is empty, moves onto next line if true
            if line == "":
                continue
            line_list.append(line)
        return line_list

    # forms and returns a dictionary with indexed words as keys and sentences as values
    def __make_keyword_dictionary(self, lines, exclusion_words):
        keyword_dict = {}

        for line in lines:
            split_line = line.split(" ")
            for word in split_line:
                word = word.strip().upper()
                # checks word against exclusion_words ignores if it's present, indexes it otherwise
                if word not in exclusion_words:
                    line_copy = line[:]
                    line_copy = re.sub(r"\b"+word+r"\b", word, line_copy, flags=re.I)

                    # checks if keyword is already in dictionary and appends to value list
                    # creates new dictionary entry otherwise
                    if word in keyword_dict:
                        keyword_dict[word].append(line_copy)
                    else:
                        keyword_dict[word] = [line_copy]
        return keyword_dict

    # writes the full concordance to output file given from self
    def __write_to_output(self, concordance):
        to_write = open(self.output_file, "w")
        to_write.write("\n".join(concordance))
        to_write.write("\n")
        to_write.close()

    # formats the concordance lines and returns a list of all indexed lines
    def __format_concordance(self, keywords, keyword_dict):
        final_list = []

        for word in keywords:
            lines = keyword_dict[word]
            for line in lines:
                line = line.strip()

                matchobj = re.search(r"(\b.{,ro}\b)"+word+rf"\b.{{,{31-len(word)}}}\b", line)

                final_line = re.sub(r"^", " "*(29-len(matchobj.group(1))), matchobj.group(0))
                final_list.append(final_line.rstrip())

        return final_list

    def full_concordance(self):

        if self.input_file != None:
            to_read = open(self.input_file, "r")
        else:
            to_read = sys.stdin

        self.__version_check(to_read)
        exclusion_words = self.__get_exclusion_words(to_read)
        lines = self.__get_lines(to_read)
        keyword_dict = self.__make_keyword_dictionary(lines, exclusion_words)
        sorted_keywords = sorted(keyword_dict, key=str.casefold)
        concord_list = self.__format_concordance(sorted_keywords, keyword_dict)

        if self.input_file != None:
            to_read.close()

        return concord_list
