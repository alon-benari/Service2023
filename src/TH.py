import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

    def barh_graph(self, object, fname):
        '''
        A method to return a bar graph of counts
        '''
        fig, ax = plt.subplots(1,1, figsize = (14,8))
        object.plot(kind = 'barh', fontsize = 6, ax = ax)
        ax.set_xlabel('count')
        plt.savefig('../figs/'+fname)
        plt.show

th = TH()
th.load('requests.xlsx')

#th.data[['ID','TelehealthTopic']].groupby('TelehealthTopic').count().plot(kind = 'barh')
#th.data[['QuestionorRequest','Month']].groupby('Month').count()
#  th.data[['QuestionorRequest','URGENCY']].groupby('URGENCY').count()
# th.data[['STATUS','Month']].groupby(['Month','STATUS']).value_counts()

#Students 
th.load('StaffTraining.xlsx')

# th.data['Student Status'].value_counts() # counts of student per category.
th.data[['Month']].value_counts().\
  reset_index().sort_values(by = 'Month').\
  set_index('Month')
  #training per month, instead of total count
#
# Box plot 
fig,ax  = plt.subplots(1, figsize = (10,8))
ax.grid('on')
th.data[['Month']].value_counts().reset_index().\
        sort_values(by = 'Month').set_index('Month').boxplot(ax = ax)
plt.savefig('DistribMonthTrainig.jpeg' )
plt.show()


# Equipment
th.load('THEquipment.xlsx')
th.data['DateCreated'] = th.data.Created.apply(lambda x: x.date())
th.data['DateCompleted'] = th.data['Date Install Completed'].apply(lambda x: x.date())
days = -(th.data['DateCreated'] - th.data['DateCompleted'])
days.dropna(inplace=True)
fig, ax = plt.subplots(1,1, figsize = (12,10))
ax.set_ylabel('days')
days.apply(lambda x: x.days).plot.box(ax = ax)
plt.savefig('../figs/Time2Equipment.jpeg')
plt.show()

# MHV
th.load('MHVStaffAddModificationRequest.xlsx')
object = th.data.Month.reset_index().groupby('Month').count()
th.barh_graph(object,'MHV_Staff_Add_Request.jpeg')

# MHV
th.load('MHV_TRIAGE_TEAM_NEW_REMOVE_REQUESTS .xlsx')
th.data['Month'] = th.data.Created.apply(lambda x: x.date().month)
th.data['Month'].reset_index().groupby('Month').count()
th.barh_graph(object,'MonthlyTriageTeamRemoveReqs.jpeg')

#MHV
th.load('MHVAddRemovePatientRequests .xlsx')
th.data['Month'] = th.data.Created.apply(lambda x: x.date().month)
object = th.data['Month'].value_counts().reset_index().sort_values('Month').set_index('Month')
th.barh_graph(object,"AddRemovePatient.jpeg")