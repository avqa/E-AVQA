import numpy as np

from nltk.corpus import wordnet as wn

word_pair_dict = {}


def acc_measure(a, b):
    return float(a == b)


# input: '狗' '猫'
def wups_word(pred, gt, similarity_threshold=0.0):
    if pred == gt:
        return 1.0

    dict_key = pred + ' ' + gt
    if dict_key in word_pair_dict:
        return word_pair_dict[dict_key]

    def get_semantic_field(word):
        return wn.synsets(word, lang='cmn')

    # print(gt, "***", pred)
    if gt == '纪念日':
        gt = '日'
    if pred == '纪念日':
        pred = '日'
    semantic_pred = get_semantic_field(pred)
    semantic_gt = get_semantic_field(gt)
    # print('{}: {}'.format(pred, semantic_pred))
    # print('{}: {}'.format(gt, semantic_gt))

    if semantic_pred == [] or semantic_gt == []:
        return 0.0

    # a的所有同义词和b的所有同义词遍历计算相似度，选择最大值
    global_max = 0
    for par_pred in semantic_pred:
        for par_gt in semantic_gt:
            local_score = par_pred.wup_similarity(par_gt)
            # print('{},{}: {}'.format(par_pred, par_gt, local_score))
            if local_score > global_max:
                global_max = local_score

    if global_max < similarity_threshold:
        wup_weight = 0.1
    else:
        wup_weight = 1.0

    word_final_score = global_max * wup_weight
    word_pair_dict[dict_key] = word_final_score

    return word_final_score


# input: '车 狗' '船 飞机'
def wups_wordset(pred, gt, threshold=0.0):
    # print(".........")
    # print(gt)
    # print("--------")
    # print(pred)
    gt_words = gt.split()
    pred_words = pred.split()

    pred_gt_score = 1
    for pred_word in pred_words:
        max_word_score = 0
        for gt_word in gt_words:
            word_score = wups_word(pred_word, gt_word, threshold)
            # print('word_score: {}'.format(word_score))
            if word_score > max_word_score:
                max_word_score = word_score
        # print('max_word_score: {}'.format(max_word_score))
        pred_gt_score *= max_word_score

    gt_pred_score = 1
    for gt_word in gt_words:
        max_word_score = 0
        for pred_word in pred_words:
            word_score = wups_word(pred_word, gt_word, threshold)
            # print('word_score: {}'.format(word_score))
            if word_score > max_word_score:
                max_word_score = word_score
        # print('max_word_score: {}'.format(max_word_score))
        gt_pred_score *= max_word_score

    # print(pred_gt_score)
    # print(gt_pred_score)
    answer_wups = min(pred_gt_score, gt_pred_score)

    return answer_wups


# input: (18000, ) ['我 是', '', ...]
def cal_wups(input_pred, input_gt, thresh):
    global word_pair_dict
    word_pair_dict = {}

    if thresh == -1:
        measure = acc_measure
    else:
        measure = lambda x, y: wups_wordset(x, y, thresh)

    if thresh == -1:
        pass
        # print('standard Accuracy is used')
    else:
        pass
        # print('soft WUPS is used')
    score_list = [measure(pred, gt) for (pred, gt) in zip(input_pred, input_gt)]
    # print(score_list)

    final_score = sum(map(lambda x: float(x) / float(len(score_list)), score_list))

    return final_score
