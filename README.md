# TaoAVQA

This repository contains the question, audio, and visual features we extracted for **TaoAVQA** dataset in the paper *Multi-Granularity Relational Attention Network with Contrastive Constraints for Tao-AVQA*.


## Statistics of TaoAVQA

Tao-AVQA dataset is different from other datasets since its questions are annotated based on raw audio. Tao-AVQA dataset consists of 34,033 QA pairs collected from 18,786 **e-commerce videos**. We collected our dataset on 12 categories (*e.g.* “sport”, “cosmetic tutorial”, and “quality goods reviews”) from Taobao, the largest e-commerce platform in China.


### How to ask a question?

Note that the template here is only for the annotator to learn and reference, not mandatory. This is to ensure the diversity of our data. The specific template sentences are displayed as follows. Our template is displayed in English, but Chinese is used in the actual application.

<table class="tg">
<thead>
  <tr>
    <th class="tg-c3ow">Category</th>
    <th class="tg-c3ow">Finer Category</th>
    <th class="tg-c3ow">Questions</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-c3ow" rowspan="4">Object</td>
    <td class="tg-c3ow" rowspan="2">Definition</td>
    <td class="tg-0pky">What is/are the [sub]?</td>
  </tr>
  <tr>
    <td class="tg-0pky">Who is the man/woman?</td>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="2">Attribute</td>
    <td class="tg-0pky">What's the [attr] of [sub]</td>
  </tr>
  <tr>
    <td class="tg-0pky">How many [obj]/[location]?</td>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="4">Action</td>
    <td class="tg-c3ow">Definition</td>
    <td class="tg-0pky">What does the [sub] do?</td>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="3">Element</td>
    <td class="tg-0pky">How does the [sub] do?</td>
  </tr>
  <tr>
    <td class="tg-0pky">What's the [obj] of [action]?</td>
  </tr>
  <tr>
    <td class="tg-0pky">How many times does [action]?</td>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="2">Event</td>
    <td class="tg-c3ow">Process</td>
    <td class="tg-0pky">(how) What's the process?</td>
  </tr>
  <tr>
    <td class="tg-c3ow">Cause</td>
    <td class="tg-0pky">Why does [sub] do [obj]?</td>
  </tr>
  <tr>
    <td class="tg-c3ow" rowspan="2">Plot</td>
    <td class="tg-c3ow" rowspan="2">-</td>
    <td class="tg-0pky">What is the video about?</td>
  </tr>
  <tr>
    <td class="tg-0pky">What's the weather like?</td>
  </tr>
</tbody>
</table>


### What modalities a question needs to be answered?

<!-- ![](/images/veien_fig.png) -->
<img src="/images/veien_fig.png" alt="drawing" width="400"/>

Our dataset is challenging, as 11.32% of the data requires a combination of audio-visual cues to arrive at the correct answers. In addition, 20% of the data can use audio information, including speech and surrounding sound.


### Categories of QA pairs

<img src="/images/catg.png" alt="drawing" width="500"/>

To focus on various aspects of the videos and ensure the diversity of questions, we set QA pairs into four categories (*i.e.* Object, Action, Event, and Plot). The ratio of these four categories satisfies 3:2:1:2. 


### Word clouds

<table>
  <thead>
    <tr>
      <th><img src="/images/fig_qwords.png" alt="drawing" width="600"/></th>
      <th><img src="/images/fig_awords.png" alt="drawing" width="600"/></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Word cloud for question texts</td>
      <td>Word cloud for answer texts</td>
    </tr>
  </tbody>
</table>


### Quality Examples

<img src="/images/qe.png" alt="drawing" width="400"/>

The red words only can be generated leveraging audio content. The blue words can be obtained by visual or audio information. Words in green indicate poor performance. Case (a), (b) and (c) are quality instances for the AVQA task. Case (d) displays our unique words in e-commerce scenarios.


## TaoAVQA Dataset

The question, audio, and visual features are available for download through the following links:
+ [TaoAVQA_bert_768.tar.gz](http://taocaption.oss-cn-hangzhou.aliyuncs.com/TaoAVQA/TaoAVQA_bert.tar.gz)
+ [TaoAVQA_i3d_2048.tar.gz](http://taocaption.oss-cn-hangzhou.aliyuncs.com/TaoAVQA/TaoAVQA_i3d.tar.gz)
+ [TaoAVQA_xlsr_512.tar.gz](http://taocaption.oss-cn-hangzhou.aliyuncs.com/TaoAVQA/TaoAVQA_xlsr.tar.gz)
