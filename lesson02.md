```python

import numpy as np
a = ([1,6],[2,8],[3,11],[3,10], [1,7])

mean_a =np.mean(a)
print(mean_a)

```

    5.2
    


```python
a_centred = a - mean_a
print(a_centred)

```

    [[ 4.2 -0.8]
     [ 3.2 -2.8]
     [ 2.2 -5.8]
     [ 2.2 -4.8]
     [ 4.2 -1.8]]
    


```python
a_centred_sp = a_centred.T[0] @ a_centred.T[1]
print(a_centred_sp)
```

    -43.199999999999996
    


```python
a_centred_sp/(a_centred[0] - 1)
```




    array([-13.5,  24. ])




```python
m = np.transpose(a)
m_cov = np.cov(m)
print(m_cov)
```

    [[1.  2. ]
     [2.  4.3]]
    


```python
import pandas as pd
authors = pd.DataFrame({'author_id':[1,2,3],'author_name':['Тургенев', 'Чехов', 'Островский']},columns = ['author_id','author_name'])
print(authors)
```

       author_id author_name
    0          1    Тургенев
    1          2       Чехов
    2          3  Островский
    


```python
import pandas as pd
authors = pd.DataFrame({'author_id':[1,2,3],'author_name':['Тургенев', 'Чехов', 'Островский']},columns = ['author_id','author_name'])
print(authors)
```

       author_id            book_title  price
    0          1           Отцы и дети    450
    1          1                 Рудин    300
    2          1     Дворянское гнездо    350
    3          2      Толстый и тонкий    500
    4          2       Дама с собачкой    450
    5          3                 Гроза    370
    6          3  Таланты и поклонники    290
    


```python
authors_price = pd.merge(authors, books, on = 'author_id', how = 'outer')
print(authors_price)
```

       author_id author_name            book_title  price
    0          1    Тургенев           Отцы и дети    450
    1          1    Тургенев                 Рудин    300
    2          1    Тургенев     Дворянское гнездо    350
    3          2       Чехов      Толстый и тонкий    500
    4          2       Чехов       Дама с собачкой    450
    5          3  Островский                 Гроза    370
    6          3  Островский  Таланты и поклонники    290
    


```python
top5 = authors_price.nlargest(5,'price')
print(top5)
```

       author_id author_name         book_title  price
    3          2       Чехов   Толстый и тонкий    500
    0          1    Тургенев        Отцы и дети    450
    4          2       Чехов    Дама с собачкой    450
    5          3  Островский              Гроза    370
    2          1    Тургенев  Дворянское гнездо    350
    


```python
authors_stat = authors_price.value_counts()
print(authors_stat)
```

    author_id  author_name  book_title            price
    1          Тургенев     Дворянское гнездо     350      1
                            Отцы и дети           450      1
                            Рудин                 300      1
    2          Чехов        Дама с собачкой       450      1
                            Толстый и тонкий      500      1
    3          Островский   Гроза                 370      1
                            Таланты и поклонники  290      1
    dtype: int64
    


```python
authors_price['cover'] = ['твердая', 'мягкая', 'мягкая', 'твердая', 'твердая', 'мягкая', 'мягкая'] 
print(authors_price)

```

       author_id author_name            book_title  price    cover
    0          1    Тургенев           Отцы и дети    450  твердая
    1          1    Тургенев                 Рудин    300   мягкая
    2          1    Тургенев     Дворянское гнездо    350   мягкая
    3          2       Чехов      Толстый и тонкий    500  твердая
    4          2       Чехов       Дама с собачкой    450  твердая
    5          3  Островский                 Гроза    370   мягкая
    6          3  Островский  Таланты и поклонники    290   мягкая
    


```python
book_info = pd.pivot_table(authors_price, values='price', index=['author_name'], columns=['cover'], aggfunc=np.sum)
book_info['мягкая'] = book_info['мягкая'].fillna(0)
book_info['твердая'] = book_info['твердая'].fillna(0)
print(book_info)
```

    cover        мягкая  твердая
    author_name                 
    Островский    660.0      0.0
    Тургенев      650.0    450.0
    Чехов           0.0    950.0
    


```python

```
