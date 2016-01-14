#!/usr/bin/env python
# -*- coding: utf-8 -*-

# convert hangul to jamo back and forth

class Hangul:
    
    @staticmethod
    def hangul2jamo(hangul):
        # input: string or unicode
        # output: unicode
        if type(hangul) == str:
            hangul = hangul.decode('utf8')
        assert(len(hangul) == 1)
        codepoint = ord(hangul)
        if not (codepoint >= int('AC00',16) and codepoint<=int('D7A3',16)):
            return hangul
        start = 44032
        lead = ( codepoint - start ) / 588
        tail = ( codepoint - start ) % 28
        vowel = ((((codepoint - start) - tail) % 588) / 28)
        jamo = None;
        if tail == 0:
            jamo = unichr(lead + int('1100',16)) + unichr(vowel + int('1161',16))
        else:
            jamo = unichr(lead + int('1100',16)) + unichr(vowel + int('1161',16)) + unichr(tail + int('11A7',16))
        return jamo


    def jamo2hangul(jamo):
        pass


import sys

for line in sys.stdin:
    line = line.strip()
    line = line.decode('utf8')
    new_line = ""
    for c in line:
        new_line += Hangul.hangul2jamo(c)
    new_line = unicode(' ').join(new_line)
    new_line = new_line.encode('utf8')
    print new_line