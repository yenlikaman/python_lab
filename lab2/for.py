{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "red apple\n",
      "red banana\n",
      "red cherry\n",
      "big apple\n",
      "big banana\n",
      "big cherry\n",
      "tasty apple\n",
      "tasty banana\n",
      "tasty cherry\n"
     ]
    }
   ],
   "source": [
    "adj = [\"red\", \"big\", \"tasty\"]\n",
    "fruits = [\"apple\", \"banana\", \"cherry\"]\n",
    "\n",
    "for x in adj:\n",
    "  for y in fruits:\n",
    "    print(x, y)"
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
      "0\n",
      "1\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "for x in range(6):\n",
    "  if x == 3: break\n",
    "  print(x)\n",
    "else:\n",
    "  print(\"Finally finished!\")"
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
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "Finally finished!\n"
     ]
    }
   ],
   "source": [
    "for x in range(6):\n",
    "  print(x)\n",
    "else:\n",
    "  print(\"Finally finished!\")"
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
      "2\n",
      "5\n",
      "8\n",
      "11\n",
      "14\n",
      "17\n",
      "20\n",
      "23\n",
      "26\n",
      "29\n"
     ]
    }
   ],
   "source": [
    "for x in range(2, 30, 3):\n",
    "  print(x)"
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
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "for x in range(2, 6):\n",
    "  print(x)"
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
      "0\n",
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "for x in range(6):\n",
    "  print(x)"
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
      "apple\n",
      "cherry\n"
     ]
    }
   ],
   "source": [
    "fruits = [\"apple\", \"banana\", \"cherry\"]\n",
    "for x in fruits:\n",
    "  if x == \"banana\":\n",
    "    continue\n",
    "  print(x)"
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
      "apple\n"
     ]
    }
   ],
   "source": [
    "fruits = [\"apple\", \"banana\", \"cherry\"]\n",
    "for x in fruits:\n",
    "  if x == \"banana\":\n",
    "    break\n",
    "  print(x)"
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
      "apple\n",
      "banana\n"
     ]
    }
   ],
   "source": [
    "fruits = [\"apple\", \"banana\", \"cherry\"]\n",
    "for x in fruits:\n",
    "  print(x)\n",
    "  if x == \"banana\":\n",
    "    break"
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
      "apple\n",
      "banana\n",
      "cherry\n"
     ]
    }
   ],
   "source": [
    "fruits = [\"apple\", \"banana\", \"cherry\"]\n",
    "for x in fruits:\n",
    "  print(x)"
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