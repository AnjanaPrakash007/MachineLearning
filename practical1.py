{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 52,
   "id": "105e7fc5",
   "metadata": {},
   "outputs": [
    {
     "ename": "AttributeError",
     "evalue": "'DataFrame' object has no attribute 'date'",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "\u001b[0;32m/tmp/ipykernel_2695/989488618.py\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     75\u001b[0m \u001b[0mdf\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mgenerate_sample_data\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mrow_count\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m1000\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     76\u001b[0m \u001b[0mcleanup_column_names\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdf\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 77\u001b[0;31m \u001b[0mdf\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'Date'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mto_datetime\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdate\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     78\u001b[0m \u001b[0mdf\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'User class'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mdf\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'User Type'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmap\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mexpand_user_type\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     79\u001b[0m \u001b[0mdf\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'Purchase week'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mdf\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m'Date'\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mapplymap\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;32mlambda\u001b[0m \u001b[0mdt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0mdt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mweek\u001b[0m \u001b[0;32mif\u001b[0m \u001b[0;32mnot\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0misnull\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mdt\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mweek\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;32melse\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/.local/lib/python3.10/site-packages/pandas/core/generic.py\u001b[0m in \u001b[0;36m__getattr__\u001b[0;34m(self, name)\u001b[0m\n\u001b[1;32m   5900\u001b[0m         ):\n\u001b[1;32m   5901\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mname\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 5902\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mobject\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__getattribute__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   5903\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   5904\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__setattr__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mvalue\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m->\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mAttributeError\u001b[0m: 'DataFrame' object has no attribute 'date'"
     ]
    }
   ],
   "source": [
    "\n",
    "import random\n",
    "import datetime\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "from random import randrange\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "\n",
    "sns.set_style('whitegrid')\n",
    "sns.set_context('talk')\n",
    "params={'legend.fontsize':'small','figure.figsize':(10,5),\n",
    "       'axes.labelsize':'medium',\n",
    "       'axes.titlesize':'medium',\n",
    "       'xtick.labelsize':'medium',\n",
    "       'ytick.labelsize':'medium'}\n",
    "plt.rcParams.update(params)\n",
    "fom IPython.display import display,HTML\n",
    "\n",
    "def _random_date(start,date_count):\n",
    "    current=start\n",
    "    while date_count>0:\n",
    "        curr=current+datetime.timedelta(days=randrange(42))\n",
    "        yield curr\n",
    "        date_count-=1\n",
    "        \n",
    "def generate_sample_data(row_count=100):\n",
    "    #sentinels\n",
    "    startDate=datetime.datetime(2014,1,12,4)\n",
    "    serial_number_sentinel=1000\n",
    "    user_id_sentinel=5001\n",
    "    product_id_sentinel=100\n",
    "    price_sentinel=200\n",
    "    #base list of attributes\n",
    "    data_dict = {\n",
    "        'Serial No': np.arange(row_count)+serial_number_sentinel,\n",
    "        'Date':np.random.permutation(pd.to_datetime([x.strftime('%d-%m-%y')for x in _random_date(startDate,row_count)]).date),\n",
    "        'User ID':np.random.permutation(np.random.randint(0,row_count,size=int(row_count/10)) + user_id_sentinel).tolist()*10,\n",
    "        'Quantity purchased': np.random.permutation(np.random.randint(1,42,size=row_count)),\n",
    "        'Product Id':np.random.permutation(np.random.randint(0,row_count,size=int(row_count/10)) + user_id_sentinel).tolist()*10,\n",
    "        'Price':np.round(np.abs(np.random.randn(row_count)+1)*price_sentinel,decimals=2),\n",
    "        'User Type':np.random.permutation([chr(random.randrange(97, 97 + 3 + 1)) for i in range(row_count)]),\n",
    "           \n",
    "        }\n",
    "    for index in range (int(np.sqrt(row_count))):\n",
    "        data_dict['Price'][np.argmax(data_dict['Price']==random.choice(data_dict['Price']))]=np.nan\n",
    "        data_dict['User Type'][np.argmax(data_dict['User Type']==random.choice(data_dict['User Type']))]=np.nan\n",
    "        data_dict['Date'][np.argmax(data_dict['Date']==random.choice(data_dict['Date']))]=np.nan\n",
    "        data_dict['Product Id'][np.argmax(data_dict['Product Id']==random.choice(data_dict['Product Id']))]=0\n",
    "        data_dict['Serial No'][np.argmax(data_dict['Serial No']==random.choice(data_dict['Serial No']))]=-1\n",
    "        data_dict['User ID'][np.argmax(data_dict['User ID']==random.choice(data_dict['User ID']))]=-102 \n",
    "    df=pd.DataFrame(data_dict)\n",
    "    return df\n",
    "\n",
    "def cleanup_column_names(df,rename_dict={},do_inplace=True):\n",
    "\n",
    "    if not rename_dict:\n",
    "        return df.rename(columns={col:col.lower().replace('','_')\n",
    "                                  for col in df.columns.values.tolist()},\n",
    "                         inplace=do_inplace)\n",
    "    else:\n",
    "        return df.rename(columns=rename_dict,inplace=do_inplace)\n",
    "\n",
    "\n",
    "def expand_user_type(u_type):\n",
    "    if u_type in ['a','b']:\n",
    "        return 'new'\n",
    "    elif u_type=='c':\n",
    "        return 'existing'\n",
    "    elif u_type=='d':\n",
    "        return 'loyal_existing'\n",
    "    else:\n",
    "        return 'error'\n",
    "        \n",
    "        \n",
    "df=generate_sample_data(row_count=1000)\n",
    "cleanup_column_names(df)\n",
    "df['Date']=pd.to_datetime(df.date)\n",
    "df['User class']=df['User Type'].map(expand_user_type)\n",
    "df['Purchase week']=df[['Date']].applymap(lambda dt:dt.week if not pd.isnull(dt.week)else 0)\n",
    "df=df.dropna(subset=['Date'])\n",
    "df['Price'].fillna(value=np.round(df.price.mean(),decimals=2),inplace=True)\n",
    "display(df.head())\n",
    "        \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c2779e15",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f28e2549",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}