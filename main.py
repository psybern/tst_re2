import re

with open('txt.txt', 'r', encoding='utf-8') as orig_txt:
    text_read = orig_txt.read()
    orig_txt.close()
    txt_filter = re.sub(r"[\([{«,.'':;—»})\]*#%^]", "", text_read)
    txt_low_reg = txt_filter.lower()
    txt_slt = txt_low_reg.split()

    print(len(txt_slt))  
    print(len(set(txt_slt)))
