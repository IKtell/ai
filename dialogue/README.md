# Implementation of Adversarial Learning for Neural Dialogue Generation

reference： [paper](https://arxiv.org/pdf/1701.06547.pdf) by Jiwei Li et al.



The model is based on generative adversarial network with a Generative model learning to create examples to be evaluated by a Discriminator model. 

**Generative Model**: a Seq2Seq setup using a GRU cell to implement attention.

**Discriminator Model**: Hierarchical RNN as used in [paper](http://www.aaai.org/ocs/index.php/AAAI/AAAI16/paper/download/11957/12160).

（problem：难训练）