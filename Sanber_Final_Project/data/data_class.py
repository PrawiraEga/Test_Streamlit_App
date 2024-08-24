class data_class:
    def __init__(self, list_text, list_txt_one, list_txt_two):
        self.list_text = list_text
        self.list_txt_one = list_txt_one
        self.list_txt_two = list_txt_two
        self.merge = True

    def merge_list(self, list_txt_one, list_txt_two):
        if self.merge == True:
            list_text = list_txt_one + list_txt_two
            return list_text
        
    def separate_list(self):
        self.merge = False    