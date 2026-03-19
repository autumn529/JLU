import numpy as np
import re

def calculate_multiclass_metrics(y_true, y_pred, actural_class):

    all_labels = list(set(y_true).union(set(y_pred)))


    num_classes = len(all_labels)
    conf_matrix = np.zeros((num_classes, num_classes), dtype=int)


    label_to_index = {label: idx for idx, label in enumerate(all_labels)}

    for t, p in zip(y_true, y_pred):
        true_index = label_to_index[t]
        pred_index = label_to_index[p]
        conf_matrix[true_index][pred_index] += 1


    accuracy = sum(conf_matrix[i][i] for i in range(num_classes)) / len(y_true)


    precision_per_class = []
    for i in range(num_classes):
        tp = conf_matrix[i][i]
        fp = sum(conf_matrix[:, i]) - tp
        precision = tp / (tp + fp) if (tp + fp) != 0 else 0
        precision_per_class.append(precision)
    precision = np.sum(precision_per_class) / actural_class


    recall_per_class = []
    for i in range(num_classes):
        tp = conf_matrix[i][i]
        fn = sum(conf_matrix[i, :]) - tp
        recall = tp / (tp + fn) if (tp + fn) != 0 else 0
        recall_per_class.append(recall)
    recall = np.sum(recall_per_class)/actural_class


    f1_per_class = []
    for i in range(num_classes):
        precision_each_class = precision_per_class[i]
        recall_each_class = recall_per_class[i]
        if (precision_each_class + recall_each_class) != 0:
            f1 = 2 * (precision_each_class * recall_each_class) / (precision_each_class + recall_each_class)
        else:
            f1 = 0
        f1_per_class.append(f1)
    f1 = np.sum(f1_per_class)/actural_class


    return {
        "confusion_matrix": conf_matrix,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1_score": f1,
    }



def remove_special_chars(s):
    pattern = r"[^a-zA-Z0-9\s]"
    s = re.sub(pattern, "", s)
    return s


def has_word(sentence, word):
    pattern = r"\b" + re.escape(word) + r"\b"
    match = re.search(pattern, sentence)
    if match:
        return True
    else:
        return False

def label_regular(output):
    eval = VQAEval()
    if  eval.evaluate(output, 'Finish[TEXT REFUTES]'):
        bina_predict_label = 1
        multiclass_predict_label = 1
    elif eval.evaluate(output, 'Finish[IMAGE REFUTES]'):
        bina_predict_label = 1
        multiclass_predict_label = 2
    elif eval.evaluate(output, 'Finish[MISMATCH]'):
        bina_predict_label = 1
        multiclass_predict_label = 3
    elif eval.evaluate(output, 'Finish[ORIGINAL]') or eval.evaluate(output, 'Finish[MATCH]'):
        bina_predict_label = 0
        multiclass_predict_label = 0
    else:
        X_num += 1
        bina_predict_label = 'X'
        multiclass_predict_label = 'X'
    return bina_predict_label, multiclass_predict_label


