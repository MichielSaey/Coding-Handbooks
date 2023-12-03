# algorithm kmp_search

**Input:**

| variable | type                | description             |
|----------|---------------------|-------------------------|
| line     | array of characters | the text to be searched |
| word     | array of characters | the word sought         |

**Output:**

| variable         | type              | description                              |
|------------------|-------------------|------------------------------------------|
| match_possitions | array of integers | positions in line at which word is found |
| match_count      | interger          | number of matches found                  |


**Defined variables:**

| variable      | type              | description                                   |
|---------------|-------------------|-----------------------------------------------|
| index_in_line | integer           | the position of the current character in line |
| index_in_word | integer           | the position of the current character in word |
| sigman_table  | array of integers | return value from kmp_table                   |


```pseudo
match_count = 0

while index_in_line < length(line):
    if word[index_in_word] = line[index_in_line]:
        ++index_in_line
        ++index_in_word
        if index_in_word = length(word):
            # occurrence found 
            # if only first occurrence is needed: 
                match_possitions = index_in_line - index_in_word
            # else:
            match_possitions[match_count] = index_in_line - index_in_word
            match_count++
            index_in_word = sigman_table[index_in_word]
    else:
        index_in_word = sigman_table[index_in_word]
        if index_in_word < 0:
            index_in_line++
            index_in_word++
```

# algorithm kmp_table:
**Input:**

| variable | type                | description             |
|----------|---------------------|-------------------------|
| word     | array of characters | the word to be analyzed |

**Output:**

| variable | type              | description                              |
|----------|-------------------|------------------------------------------|
| table    | array of integers | the table to be filled                   |

**Define variables:**

| variable       | type    | description                                                                | value |
|----------------|---------|----------------------------------------------------------------------------|-------|
| index_in_table | integer | the current position we are computing in table                             | 1     |
| index_in_word  | integer | the index in word of the next character of the current candidate substring | 0     |

```pseudo
table[0] = -1

while index_in_table < length(W):
    if W[index_in_table] = W[index_in_word]:
        table[index_in_table] = table[index_in_word]
    else:
        table[index_in_table] = index_in_word
        while index_in_word >= 0 and word[index_in_table] ≠ word[index_in_word]:
            index_in_word = table[index_in_word]
        index_in_table++
        index_in_word++

    table[index_in_table] = index_in_word (only needed when all word occurrences are searched)
```