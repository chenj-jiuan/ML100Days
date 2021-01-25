#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt


# In[4]:


w=3
b=0.5
x_lin = np.linspace(0, 100, 101)
y = (x_lin + np.random.randn(101) * 5) * w + b
plt.plot(x_lin, y, 'b.', label = 'data points')
plt.title("Assume we have data points")
plt.legend(loc = 2)
plt.show()


# In[5]:


y_hat = x_lin * w + b
plt.plot(x_lin, y, 'b.', label = 'data')
plt.plot(x_lin, y_hat, 'r-', label = 'prediction')
plt.title("Assume we have data points (And the prediction)")
plt.legend(loc = 2)
plt.show()


# In[ ]:


1. 你選的這組資料為何重要
Music Label Dataset，其重要的原因是因為可以透過資料的方式來合成的音樂數據。
2. 資料從何而來 (tips: 譬如提供者是誰、以什麼方式蒐集)
提供者為Revil Rosa，透過csv轉譯分析方式
3. 蒐集而來的資料型態為何
csv，編碼而成
4. 這組資料想解決的問題如何評估
評估其供給的Column後所呈現的資料來判斷


# In[ ]:


想像你經營一個自由載客車隊，你希望能透過數據分析以提升業績，請你思考並描述你如何規劃整體的分析/解決方案：
1. 核心問題為何 (tips：如何定義 「提升業績 & 你的假設」)
數據分析提升業績，相對於過去業績來進行比較，看其是否提升多少個百分點
假設：增加需求多的路段車輛是否可提升自由車隊的載客量？
2. 資料從何而來 (tips：哪些資料可能會對你想問的問題產生影響 & 資料如何蒐集)
因本身為自由載客車隊，故在蒐集資料上可以透過公開資料，包含中華車隊或是說uber等資料來進行分析
認為可以透過路段的分析方式，看哪個位置較多人會叫車，並透過車隊的數據資料來發現到其價格區間及接受度，因其為可能影響因素
3. 蒐集而來的資料型態為何
非結構化：口述、文字及結構化的數值資料
4. 你要回答的問題，其如何評估 (tips：你的假設如何驗證)
透過文字探勘或是熱點分析等方式來評估，來驗證結果

