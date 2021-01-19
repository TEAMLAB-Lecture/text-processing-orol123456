# -*- coding: utf-8 -*-
# #######################
# # Test Processing I   #
# #######################
# """
# NLP에서 흔히하는 전처리는 소문자 변환, 앞뒤 필요없는 띄어쓰기를 제거하는 등의 텍스트 정규화 (text normalization)입니다. 
# 이번 숙제에서는 텍스트 처리 방법을 파이썬으로 배워보겠습니다. 
# """


def normalize(input_string):
    normalized_string=input_string.lower().strip()
    return ' '.join(normalized_string.split())


def no_vowels(input_string):
    vowel=['a','e','i','o','u','A','E','I','O','U']
    input_list=list(input_string)
    for i in range(len(input_list)):
        if input_list[i] in vowel:
            input_list[i]=""
    return "".join(input_list)
