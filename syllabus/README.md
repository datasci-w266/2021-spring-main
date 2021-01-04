# DATASCI W266: Natural Language Processing with Deep Learning

[Course Overview](#course-overview)  
[Grading](#grading)  
[Final Project](#final-project)  
[Course Resources](#course-resources)  
[Schedule and Readings](#schedule-and-readings)  

* [Piazza](https://piazza.com/berkeley/spring2021/datasciw266) - we'll use this for Q&A, and this will be the fastest way to reach the course staff. Note that you can post anonymously, and/or make posts visible only to instructors for private questions.

## Course Overview
Understanding language is fundamental to human interaction. Our brains have evolved language-specific circuitry that helps us learn it very quickly; however, this also means that we have great difficulty explaining how exactly meaning arises from sounds and symbols. This course is a broad introduction to linguistic phenomena and our attempts to analyze them with machine learning. We will cover a wide range of concepts with a focus on practical applications such as information extraction, machine translation, sentiment analysis, and summarization.

**Prerequisites:**
* Language: All assignments will be in Python using Jupyter notebooks, NumPy, and TensorFlow.
* Time:  There are 6-7 substantial assignments in this course as well as a term project.  Make sure you give yourself enough time to be successful! In particular, you may be in for a rough semester if you have other significant commitments at work or home, or take both this and any of 210 (Capstone), 261, or 271 :)
* [MIDS 207 (Machine Learning)](https://www.ischool.berkeley.edu/courses/datasci/207): We assume you know what gradient descent is.  We'll review simple linear classifiers and softmax at a high level, but make sure you've at least heard of these! You should also be comfortable with linear algebra, which we'll use for vector representations and when we discuss deep learning.

**Contacts and resources:**
* Course website: [GitHub datasci-w266/2021-spring-main](../../../)
* [Piazza](https://piazza.com/) - we'll use this for Q&A, and this will be the fastest way to reach the course staff. Note that you can post anonymously, and/or make posts visible only to instructors for private questions.
* Email list for course staff (expect a somewhat slower response here): [mids-nlp-instructors@googlegroups.com](mailto:mids-nlp-instructors@googlegroups.com)

**Live Sessions:**
* (Section 1) Tuesday 4 - 5:30p Pacific (Daniel Cer)
* (Section 2) Wednesday 6:30 - 8p Pacific (Mike Tamir, Paul Spiegelhalter)
* (Section 3) Thursday 4 - 5:30p Pacific (Mark Butler)
* (Section 4) Friday 4 - 5:30p Pacific (Mark Butler)
* (Section 5) Saturday 8 - 9:30a Pacific (Sid J Reddy)
* (Section 97) Tuesday 2 - 3:30p Pacific (Peter Grabowski)
* (Section 98) Wednesday 4 - 5:30p Pacific (Joachim Rahmfeld)
* (Section 99) Thursday 4 - 5:30p Pacific (Zack Alexander)

**Teaching Staff Office Hours:**

* **Zack Alexander**: TDB
* **Mark Butler**: Thursday and Friday immediately after his live session
* **Daniel Cer**: Thursday at 4pm PST
* **Peter Grabowski**: TBD
* **Joachim Rahmfeld**: Wednesday immediately after his live session
* **Sid J Reddy**: Saturday immediately after his live session
* **Mike Tamir/Paul Spiegelhalter**: Wednesday immediately after his live session
* **Drew Plant**: Monday at 6pm PST
* **Gurdit Chahal**: Tuesday at 5pm PST
* **Anu Yadav**: TBD

Office hours are for the whole class; students from any section are welcome to attend any of the times above.

**Async Instructors:**
* Dan Gillick
* James Kunz
* Kuzman Ganchev


## Grading

### Breakdown

Your grade report can be found at [https://w266grades.appspot.com](https://w266grades.appspot.com).

Your grade will be determined as follows:
* **Weekly Assignments**: 40%
* **Final Project**: 60%
* **Participation**: Up to 10% bonus

There will be a number of smaller [assignments](../assignment/) throughout the term for you to
exercise what you learned in async and live sessions. Some assignments may be more difficult than others, and may be weighted accordingly.

Participation will be graded holistically, based on live session participation as well as participation on Piazza (or other activities that improve the course this semester or into the future). Do not stress about this part.


### Letter Grades

We curve the numerical grade to a letter grade.  While we don't release the curve, it usually results in about a quarter of the class each receiving A, A-, B+, and B.  Exceptional cases receive A+, C, or F, as appropriate.

A word of warning:  Given that we (effectively) release solutions to assignments in the form of unit tests, it shouldn't be surprising that most students earn near perfect scores.  Since the variance is so low, assignment scores aren't the primary driver of the final letter grade for most students.  A good assignment score is necessary, but not sufficient, for a strong grade in the class.  A well structured, novel project with good analysis is what makes the difference between a high B/B+ and an A-/A.

As mentioned above:  this course is a lot of work.  Give it the time it deserves and you'll be rewarded intellectually and on your transcript.


### Late Day Policy

We recognize that sometimes things happen in life outside the course, especially in MIDS where we all have full time jobs and family responsibilities to attend to. To help with these situations, we are giving you **5 "late days"** to use throughout the term as you see fit.  Each late day gives you a 24 hour (or any part thereof) extension to any deliverable in the course **except** the final project presentation or report. (UC Berkeley needs grades submitted very shortly after the end of classes.)

Once you run out of late days, each 24 hour period (or any part thereof) results in a **10 percentage point deduction** on that deliverable's grade.

You can use a **maximum of 2 late days** on any single deliverable.  We will **not be accepting any submissions more than 48 hours past the original due-date**, even if you have late days. (We want to be more flexible here, but your fellow students also want their graded assignments back promptly!)

We don't anticipate granting extensions beyond these policies.  Plan your time accordingly!

### More serious issues

If you run into a more serious issue that will affect your ability to complete the course, please email the instructors mailing list and cc MIDS student services.  A word of warning though: in previous sections, we have had students ask for INC grades because their lives were otherwise busy.  Mostly we have declined, opting instead for the student to complete the course to the best of their ability and have a grade assigned based on that work.  (MIDS prefers to avoid giving INCs, as they have been abused in the past.)  The sooner you start this process, the more options we (and the department) have to help.  Don't wait until you're suffering from the consequences to tell us what's going on!


## Final Project
*See the [Final Project Guidelines](../project/)*

## Requirements for in-class participation

We believe in the importance of the social aspects of learning: between students, and between students and instructors, and we recognize that knowledge-building is not solely occurring on an individual level, but that it is built by social activity involving people and by members engaged in the activity. Participation and communication are key aspects of this course that are vital to the learning experiences of you and your classmates.

Therefore, we like to remind all students of the following requirements for live class sessions:

* Students are required to join live class sessions from a study environment with video turned on and with a headset for clear audio, without background movement or background noise, and with an internet connection suitable for video streaming.

* You are expected to engage in class discussions, breakout room discussions and exercises, and to be present and attentive for your and other teams’ in-class presentations. 

* Keep your microphone on mute when not talking to avoid background noise. Do your best to minimize distractions in the background video, and ensure that your camera is on while you are engaged in discussions. 

That said, in exceptional circumstances, if you are unable to meet in a space with no background movement, or if your connection is poor, make arrangements with your instructor (beforehand if possible) to explain your situation. Sometimes connections and circumstances make turning off video the best option. If this is a recurring issue in your study environment, you are responsible for finding a different environment that will allow you to fully participate in classes, without distraction to your classmates.

**Failure to adhere to these requirements will result in an initial warning from your instructor(s), followed by a possible reduction in grades or a failing grade in the course.**

## Course Resources
We are not using any particular textbook for this course. We’ll list some relevant readings each week. Here are some general resources:
* [Speech and Language Processing (2nd edition)](http://www.cs.colorado.edu/~martin/slp.html) (Jurafsky and Martin)
* [Speech and Language Processing (3rd edition draft)](https://web.stanford.edu/~jurafsky/slp3/) (Jurafsky and Martin) - _free online!_
* [NLTK Book](http://www.nltk.org/book/) - Accompanies NLTK (Natural Language ToolKit) and includes useful, practical descriptions (with python code) of basic concepts.
* [Deep Learning](http://www.deeplearningbook.org/) (Goodfellow, Bengio, and Courville)

We’ll be posting materials to the course [GitHub repo](../../../).

*Note:* the syllabus below might be subject to change. We'll be sure to announce anything major on Piazza.

### Code References

The course will be taught in Python, and we'll be making heavy use of NumPy, TensorFlow, Keras, and Jupyter (IPython) notebooks. We'll also be using Git for distributing and submitting materials. If you want to brush up on any of these, we recommend:
* **Git tutorials:** [Introduction / Cheat Sheet](https://git-scm.com/docs/gittutorial), or [interactive tutorial](https://try.github.io/)
* **Python / NumPy:** Stanford's CS231n has [an excellent tutorial](http://cs231n.github.io/python-numpy-tutorial/).
* **TensorFlow:** We'll go over the basics of TensorFlow and Keras in [Assignment 2](../../../tree/master/assignment/a2/).  
  [Effective TensorFlow](https://github.com/vahidk/EffectiveTensorflow) is a great reference, ranging from the absolute basics through advanced topics like multi-GPU training, `tf.learn`, and debugging.  
  You can also check out the [tutorials](https://www.tensorflow.org/get_started/) on the TensorFlow website, but these can be somewhat confusing if you're not familiar with the underlying models. Also, look at the [Keras Guide](https://www.tensorflow.org/guide/keras/sequential_model) as we will be using Keras in this class. 


### Misc. Deep Learning and NLP References
A few useful papers that don’t fit under a particular week. All optional, but interesting!
* (optional) [Chris Olah’s blog](http://colah.github.io/) and [Distill](https://distill.pub/)
* (optional) [GloVe: Global Vectors for Word Representation (Pennington, Socher, and Manning, 2014)](http://nlp.stanford.edu/pubs/glove.pdf)

---

## Tentative Schedule and Readings

We'll update the table below with assignments as they become available, as well as additional materials throughout the semester. Keep an eye on GitHub for updates!

*Dates are tentative:* assignments in particular may change topics and dates.  (Updated slides for each week will be posted during the live session week.)

### Live Session Slides: [[available here with @berkeley.edu address](https://drive.google.com/drive/folders/1-5aoNNsqaFOaPvpUmuqQClTZeY-tgihY?usp=sharing)]

### Deliverables

Note:  we will update this table as we release (approximately weekly) assignments.  Each assignment
will be released around the last live session of the week and due approximately one week later.

<table>
<tr>
<th></th><th>Topic</th><th>Release</th><th>Deadline</th>
</tr>
<tr>
  <td>
  <!-- <strong><a href="../assignment/a0" target="_blank">Assignment&nbsp;0</a></strong>  -->
  Assignment&nbsp;0
  <td><strong>Course Set-up</strong>
  <ul>
    <li>GitHub
    <li>Piazza
    <li>Google Cloud
  </ul></td>
  <td></td>
  <td>TBD</td>
</tr>

<!-- draft project proposal -->
<!-- <tr> 
  <td><strong><a href="../project/#draft-project-proposal" target="_blank">Project&nbsp;Proposal Draft</a></strong>
  <td>
  <strong><a href="../project" target="_blank">Draft Project Guidelines</a></strong>
  </td>
  <td></td>
  <td>Sep&nbsp;12</td>
</tr> -->

<tr> <!-- project proposal -->
  <td><strong><a href="../project/#project-proposal" target="_blank">Project&nbsp;Proposal</a></strong>
  <td>
  <strong><a href="../project" target="_blank">Final Project Guidelines</a></strong>
  </td>
  <td></td>
  <td>Feb&nbsp;6</td>
</tr>
<tr><!--- Project Reports -->
  <td><strong><a href="../project/#final-submission" target="_blank">Project&nbsp;Reports</a></strong>
  </td>
  <td></td>
  <td></td>
  <td><br>due April&nbsp;10<br><strong>(hard deadline)</strong></td>
</tr>
<tr><!--- Project Presentations -->
  <td><strong><a href="../project/#presentations" target="_blank">Project&nbsp;Presentations</a></strong></td>
  <td></td>
  <td></td>
  <td>in-class April&nbsp;12-17</td>
</tr>
</table>


### Course Schedule

<table>
<tr>
<th></th>
<th>Async to Watch</th>
<th>Topics</th>
<th>Materials</th>
</tr>
<tr><!--- Introductions -->
  <td><strong>Week&nbsp;1</strong><br>(Jan&nbsp;4)</td>
  <td>Introduction
  </td>
  <td><ul>
    <li>Overview of NLP applications
	<li>NLP tasks, model structures and neural architectures
    <li>Ambiguity and grounding in language
    <li>Information theory review
    <li>ML models: Logistic regression and feed forward networks
  </ul></td>
  <td><ul>
  <li>Skim: <a href="http://www.nltk.org/book/ch01.html" target="_blank">NLTK book chapter 1 (python and basics)</a>
  <li>Skim: <a href="http://www.nltk.org/book/ch02.html" target="_blank">NLTK book chapter 2 (data resources)</a>
  <li>Read: <a href="https://www.technologyreview.com/s/602094/ais-language-problem/" target="_blank">AI’s Language Problem (Technology Review)</a>
  <li>Read: <a href="http://nautil.us/issue/54/the-unspoken/the-rise-and-fall-of-the-english-sentence" target="_blank">The Rise and Fall of the English Sentence</a>
  <li><em>Optional:</em> <a href="http://www.newyorker.com/magazine/2007/04/16/the-interpreter-2" target="_blank">The Interpreter (New Yorker)</a>
  <li><em>Optional:</em> <a href="https://www.uio.no/studier/emner/hf/ikos/EXFAC03-AAS/h05/larestoff/linguistics/Chapter%204.(H05).pdf" target="_blank">Introduction to Linguistic Typology</a>
      <li><em>Optional / fun:</em> <a href="http://playground.tensorflow.org/" target="_blank">Tensorflow Playground</a>
  </ul>
  <!-- <p>                                        -->
  <!-- <a href="../materials/week1/TensorFlow%20Tutorial.ipynb" target="_blank">[TensorFlow&nbsp;Intro&nbsp;notebook]</a> -->
  </td>
</tr>
<tr><!--- Week 2 -->
  <td><strong>Week&nbsp;2</strong><br>(Jan&nbsp;11)</td>
  <td>
  <br>5.2 Softmax Classification
  <br>5.4 Neural network recap
  <br>5.5 Neural network training loss
  </td>
  <td><ul>
    <li>ML models: Logistic regression and feed forward networks
	<li>Learning and back propagation
    <li>Initialization
  </ul></td>
  <td><ul>
  <li><em>Skim:</em> <a href="https://www.cs.toronto.edu/~hinton/absps/pdp8.pdf">Original backprop paper</a>
      <li><em>Optional / fun:</em> <a href="http://playground.tensorflow.org/" target="_blank">Tensorflow Playground</a>
  </ul>
  <!-- <p>                                        -->
  <!-- <a href="../materials/week1/TensorFlow%20Tutorial.ipynb" target="_blank">[TensorFlow&nbsp;Intro&nbsp;notebook]</a> -->
  </td>
</tr>
<tr><!--- Sentiment/Classification -->
  <td><strong>Week&nbsp;3</strong><br>(Jan&nbsp;18)</td>
  <td>Classification and Sentiment (up to 2.6), 
  <br>4.2, 4.12 - 4.17, 
  <br>6.10, 6.12
  </td>
  <td><ul>
  <li>Sentiment lexicons
  <li>Aggregated sentiment applications
  <li>Bag-of-words models
  <li>Introduction to word embeddings
  </ul></td>
  <td><ul>
  <li>Skim: <a href="http://www.cs.cornell.edu/home/llee/omsa/omsa.pdf" target="_blank">Opinion Mining and Sentiment Analysis</a> (Pang and Lee 2008) - focus on Chapters 1-4
  <li><em>Optional:</em> <a href="https://arxiv.org/pdf/1103.0398v1.pdf" target="_blank">Natural Language Processing (almost) from Scratch</a> (Collobert et al., 2011)
</tr>

<tr><!--- POS Tagging and Parsing -->
  <td><strong>Week&nbsp;4</strong><br>(Jan&nbsp;25)</td>
  <td><a href="https://www.youtube.com/playlist?list=PLh1VT8Lm3apRPGB1uKZsMyMt1DmUf_ItE">Part of Speech Supplementary Videos</a>
  <br>Dependency Parsing (Parsing I)
  <br>Constituency Parsing (Parsing II)</td>
  <td><ul>
  <li>Tag sets
  <li>Most frequent tag baseline
  <li>HMM/CRF models
  <li>Dependency trees
  <li>Transition-based parsing: Arc&#8209;standard, Arc&#8209;eager
  <li>Context-free grammars (CFGs)
  <li>CKY algorithm
  <li>Probabilistic CFGs
  </ul>
  <b>Note:</b> Section 7.6 this week in the async is optional.
  </td>
  <td><ul>
  <li>Read: <a href="http://www.nltk.org/book/ch05.html" target="_blank">NLTK book chapter 5: Categorizing and Tagging Words</a>
  <li>Read: <a href="https://arxiv.org/pdf/1104.2086.pdf" target="_blank">A Universal Part-of-Speech Tagset</a>
  <li><em>Optional:</em> <a href="http://nlp.stanford.edu/pubs/CICLing2011-manning-tagging.pdf" target="_blank">Part-of-Speech Tagging from 97% to 100%: Is It Time for Some Linguistics?</a>
    <li>Read: <a href="https://research.googleblog.com/2016/05/announcing-syntaxnet-worlds-most.html" target="_blank">SyntaxNet (Parsey McParseface)</a>
  <li>Skim: <a href="https://web.stanford.edu/~jurafsky/slp3/15.pdf" target="_blank">Dependency Parsing (J&M Chapter 15)</a>
    <li>Skim: <a href="https://web.stanford.edu/~jurafsky/slp3/13.pdf" target="_blank">Constituency Parsing (J&M Chapter 13)</a>
  <li><em>Optional:</em> <a href="http://cs.stanford.edu/people/danqi/papers/emnlp2014.pdf" target="_blank">A Fast and Accurate Dependency Parser using Neural Networks</a> (Chen & Manning 2014)
    <li>Skim: <a href="http://www.nltk.org/book/ch08.html" target="_blank">NLTK book chapter 8 (analyzing sentence structure)</a>
  <li>Skim: <a href="http://ilpubs.stanford.edu:8091/~klein/unlexicalized-parsing.pdf" target="_blank">Accurate Unlexicalized Parsing</a> (Klein & Manning 2003)
  <li>Play: <a href="http://nlp.stanford.edu:8080/parser/" target="_blank">Stanford parser</a> (online demo)
  <li><em>Optional / reference:</em> <a href="http://www.surdeanu.info/mihai/teaching/ista555-fall13/readings/PennTreebankConstituents.html" target="_blank">Penn Treebank Constituent Tags</a>
  </ul>
  <br>
  <a href="https://hmm-dot-nlp-visualizations.appspot.com/hmm?sentence=James+ate+the+food&vizMode=viterbi&numFormat=log" target="_blank">[<em>Optional:</em> Interactive HMM Demo]</a>
  <p>
  <a href="https://cky-dot-nlp-visualizations.appspot.com/cky?sentence=James+ate+the+food" target="_blank">[<em>Optional:</em> Interactive CKY Demo]</a>
  </td>
</tr>

<tr><!--- Classification and Convolutional Networks-->
  <td><strong>Week&nbsp;5</strong><br>(Feb&nbsp;1)</td>
  <td>Classification and Sentiment (2.7 onwards)
  <p><p>
  <em>Note: you should review Async 5.3, 5.4, and 5.5.</em>
  </td>
  <td><ul>
  <li>Convolutional neural networks for NLP
  </ul></td>
  <td><ul>
  <li>Read: <a href="http://www.wildml.com/2015/11/understanding-convolutional-neural-networks-for-nlp/" target="_blank">Understanding Convolutional Neural Networks for NLP</a>
  <li>Read: <a href="https://arxiv.org/abs/1408.5882" target="_blank">Convolutional Neural Networks for Sentence Classification</a> (Yoon Kim, 2014)
</ul></td>
</tr>
<tr><!--- Language models and n-grams -->
  <td><strong>Week&nbsp;6</strong><br>(Feb&nbsp;8)</td>
  <td>Language Modeling I,
  <br>4.1-4.4,
  <br>5.8, 5.11</td>
  <td><ul>
    <li>LM applications
    <li>N-gram models
    <li>Smoothing methods
    <li>Representations of meaning
    <li>Distributed representations
    <li>Neural Net LMs
    <li>Word embeddings
    <li>Softmax variants
  </ul></td>
  <td>Language model introduction:<ul>
  <li>Skim: <a href="http://www.cs.berkeley.edu/~klein/cs294-5/chen_goodman.pdf" target="_blank">Chen and Goodman Survey</a>
  <li>Skim: <a href="http://arxiv.org/pdf/1312.3005.pdf" target="_blank">1 Billion Word Benchmark</a>
  <li><em>Optional:</em> <a href="http://norvig.com/ngrams/ch14.pdf" target="_blank">Natural Language Corpus Data (Peter Norvig)</a>
  </ul>
  <p>
  <a href="../materials/simple_lm/lm1.ipynb" target="_blank">[Language&nbsp;Modeling&nbsp;Notebook]</a>
  <p>
  Distributed representations:<ul>
  <li><em>Optional:</em> <a href="https://www.aclweb.org/anthology/J92-4003" target="_blank">Brown Clustering</a> (Brown et al. 1992)
  <li>Read: <a href="http://arxiv.org/pdf/1301.3781.pdf" target="_blank">CBOW and SkipGram</a> (Mikolov et al. 2013)
  <li><em>Optional:</em> <a href="http://colah.github.io/posts/2014-07-NLP-RNNs-Representations/" target="_blank">Deep Learning, NLP, and Representations</a> (Chris Olah's blog)
  <li>Read: <a href="http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf" target="_blank">A Neural Probabilistic Language Model</a> (Bengio et al. 2003)
  </ul>
  <p>
  <a href="../materials/embeddings/embeddings.ipynb" target="_blank">[Word&nbsp;Embeddings&nbsp;Notebook]</a>
  <br><a href="../materials/nplm/nplm.ipynb" target="_blank">[NPLM Notebook]</a>
  </td>
</tr>

<tr><!--- Extra Material -->
  <td><strong>Interlude (Extra Material)</strong></td>
  <td>Units of Meaning: Words, Morphology, Sentences</td>
  <td><ul>
  <li>Edit distance for strings
  <li>Tokenization
  <li>Sentence splitting
  </ul></td>
  <td><ul>
  <li><em>Skim:</em> <a href="http://www.nltk.org/book/ch03.html" target="_blank">NLTK book chapter 3</a> (processing raw text)
  <li><em>Skim:</em> <a href="http://norvig.com/ngrams/ch14.pdf" target="_blank">Natural Language Corpus Data</a> (Peter Norvig) <em>(if you didn't read in Week 2)</em>
  <li>Read: <a href="http://u.cs.biu.ac.il/~89-680/gillick2009.pdf" target="_blank">Sentence Boundary Detection and the Problem with the U.S.</a>
  <p>
  </ul></td>
</tr>

<tr><!--- Neural language models and RNNs -->
  <td><strong>Week&nbsp;7</strong><br>(Feb&nbsp;15)</td>
  <td>Language Modeling II</td>
  <td><ul>
  <li>Recurrent Neural Nets
  <li>State of the art: Advanced Embeddings and Transfer Learning
  </ul></td>
  <td><ul>
  <li><em>Read or skim:</em> <a href="http://neuralnetworksanddeeplearning.com/chap2.html" target="_blank">How the backpropagation algorithm works</a>
  <li>Read: <a href="http://colah.github.io/posts/2015-08-Understanding-LSTMs/" target="_blank">Understanding LSTM Networks</a> (Chris Olah's blog)
    <li><em>Optional:</em> <a href="https://arxiv.org/pdf/1802.05365.pdf" target="_blank">”Deep contextualized word representations”</a>, (Peters et al, 2018)
  <li><em>Optional (skim):</em> <a href="https://www.tensorflow.org/versions/master/tutorials/recurrent/index.html#recurrent-neural-networks" target="_blank">Tensorflow LSTM Language Model Tutorial</a>
  </ul>
  <p>
  <p>
  </td>
</tr>

<tr><!--- Week 8  -->
  <td><strong>Week&nbsp;8</strong><br>(Feb&nbsp;22)</td>
  <td>Machine Translation I
  <br>Machine Translation II</td>
  <td><ul>
  <li>Word- and phrase-based MT
  <li>IBM alignment models
  <li>Evaluation
  <li>Neural MT with sequence-to-sequence models and attention
  </ul></td>
  <td><ul>
  <li>Read: <a href="http://papers.nips.cc/paper/5346-sequence-to-sequence-learning-with-neural-networks.pdf" target="_blank">Sequence to Sequence Learning with Neural Networks</a>
  <li>Read: <a href="https://arxiv.org/pdf/1409.0473.pdf" target="_blank">Neural Machine Translation by Jointly Learning to Align and Translate</a>
  <li><em>Optional:</em> <a href="https://arxiv.org/abs/1609.08144" target="_blank">Google’s Neural Machine Translation System</a>
  <li><em>Optional:</em> <a href="http://distill.pub/2016/augmented-rnns/#attentional-interfaces" target="_blank">Attention and Augmented Recurrent Neural Networks</a> (section on “Attentional Interfaces” has an awesome visualization of an MT example, showing alignments)
  </ul></td>
  </tr>
  
  <tr><!--- Transformers  week 9  -->
  <td><strong>Week&nbsp;9</strong><br>(March&nbsp;1)</td>
  <td>No Async</td>
  <td><ul>
  <li>Self-Attention
  <li>Transformers
  <li>Transfer Learning
  </ul></td>
  <td><ul>
  <li><em>Read (skim):</em> <a href="https://arxiv.org/pdf/1706.03762.pdf" target="_blank">Attention is All You Need</a> (Vaswani et. al., 2017)
 <li><em>Read (skim):</em> <a href="https://arxiv.org/pdf/1810.04805v1.pdf" target="_blank">BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding”</a>, (Devlin et al, 2018)
 <li><em>Read (skim):</em> <a href="https://jalammar.github.io/illustrated-bert/" target="_blank">The Illustrated BERT, ELMo, and co. (How NLP Cracked Transfer Learning)”</a>, (Alammar, 2018)
  </ul>
  <p>
  </td>
</tr>

<tr><!--- Week 10 Entities -->
  <td><strong>Week&nbsp;10</strong><br>(March&nbsp;8)</td>
  <td>Entities</td>
  <td><ul>
  <li>From syntax to semantics
  <li>Named Entity Recognition
  <li>Coreference Resolution
  <li>Entity Linking
  <li>Information Extraction
  </ul></td>
  <td><ul>
  <li>Read: <a href="http://www.nltk.org/book/ch07.html" target="_blank">NLTK Book Chapter 7 (Extracting Information from Text)</a>
  <li><em>Optional:</em> <a href="http://www.aclweb.org/anthology/D09-1120" target="_blank">Simple Coreference Resolution with Rich Syntactic and Semantic Features</a> (Haghighi and Klein 2009, rule-based coreference)
  <li><em>Optional:</em> <a href="http://www.aclweb.org/anthology/P16-1061" target="_blank">Improving Coreference Resolution by Learning Entity-Level Distributed
  Representations</a> (Clark and Manning 2016, neural coreference)
  </ul>
  <p>
  </td>
</tr>



<tr><!--- Week 11 Summarization-->
  <td><strong>Week&nbsp;11</strong><br>(March&nbsp;15)</td>
  <td>Summarization</td>
  <td><ul>
  <li>Single- vs. multi-document summarization
  <li>Extractive and abstractive summarization
  <li>Classical summarization algorithms
  <li>Evaluating generated summaries
  <li>Neural summarization architectures
  </ul></td>
  <td><ul>
  <li>Skim: <a href="https://www.cs.cmu.edu/~afm/Home_files/Das_Martins_survey_summarization.pdf" target="_blank">A Survey on Automatic Text Summarization</a> (Das and Martins, 2007)
  <li>Read: <a href="https://arxiv.org/pdf/1509.00685v2.pdf" target="_blank">A Neural Attention Model for Abstractive Sentence Summarization</a> (Rush et al. 2015)
  <li><em>Optional:</em> <a href="https://arxiv.org/pdf/1704.04368.pdf" target="_blank">Get To The Point: Summarization with Pointer-Generator Networks</a> (See et al. 2017)
  </ul>
  <p>
  </td>
</tr>


 <tr><!--- No class  week 10 -->
  <td><strong>Spring Break</strong><br>(March&nbsp;22)</td>
  <td>No Async</td>
    <td>No class</td>
  <td>No Readings</td>
</tr>

 <tr><!--- Practical Machine Learning  week 10 -->
  <td><strong>Week&nbsp;12</strong><br>(March&nbsp;29)</td>
  <td>No Async</td>
  <td><ul>
  <li>Document Representation
  <li>Document Term Matrix
  <li>Document Vectors
  <li>Topic Modeling and LDA
  <li>Document Classification
  </ul></td>
  <td><ul>
    <li><em>Read (skim):</em> <a href="https://arxiv.org/pdf/1904.08398.pdf" target="_blank">DocBERT: BERT for Document Classification</a> (Adhikari et. al., 2019)
    <li><em>Read:</em> <a href="https://www.aclweb.org/anthology/N16-1174.pdf" target="_blank">Hierarchical Attention Networks for Document Classification</a> (Yang et. al., 2019)
  </ul>
  <p>
  </td>
</tr>

<tr><!--- Week 13 Information Retrieval -->
  <td><strong>Week&nbsp;13</strong><br>(April&nbsp;5)</td>
  <td>Information Retrieval</td>
  <td><ul>
  <li>Building a Search Index
  <li>Ranking
  <li>TF-IDF
  <li>Click signals
  <li>Neural IR models
  </ul></td>
  <td><ul>
  <li>Read: <a href="http://static.googleusercontent.com/media/research.google.com/en//archive/googlecluster-ieee.pdf" target="_blank">Web Search for a Planet</a> (Google)
  <li>Read: <a href="http://infolab.stanford.edu/~backrub/google.html" target="_blank">The Anatomy of a Large-Scale Hypertextual Web Search Engine</a>
  <li>Skim: <a href="http://nlp.stanford.edu/IR-book/pdf/irbookprint.pdf" target="_blank">"An Introduction to Information Retrieval", sections 6.2 and 6.3</a>
  <li><em>Optional:</em> <a href="http://ilpubs.stanford.edu:8090/422/1/1999-66.pdf" target="_blank">PageRank</a> (Page, et al. 1999)
  </ul>
  <p>
  </td>
</tr>


 <tr><!--- In class presentations week 10 -->
  <td><strong>Week&nbsp;14</strong><br>(April&nbsp;12)</td>
    <td></td>
  <td>In class project presentations</td>
  <td></td>
</tr>

</table>

Thanks for a great semester!
