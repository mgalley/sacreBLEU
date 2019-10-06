#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# Small test case for deltaBLEU, which incidentally shows that dBLEU == BLEU when weights are uniform

import sacrebleu

ref_t = [
         ['the food was delicious .', 'it was great .'],
         ['it was tasty .', 'i enjoyed the music .'],
         ['it was good .', 'i liked the music .'],
         ['it was ok .', 'it sounded ok .'],
         ["it didn't taste that bad", "it wasn't that bad ."],
         ['it tasted terrible .', "it was awful ."]
]

ref_scores_t = [[1, 1], [0.7, 0.6], [0.3, 0.3], [0.0, 0.0], [-0.1, -0.1], [-1, -1]]
pred1_t = [ 'the food was quite good .', 'the music was great .' ] # "good" system, which matches highly weighted references
pred2_t = [ 'the food tasted terrible .', 'the music was awful .' ] # "bad" system, which matches lowly weighted references

print("BLEU:")
print("system1: " + str(sacrebleu.corpus_bleu(pred1_t, ref_t)))
print("system2: " + str(sacrebleu.corpus_bleu(pred2_t, ref_t)))

print("deltaBLEU with uniform weights: (shows special case of BLEU)") # for sanity check: bleu == delta_bleu when all references have w = 1
uni_scores_t = [[1, 1], [1, 1], [1, 1], [1, 1], [1, 1], [1, 1]]
print("system1: " + str(sacrebleu.corpus_bleu(pred1_t, ref_t, ref_weights=uni_scores_t)))
print("system2: " + str(sacrebleu.corpus_bleu(pred2_t, ref_t, ref_weights=uni_scores_t)))

print("deltaBLEU:")
print("system1: " + str(sacrebleu.corpus_bleu(pred1_t, ref_t, ref_weights=ref_scores_t)))
print("system2: " + str(sacrebleu.corpus_bleu(pred2_t, ref_t, ref_weights=ref_scores_t)))

# Expected output:
# BLEU:
# system1: BLEU = 36.28 90.9/66.7/28.6/10.0 (BP = 1.000 ratio = 1.100 hyp_len = 11 ref_len = 10)
# system2: BLEU = 42.04 100.0/75.0/33.3/12.5 (BP = 1.000 ratio = 1.000 hyp_len = 10 ref_len = 10)
# deltaBLEU with uniform weights: (shows special case of BLEU)
# system1: BLEU = 36.28 90.9/66.7/28.6/10.0 (BP = 1.000 ratio = 1.100 hyp_len = 11 ref_len = 10)
# system2: BLEU = 42.04 100.0/75.0/33.3/12.5 (BP = 1.000 ratio = 1.000 hyp_len = 10 ref_len = 10)
# deltaBLEU:
# system1: BLEU = 33.11 77.3/54.4/28.6/10.0 (BP = 1.000 ratio = 1.100 hyp_len = 11 ref_len = 10)
# system2: BLEU = 7.14 32.0/6.2/4.2/3.1 (BP = 1.000 ratio = 1.000 hyp_len = 10 ref_len = 10)
