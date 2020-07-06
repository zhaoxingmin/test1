import numpy as np
import json
# a= [[0.01014794,0.989852]]
# b = np.array(a)
# c=[]
# c.append(a)
# print(b)
# #print(b.tostring())
# d = json.loads('[[0.01014794,0.989852]]')
# print(d)

# sent = [("我是生命人寿保险公司郑州中。", "我是件，请您核对",  "我是德件，请您核对"), ('我喜欢看电影', '看电影我喜欢'), ('我喜欢看电影', '看电影我喜欢')]
# a = sent[0]
# b = sent[1]
# c = a[0]
# d =1
features = {"input_ids":[1.0,1.1,1.2,1.3] ,"input_mask":[2.0,2.1,2.2,2.3]}

input_ids = [1.1, 1.2, 1.3]
input_mask = [2.1, 2.2, 2.3]
segment_ids = [3.1, 3.2, 3.3]
label_ids = [4.1, 4.2, 4.3]

datas = {'inputs': {'input_ids': input_ids, 'input_mask': input_mask, 'segment_ids': segment_ids, 'label_ids': label_ids}}
datas = {
    'instances': [{'input_ids': input_ids[0], 'input_mask': input_mask[0], 'segment_ids': segment_ids[0],
                   'label_ids': label_ids[0]},
                  {'input_ids': input_ids[1], 'input_mask': input_mask[1], 'segment_ids': segment_ids[1],
                   'label_ids': label_ids[1]}]
}
#[f.label_id for f in features]
a= [f for f in input_ids]
b=1
# 'instances': [{'input_ids': input_ids[0], 'input_mask': input_mask[0], 'segment_ids': segment_ids[0],'label_ids':
# label_ids[0]}, {'input_ids': input_ids[1], 'input_mask': input_mask[1], 'segment_ids': segment_ids[1],'label_ids':
# label_ids[1]}]
x=[]
ins = {'instances':x}

# a= {}
# a['input_ids']=input_ids[0]
# a['input_mask']=input_mask[0]
# a['segment_ids']=segment_ids[0]
# print(a)


a = [[1,2,3],[4,5,6]]

b=[f for f in a]
print(b)
print(b[0])




