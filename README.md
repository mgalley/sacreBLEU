This project adds deltaBLEU ([Galley et al., 2015](https://www.aclweb.org/anthology/P15-2073/)) to [SacreBLEU](https://github.com/mjpost/sacreBLEU). 

The method `corpus_bleu` has been extended to take an optional `ref_weights` argument, which is needed to compute deltaBLEU. If these weights are missing (or all set to 1), the method returns the same values as the original `corpus_bleu` method. This is because deltaBLEU was defined in such a way that it admits BLEU as a special case. For a sample usage of deltaBLEU with this project, you can run:

```
python test_deltableu.py
```

As this project is otherwise identical to SacreBLEU, 
please refer to [this page](https://github.com/mjpost/sacreBLEU) for more information on how to install and use the code. Note that you will have to 
install SacreBLEU manually (i.e., without pip3, etc.) as this extension is not part of SacreBLEU.

If you use SacreBLEU, please cite the following:

```
@inproceedings{post-2018-call,
  title = "A Call for Clarity in Reporting {BLEU} Scores",
  author = "Post, Matt",
  booktitle = "Proceedings of the Third Conference on Machine Translation: Research Papers",
  month = oct,
  year = "2018",
  address = "Belgium, Brussels",
  publisher = "Association for Computational Linguistics",
  url = "https://www.aclweb.org/anthology/W18-6319",
  pages = "186--191",
}
```

If you use deltaBLEU (e.g., this implementation), please cite:

```
@inproceedings{galley-etal-2015-deltableu,
  title = "delta{BLEU}: A Discriminative Metric for Generation Tasks with Intrinsically Diverse Targets",
  author = "Galley, Michel  and
  Brockett, Chris  and
  Sordoni, Alessandro  and
  Ji, Yangfeng  and
  Auli, Michael  and
  Quirk, Chris  and
  Mitchell, Margaret  and
  Gao, Jianfeng  and
  Dolan, Bill",
  booktitle = "Proceedings of the 53rd Annual Meeting of the Association for Computational Linguistics and the 7th International Joint Conference on Natural Language Processing (Volume 2: Short Papers)",
  month = jul,
  year = "2015",
  address = "Beijing, China",
  publisher = "Association for Computational Linguistics",
  doi = "10.3115/v1/P15-2073",
  pages = "445--450",
}
```
