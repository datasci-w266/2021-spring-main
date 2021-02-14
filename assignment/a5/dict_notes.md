# Python Dictionaries: Advanced Use

Dictionaries are a straightforward and powerful way to build a sparse map, such as our n-gram counts, and we'll make extensive use of them in Part 1 to build our language model.

We assume some familiarity with the basics of Python `dicts`; if not, we recommend looking over the Python tutorial here: [5.5. Dictionaries](https://docs.python.org/3/tutorial/datastructures.html#dictionaries).

## enumerate()

This isn't strictly for dictionaries, but it's an incredibly powerful builtin for iterating through a list along with indices. To loop normally, you might do:
```python
for elem in my_collection:
  # do something with elem
```
If you also want to get unique indices corresponding to the iteration order, do:
```python
for i, elem in enumerate(my_collection):
  # i = 0, 1, 2, ...
  # elem as above
```

Of course, you can also use it inside list (or dict or set) comprehensions as well. Here's a practical example, similar to how `vocabulary.py` is implemented:
```python
wordlist = set(tokens)  # de-dupe
# map each word to a unique id
word_to_id = {word:idx for idx, word in enumerate(wordlist)}
```

*See [5.6. Looping Techniques](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques) for more.*

## items()

To iterate over both the *keys* and the *values* of a dictionary at once, use `items`:
```python
for key, value in my_dict.items():
  # do something
```

*See [5.6. Looping Techniques](https://docs.python.org/3/tutorial/datastructures.html#looping-techniques) for more.*

## defaultdict and dict.get():

It's a common pattern to check if values exist in a dictionary before retrieving them, or to add a default value before modifying (such as incrementing) it. The naive way of doing this is somewhat tedious, but Python provides [`collections.defaultdict`](https://docs.python.org/3.6/library/collections.html#collections.defaultdict) and [`dict.get()`](https://docs.python.org/3/library/stdtypes.html#dict.get), which can make this process much easier.

Suppose you want to increment a value by 1, or add it if it does not exist. Here's a naive version:
```python
d = dict()
# (...)
if not key in d:
  d[key] = 0
d[key] += 1
```
A cleaner way uses `defaultdict`, which automatically constructs a default value:
```python
d = collections.defaultdict(lambda: 0)
# (...)
d[key] += 1
```
Note that the argument to the constructor is a *function* which takes zero arguments and furnishes a default value on each call. *This value gets automatically inserted into the dict!*

In another case, you might want to get a default value *without* modifying the dictionary. For that, use `.get()`:
```python
val = d.get(key, 0)
```
You can also return richer types:
```python
# nested_d maps key -> dict
d = nested_d.get(key, {})
```
Or even chain it:
```python
# nested_d maps key -> dict -> int
d = nested_d.get(key_1, {})
val = d.get(key_2, 0)
```

*See [`dict.get()`](https://docs.python.org/3/library/stdtypes.html#dict.get) and [`collections.defaultdict`](https://docs.python.org/3.6/library/collections.html#collections.defaultdict) for more.*
