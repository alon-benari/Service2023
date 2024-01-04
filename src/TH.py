import pandas as pd
import matplotlib.pyplot as plt


class TH:
    '''
    A set of methods to prodcue visualizations for TH
    '''

    def load(self,fname):
        '''
        A method to load data
        fname -  string, the csv for the file
        '''
        self.data = pd.read_excel('../assets/'+fname)
        self.data['Month'] = self.data.Created.apply(lambda x: pd.Timestamp(x).month)



th = TH()
th.load('TH0.xlsx')

#th.data[['ID','TelehealthTopic']].groupby('TelehealthTopic').count().plot(kind = 'barh')
#th.data[['QuestionorRequest','Month']].groupby('Month').count()
#  th.data[['QuestionorRequest','URGENCY']].groupby('URGENCY').count()
# th.data[['STATUS','Month']].groupby(['Month','STATUS']).value_counts()
