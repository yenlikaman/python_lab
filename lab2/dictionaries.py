{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'key1': 0, 'key2': 0, 'key3': 0}\n"
     ]
    }
   ],
   "source": [
    "x = ('key1', 'key2', 'key3')\n",
    "y = 0\n",
    "\n",
    "thisdict = dict.fromkeys(x, y)\n",
    "\n",
    "print(thisdict)\n"
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
      "child1\n",
      "name: Emil\n",
      "year: 2004\n",
      "child2\n",
      "name: Tobias\n",
      "year: 2007\n",
      "child3\n",
      "name: Linus\n",
      "year: 2011\n"
     ]
    }
   ],
   "source": [
    "myfamily = {\n",
    "  \"child1\" : {\n",
    "    \"name\" : \"Emil\",\n",
    "    \"year\" : 2004\n",
    "  },\n",
    "  \"child2\" : {\n",
    "    \"name\" : \"Tobias\",\n",
    "    \"year\" : 2007\n",
    "  },\n",
    "  \"child3\" : {\n",
    "    \"name\" : \"Linus\",\n",
    "    \"year\" : 2011\n",
    "  }\n",
    "}\n",
    "\n",
    "for x, obj in myfamily.items():\n",
    "    print(x)\n",
    "    \n",
    "    for y in obj:\n",
    "        print(y + ':', obj[y])\n"
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
      "Tobias\n"
     ]
    }
   ],
   "source": [
    "myfamily = {\n",
    "  \"child1\" : {\n",
    "    \"name\" : \"Emil\",\n",
    "    \"year\" : 2004\n",
    "  },\n",
    "  \"child2\" : {\n",
    "    \"name\" : \"Tobias\",\n",
    "    \"year\" : 2007\n",
    "  },\n",
    "  \"child3\" : {\n",
    "    \"name\" : \"Linus\",\n",
    "    \"year\" : 2011\n",
    "  }\n",
    "}\n",
    "\n",
    "print(myfamily[\"child2\"][\"name\"])"
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
      "{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}\n"
     ]
    }
   ],
   "source": [
    "myfamily = {\n",
    "  \"child1\" : {\n",
    "    \"name\" : \"Emil\",\n",
    "    \"year\" : 2004\n",
    "  },\n",
    "  \"child2\" : {\n",
    "    \"name\" : \"Tobias\",\n",
    "    \"year\" : 2007\n",
    "  },\n",
    "  \"child3\" : {\n",
    "    \"name\" : \"Linus\",\n",
    "    \"year\" : 2011\n",
    "  }\n",
    "}\n",
    "\n",
    "print(myfamily)\n"
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
      "{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}\n"
     ]
    }
   ],
   "source": [
    "thisdict = {\n",
    "  \"brand\": \"Ford\",\n",
    "  \"model\": \"Mustang\",\n",
    "  \"year\": 1964\n",
    "}\n",
    "mydict = thisdict.copy()\n",
    "print(mydict)"
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
      "brand\n",
      "model\n",
      "year\n"
     ]
    }
   ],
   "source": [
    "thisdict =\t{\n",
    "  \"brand\": \"Ford\",\n",
    "  \"model\": \"Mustang\",\n",
    "  \"year\": 1964\n",
    "}\n",
    "for x in thisdict.keys():\n",
    "  print(x)\n"
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
      "Ford\n",
      "Mustang\n",
      "1964\n"
     ]
    }
   ],
   "source": [
    "thisdict =\t{\n",
    "  \"brand\": \"Ford\",\n",
    "  \"model\": \"Mustang\",\n",
    "  \"year\": 1964\n",
    "}\n",
    "for x in thisdict.values():\n",
    "  print(x)\n"
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
      "brand\n",
      "model\n",
      "year\n"
     ]
    }
   ],
   "source": [
    "thisdict =\t{\n",
    "  \"brand\": \"Ford\",\n",
    "  \"model\": \"Mustang\",\n",
    "  \"year\": 1964\n",
    "}\n",
    "for x in thisdict:\n",
    "  print(x)\n"
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
      "{'brand': 'Ford', 'year': 1964}\n"
     ]
    }
   ],
   "source": [
    "thisdict = {\n",
    "  \"brand\": \"Ford\",\n",
    "  \"model\": \"Mustang\",\n",
    "  \"year\": 1964\n",
    "}\n",
    "del thisdict[\"model\"]\n",
    "print(thisdict)"
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
      "{'brand': 'Ford', 'year': 1964}\n"
     ]
    }
   ],
   "source": [
    "thisdict = {\n",
    "  \"brand\": \"Ford\",\n",
    "  \"model\": \"Mustang\",\n",
    "  \"year\": 1964\n",
    "}\n",
    "thisdict.pop(\"model\")\n",
    "print(thisdict)"
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
      "{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}\n"
     ]
    }
   ],
   "source": [
    "thisdict = {\n",
    "  \"brand\": \"Ford\",\n",
    "  \"model\": \"Mustang\",\n",
    "  \"year\": 1964\n",
    "}\n",
    "thisdict.update({\"color\": \"red\"})\n",
    "print(thisdict)"
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
      "{'brand': 'Ford', 'model': 'Mustang', 'year': 2018}\n"
     ]
    }
   ],
   "source": [
    "thisdict = {\n",
    "  \"brand\": \"Ford\",\n",
    "  \"model\": \"Mustang\",\n",
    "  \"year\": 1964\n",
    "}\n",
    "thisdict[\"year\"] = 2018\n",
    "print(thisdict)\n"
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
      "Yes, 'model' is one of the keys in the thisdict dictionary\n"
     ]
    }
   ],
   "source": [
    "thisdict = {\n",
    "  \"brand\": \"Ford\",\n",
    "  \"model\": \"Mustang\",\n",
    "  \"year\": 1964\n",
    "}\n",
    "if \"model\" in thisdict:\n",
    "  print(\"Yes, 'model' is one of the keys in the thisdict dictionary\")"
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
      "dict_values(['Ford', 'Mustang', 1964])\n",
      "dict_values(['Ford', 'Mustang', 1964, 'red'])\n"
     ]
    }
   ],
   "source": [
    "car = {\n",
    "\"brand\": \"Ford\",\n",
    "\"model\": \"Mustang\",\n",
    "\"year\": 1964\n",
    "}\n",
    "\n",
    "x = car.values()\n",
    "\n",
    "print(x) #before the change\n",
    "\n",
    "car[\"color\"] = \"red\"\n",
    "\n",
    "print(x) #after the change"
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
      "dict_keys(['brand', 'model', 'year'])\n",
      "dict_keys(['brand', 'model', 'year', 'color'])\n"
     ]
    }
   ],
   "source": [
    "car = {\n",
    "\"brand\": \"Ford\",\n",
    "\"model\": \"Mustang\",\n",
    "\"year\": 1964\n",
    "}\n",
    "\n",
    "x = car.keys()\n",
    "\n",
    "print(x) #before the change\n",
    "\n",
    "car[\"color\"] = \"white\"\n",
    "\n",
    "print(x) #after the change"
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
      "Mustang\n"
     ]
    }
   ],
   "source": [
    "thisdict = {\n",
    "  \"brand\": \"Ford\",\n",
    "  \"model\": \"Mustang\",\n",
    "  \"year\": 1964\n",
    "}\n",
    "x = thisdict[\"model\"]\n",
    "print(x)"
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
      "{'name': 'John', 'age': 36, 'country': 'Norway'}\n"
     ]
    }
   ],
   "source": [
    "thisdict = dict(name = \"John\", age = 36, country = \"Norway\")\n",
    "print(thisdict)"
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
      "<class 'dict'>\n"
     ]
    }
   ],
   "source": [
    "thisdict = {\n",
    "  \"brand\": \"Ford\",\n",
    "  \"model\": \"Mustang\",\n",
    "  \"year\": 1964\n",
    "}\n",
    "print(type(thisdict))"
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
      "{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}\n"
     ]
    }
   ],
   "source": [
    "thisdict = {\n",
    "  \"brand\": \"Ford\",\n",
    "  \"model\": \"Mustang\",\n",
    "  \"year\": 1964\n",
    "}\n",
    "print(thisdict)"
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