{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "a = 33\n",
    "b = 200\n",
    "\n",
    "if b > a:\n",
    "  pass\n",
    "\n",
    "# having an empty if statement like this, would raise an error without the pass statement"
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
      "a is NOT greater than b\n"
     ]
    }
   ],
   "source": [
    "a = 33\n",
    "b = 200\n",
    "if not a > b:\n",
    "  print(\"a is NOT greater than b\")"
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
      "At least one of the conditions is True\n"
     ]
    }
   ],
   "source": [
    "a = 200\n",
    "b = 33\n",
    "c = 500\n",
    "if a > b or a > c:\n",
    "  print(\"At least one of the conditions is True\")"
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
      "Both conditions are True\n"
     ]
    }
   ],
   "source": [
    "a = 200\n",
    "b = 33\n",
    "c = 500\n",
    "if a > b and c > a:\n",
    "  print(\"Both conditions are True\")"
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
      "B\n"
     ]
    }
   ],
   "source": [
    "a = 2\n",
    "b = 330\n",
    "print(\"A\") if a > b else print(\"B\")"
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
      "b is not greater than a\n"
     ]
    }
   ],
   "source": [
    "a = 200\n",
    "b = 33\n",
    "if b > a:\n",
    "  print(\"b is greater than a\")\n",
    "else:\n",
    "  print(\"b is not greater than a\")"
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
      "a is greater than b\n"
     ]
    }
   ],
   "source": [
    "a = 200\n",
    "b = 33\n",
    "if b > a:\n",
    "  print(\"b is greater than a\")\n",
    "elif a == b:\n",
    "  print(\"a and b are equal\")\n",
    "else:\n",
    "  print(\"a is greater than b\")"
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
      "a and b are equal\n"
     ]
    }
   ],
   "source": [
    "a = 33\n",
    "b = 33\n",
    "if b > a:\n",
    "  print(\"b is greater than a\")\n",
    "elif a == b:\n",
    "  print(\"a and b are equal\")"
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
      "b is greater than a\n"
     ]
    }
   ],
   "source": [
    "a = 33\n",
    "b = 200\n",
    "if b > a:\n",
    "  print(\"b is greater than a\")"
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