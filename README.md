# TaoAVQA

This repository contains the question, audio, and visual features we extracted for **TaoAVQA** dataset in the paper *Multi-Granularity Relational Attention Network with Contrastive Constraints for Tao-AVQA*.


## Statistics of TaoAVQA

Tao-AVQA dataset is different from other datasets since its questions are annotated based on raw audio. Tao-AVQA dataset consists of 34,033 QA pairs collected from 18,786 **e-commerce videos**. We collected our dataset on 12 categories (*e.g.* “sport”, “cosmetic tutorial”, and “quality goods reviews”) from Taobao, the largest e-commerce platform in China. To focus on various aspects of the videos and ensure the diversity of questions, we set QA pairs into four categories (*i.e.* Object, Action, Event, and Plot). The ratio of these four categories satisfies 3:2:1:2. 


### How to ask a question?

<style type="text/css">
.tg  {border-collapse:collapse;border-spacing:0;}
.tg td{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  overflow:hidden;padding:10px 5px;word-break:normal;}
.tg th{border-color:black;border-style:solid;border-width:1px;font-family:Arial, sans-serif;font-size:14px;
  font-weight:normal;overflow:hidden;padding:10px 5px;word-break:normal;}
.tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
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


### Categories of QA pairs


### Word clouds


### Quality Examples



## TaoAVQA Dataset

The question, audio, and visual features are available for download through the following links:
+ [TaoAVQA_bert_768.tar.gz](http://taocaption.oss-cn-hangzhou.aliyuncs.com/TaoAVQA/TaoAVQA_bert.tar.gz)
+ [TaoAVQA_i3d_2048.tar.gz](http://taocaption.oss-cn-hangzhou.aliyuncs.com/TaoAVQA/TaoAVQA_i3d.tar.gz)
+ [TaoAVQA_xlsr_512.tar.gz](http://taocaption.oss-cn-hangzhou.aliyuncs.com/TaoAVQA/TaoAVQA_xlsr.tar.gz)
