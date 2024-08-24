class data_sentiment:
    def __init__(self, list_sentim, list_sentim_one, list_sentim_two):
        self.list_sentim = list_sentim
        self.list_sentim_one = list_sentim_one
        self.list_sentim_two = list_sentim_two
        self.merge = True

    def avg_sentim(self, sentim_one, sentim_two):
        if self.merge == True:
            avg_sentim = sentim_one + sentim_two
            return avg_sentim
        
    def separate_list(self):
        self.merge = False  

    def label_to_score(self, sentim_label):
        if self.merge == True:
            if sentim_label == 'POSITIVE':
                vals = 1
            elif sentim_label == 'NEGATIVE':    
                vals = -1
            else:
                vals = 0
            return vals

    def fin_sum(self, sentim_vals):
        if sentim_vals > 0:
            fin_sum = 'POSITIVE'
        elif sentim_vals < 0:
            fin_sum = 'NEGATIVE'
        else:
            fin_sum = 'NEUTRAL'
        return fin_sum            