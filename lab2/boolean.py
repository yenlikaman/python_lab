{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n"
     ]
    }
   ],
   "source": [
    "x = 200\n",
    "print(isinstance(x, int))"
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
      "YES!\n"
     ]
    }
   ],
   "source": [
    "def myFunction() :\n",
    "  return True\n",
    "\n",
    "if myFunction():\n",
    "  print(\"YES!\")\n",
    "else:\n",
    "  print(\"NO!\")"
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
      "False\n"
     ]
    }
   ],
   "source": [
    "class myclass():\n",
    "  def __len__(self):\n",
    "    return 0\n",
    "\n",
    "myobj = myclass()\n",
    "print(bool(myobj))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "False"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bool(False)\n",
    "bool(None)\n",
    "bool(0)\n",
    "bool(\"\")\n",
    "bool(())\n",
    "bool([])\n",
    "bool({})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "bool(\"abc\")\n",
    "bool(123)\n",
    "bool([\"apple\", \"cherry\", \"banana\"])"
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
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "x = \"Hello\"\n",
    "y = 15\n",
    "\n",
    "print(bool(x))\n",
    "print(bool(y))"
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
      "b is not greater than a\n"
     ]
    }
   ],
   "source": [
    "a = 200\n",
    "b = 33\n",
    "\n",
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
      "True\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "print(bool(\"Hello\"))\n",
    "print(bool(15))"
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
      "True\n",
      "False\n",
      "False\n"
     ]
    }
   ],
   "source": [
    "print(10 > 9)\n",
    "print(10 == 9)\n",
    "print(10 < 9)"
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