class VQAEval:
    def __init__(self):
        self.contractions = {
            "aint": "ain't",
            "arent": "aren't",
            "cant": "can't",
            "couldve": "could've",
            "couldnt": "couldn't",
            "couldn'tve": "couldn't've",
            "couldnt've": "couldn't've",
            "didnt": "didn't",
            "doesnt": "doesn't",
            "dont": "don't",
            "hadnt": "hadn't",
            "hadnt've": "hadn't've",
            "hadn'tve": "hadn't've",
            "hasnt": "hasn't",
            "havent": "haven't",
            "hed": "he'd",
            "hed've": "he'd've",
            "he'dve": "he'd've",
            "hes": "he's",
            "howd": "how'd",
            "howll": "how'll",
            "hows": "how's",
            "Id've": "I'd've",
            "I'dve": "I'd've",
            "Im": "I'm",
            "Ive": "I've",
            "isnt": "isn't",
            "itd": "it'd",
            "itd've": "it'd've",
            "it'dve": "it'd've",
            "itll": "it'll",
            "let's": "let's",
            "maam": "ma'am",
            "mightnt": "mightn't",
            "mightnt've": "mightn't've",
            "mightn'tve": "mightn't've",
            "mightve": "might've",
            "mustnt": "mustn't",
            "mustve": "must've",
            "neednt": "needn't",
            "notve": "not've",
            "oclock": "o'clock",
            "oughtnt": "oughtn't",
            "ow's'at": "'ow's'at",
            "'ows'at": "'ow's'at",
            "'ow'sat": "'ow's'at",
            "shant": "shan't",
            "shed've": "she'd've",
            "she'dve": "she'd've",
            "she's": "she's",
            "shouldve": "should've",
            "shouldnt": "shouldn't",
            "shouldnt've": "shouldn't've",
            "shouldn'tve": "shouldn't've",
            "somebody'd": "somebodyd",
            "somebodyd've": "somebody'd've",
            "somebody'dve": "somebody'd've",
            "somebodyll": "somebody'll",
            "somebodys": "somebody's",
            "someoned": "someone'd",
            "someoned've": "someone'd've",
            "someone'dve": "someone'd've",
            "someonell": "someone'll",
            "someones": "someone's",
            "somethingd": "something'd",
            "somethingd've": "something'd've",
            "something'dve": "something'd've",
            "somethingll": "something'll",
            "thats": "that's",
            "thered": "there'd",
            "thered've": "there'd've",
            "there'dve": "there'd've",
            "therere": "there're",
            "theres": "there's",
            "theyd": "they'd",
            "theyd've": "they'd've",
            "they'dve": "they'd've",
            "theyll": "they'll",
            "theyre": "they're",
            "theyve": "they've",
            "twas": "'twas",
            "wasnt": "wasn't",
            "wed've": "we'd've",
            "we'dve": "we'd've",
            "weve": "we've",
            "werent": "weren't",
            "whatll": "what'll",
            "whatre": "what're",
            "whats": "what's",
            "whatve": "what've",
            "whens": "when's",
            "whered": "where'd",
            "wheres": "where's",
            "whereve": "where've",
            "whod": "who'd",
            "whod've": "who'd've",
            "who'dve": "who'd've",
            "wholl": "who'll",
            "whos": "who's",
            "whove": "who've",
            "whyll": "why'll",
            "whyre": "why're",
            "whys": "why's",
            "wont": "won't",
            "wouldve": "would've",
            "wouldnt": "wouldn't",
            "wouldnt've": "wouldn't've",
            "wouldn'tve": "wouldn't've",
            "yall": "y'all",
            "yall'll": "y'all'll",
            "y'allll": "y'all'll",
            "yall'd've": "y'all'd've",
            "y'alld've": "y'all'd've",
            "y'all'dve": "y'all'd've",
            "youd": "you'd",
            "youd've": "you'd've",
            "you'dve": "you'd've",
            "youll": "you'll",
            "youre": "you're",
            "youve": "you've",
        }
        self.manualMap = {
            "none": "0",
            "zero": "0",
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9",
            "ten": "10",
        }
        self.articles = ["a", "an", "the"]

        self.periodStrip = re.compile("(?!<=\d)(\.)(?!\d)")
        self.commaStrip = re.compile("(\d)(\,)(\d)")
        self.punct = [
            ";",
            r"/",
            "[",
            "]",
            '"',
            "{",
            "}",
            "(",
            ")",
            "=",
            "+",
            "\\",
            "_",
            "-",
            ">",
            "<",
            "@",
            "`",
            ",",
            "?",
            "!",
        ]

    def evaluate(self, answer, gt_answers):
        answer = answer.replace("\n", " ")
        answer = answer.replace("\t", " ")
        answer = answer.strip()
        answer = self.processPunctuation(answer)
        answer = self.processDigitArticle(answer)
        if type(gt_answers)==list:
            for i in range(len(gt_answers)):
                gt_answers[i] = gt_answers[i].replace("\n", " ")
                gt_answers[i] = gt_answers[i].replace("\t", " ")
                gt_answers[i] = gt_answers[i].strip()
                gt_answers[i] = self.processPunctuation(gt_answers[i])
                gt_answers[i] = self.processDigitArticle(gt_answers[i])
                if has_word(answer, gt_answers[i]):
                    return 1
            return 0
        else:
            gt_answers = gt_answers.replace("\n", " ")
            gt_answers= gt_answers.replace("\t", " ")
            gt_answers = gt_answers.strip()
            gt_answers = self.processPunctuation(gt_answers)
            gt_answers = self.processDigitArticle(gt_answers)
            if has_word(answer, gt_answers):
                return 1
            else:
                return 0
    
    def evaluate_MRR(self, answer, gt_answers):
        answer = answer.replace("\n", " ")
        answer = answer.replace("\t", " ")
        answer = answer.strip()
        answer = self.processPunctuation(answer)
        answer = self.processDigitArticle(answer)
        if type(gt_answers) is str:
            gt_answers = [gt_answers]
        for i in range(len(gt_answers)):
            gt_answers[i] = gt_answers[i].replace("\n", " ")
            gt_answers[i] = gt_answers[i].replace("\t", " ")
            gt_answers[i] = gt_answers[i].strip()
            gt_answers[i] = self.processPunctuation(gt_answers[i])
            gt_answers[i] = self.processDigitArticle(gt_answers[i])
            if has_word(answer, gt_answers[i]):
                return 1 / (i + 1)
        return 0.0

    def processPunctuation(self, inText):
        outText = inText
        for p in self.punct:

            if (p + " " in inText or " " + p in inText):
                outText = outText.replace(p, "")
            else:
                outText = outText.replace(p, " ")
        outText = self.periodStrip.sub("", outText, re.UNICODE)
        return outText

    def processDigitArticle(self, inText):
        outText = []
        tempText = inText.lower().split()
        for word in tempText:
            word = self.manualMap.setdefault(word, word)
            if word not in self.articles:
                outText.append(word)
            else:
                pass
        for wordId, word in enumerate(outText):
            if word in self.contractions:
                outText[wordId] = self.contractions[word]
        outText = " ".join(outText)
        return outText