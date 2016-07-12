#! /usr/bin/python
#coding=gbk

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
       print(arg)
    print("-" * 40)         #打印40个-
    keys = sorted(keywords.keys())
    for kw in keys:
      print(kw, ":", keywords[kw])


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           "It's one",
           "It's two",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
