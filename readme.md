# Python txt/csv file cleaner

## Currently replaces words with double pipe.

Add words you'd like to be replaced in the replace_these_words array.  

### Currently searching through pipe delimited files.  

If you wanted to use comma delimited you would need to change what is being replaced:  
```python
line = line.replace(word, "||")
```

### Examples: of words I would place inside that array |Null| (case sensitive) 

```python
replace_these_words = [
    '|Null|',
    '|None|',
] 
```

### If you wanted to skip a folder to not alter add the folder name to (case sensitive):

```python
folders_to_exclude = [
    'exampleFolder'
]
```

Script would replace the above words with empty ||

## Currently set up to search through main directory of client directories
    
    |--MainDirectory
        |--ClientA
            |--Archive(dir)
            --Filestobecleaned
        |--ClientB
            |--Archive(dir)
            --Filestobecleaned
            --Filestobecleaned
            --Filestobecleaned
        |--ClientC
            |--Archive(dir)
            --Filestobecleaned
