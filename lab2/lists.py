{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "fruits = ['apple', 'banana', 'cherry']\n",
    "\n",
    "x = fruits.count(\"cherry\")\n",
    "print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'b', 'c', 1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "list1 = [\"a\", \"b\" , \"c\"]\n",
    "list2 = [1, 2, 3]\n",
    "\n",
    "list1.extend(list2)\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'b', 'c', 1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "list1 = [\"a\", \"b\" , \"c\"]\n",
    "list2 = [1, 2, 3]\n",
    "\n",
    "for x in list2:\n",
    "  list1.append(x)\n",
    "\n",
    "print(list1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'b', 'c', 1, 2, 3]\n"
     ]
    }
   ],
   "source": [
    "list1 = [\"a\", \"b\", \"c\"]\n",
    "list2 = [1, 2, 3]\n",
    "\n",
    "list3 = list1 + list2\n",
    "print(list3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana', 'cherry']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "mylist = thislist[:]\n",
    "print(mylist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana', 'cherry']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "mylist = thislist.copy()\n",
    "print(mylist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['cherry', 'Kiwi', 'Orange', 'banana']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"banana\", \"Orange\", \"Kiwi\", \"cherry\"]\n",
    "thislist.reverse()\n",
    "print(thislist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['banana', 'cherry', 'Kiwi', 'Orange']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"banana\", \"Orange\", \"Kiwi\", \"cherry\"]\n",
    "thislist.sort(key = str.lower)\n",
    "print(thislist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[50, 65, 23, 82, 100]\n"
     ]
    }
   ],
   "source": [
    "def myfunc(n):\n",
    "  return abs(n - 50)\n",
    "\n",
    "thislist = [100, 50, 65, 82, 23]\n",
    "thislist.sort(key = myfunc)\n",
    "print(thislist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[100, 82, 65, 50, 23]\n"
     ]
    }
   ],
   "source": [
    "thislist = [100, 50, 65, 82, 23]\n",
    "thislist.sort(reverse = True)\n",
    "print(thislist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['pineapple', 'orange', 'mango', 'kiwi', 'banana']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"orange\", \"mango\", \"kiwi\", \"pineapple\", \"banana\"]\n",
    "thislist.sort(reverse = True)\n",
    "print(thislist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['banana', 'kiwi', 'mango', 'orange', 'pineapple']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"orange\", \"mango\", \"kiwi\", \"pineapple\", \"banana\"]\n",
    "thislist.sort()\n",
    "print(thislist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']\n"
     ]
    }
   ],
   "source": [
    "fruits = [\"apple\", \"banana\", \"cherry\", \"kiwi\", \"mango\"]\n",
    "\n",
    "newlist = [x.upper() for x in fruits]\n",
    "\n",
    "print(newlist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n"
     ]
    }
   ],
   "source": [
    "newlist = [x for x in range(10)]\n",
    "\n",
    "print(newlist)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['banana', 'cherry', 'kiwi', 'mango']\n"
     ]
    }
   ],
   "source": [
    "fruits = [\"apple\", \"banana\", \"cherry\", \"kiwi\", \"mango\"]\n",
    "\n",
    "newlist = [x for x in fruits if x != \"apple\"]\n",
    "\n",
    "print(newlist)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana', 'mango']\n"
     ]
    }
   ],
   "source": [
    "fruits = [\"apple\", \"banana\", \"cherry\", \"kiwi\", \"mango\"]\n",
    "\n",
    "newlist = [x for x in fruits if \"a\" in x]\n",
    "\n",
    "print(newlist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana', 'mango']\n"
     ]
    }
   ],
   "source": [
    "fruits = [\"apple\", \"banana\", \"cherry\", \"kiwi\", \"mango\"]\n",
    "newlist = []\n",
    "\n",
    "for x in fruits:\n",
    "  if \"a\" in x:\n",
    "    newlist.append(x)\n",
    "\n",
    "print(newlist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apple\n",
      "banana\n",
      "cherry\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[None, None, None]"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "[print(x) for x in thislist]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apple\n",
      "banana\n",
      "cherry\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "i = 0\n",
    "while i < len(thislist):\n",
    "  print(thislist[i])\n",
    "  i = i + 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apple\n",
      "banana\n",
      "cherry\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "for i in range(len(thislist)):\n",
    "  print(thislist[i])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "apple\n",
      "banana\n",
      "cherry\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "for x in thislist:\n",
    "  print(x)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[]\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "thislist.clear()\n",
    "print(thislist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['banana', 'cherry']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "del thislist[0]\n",
    "print(thislist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "thislist.pop()\n",
    "print(thislist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'cherry']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "thislist.pop(1)\n",
    "print(thislist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'cherry']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "thislist.remove(\"banana\")\n",
    "print(thislist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "tropical = [\"mango\", \"pineapple\", \"papaya\"]\n",
    "thislist.extend(tropical)\n",
    "print(thislist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana', 'cherry', 'orange']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "thislist.append(\"orange\")\n",
    "print(thislist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana', 'watermelon', 'cherry']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "thislist.insert(2, \"watermelon\")\n",
    "print(thislist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'watermelon']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "thislist[1:3] = [\"watermelon\"]\n",
    "print(thislist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\", \"orange\", \"kiwi\", \"mango\"]\n",
    "thislist[1:3] = [\"blackcurrant\", \"watermelon\"]\n",
    "print(thislist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'blackcurrant', 'cherry']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "thislist[1] = \"blackcurrant\"\n",
    "print(thislist)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Yes, 'apple' is in the fruits list\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "if \"apple\" in thislist:\n",
    "  print(\"Yes, 'apple' is in the fruits list\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['orange', 'kiwi', 'melon']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\", \"orange\", \"kiwi\", \"melon\", \"mango\"]\n",
    "print(thislist[-4:-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['cherry', 'orange', 'kiwi', 'melon', 'mango']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\", \"orange\", \"kiwi\", \"melon\", \"mango\"]\n",
    "print(thislist[2:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana', 'cherry', 'orange']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\", \"orange\", \"kiwi\", \"melon\", \"mango\"]\n",
    "print(thislist[:4])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['cherry', 'orange', 'kiwi']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\", \"orange\", \"kiwi\", \"melon\", \"mango\"]\n",
    "print(thislist[2:5])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cherry\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "print(thislist[-1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "banana\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "print(thislist[1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'list'>\n"
     ]
    }
   ],
   "source": [
    "mylist = [\"apple\", \"banana\", \"cherry\"]\n",
    "print(type(mylist))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "print(len(thislist))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['apple', 'banana', 'cherry']\n"
     ]
    }
   ],
   "source": [
    "thislist = [\"apple\", \"banana\", \"cherry\"]\n",
    "print(thislist)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}