import statistics as st
import pandas as pd
import plotly.figure_factory as pff
import random
import plotly.graph_objects as go

dataframe = pd.read_csv('medium_data.csv')
reading_time = dataframe['reading_time'].to_list()
pop_mean = st.mean(reading_time)
stdev = st.stdev(reading_time)

mean_data = []

for i in range(0, 100):
    sample_data = []
    for i in range(0, 30):
        rand_ind = random.randint(0, len(reading_time) - 1)
        ind_val = reading_time[rand_ind]
        sample_data.append(ind_val)        
    meanofsam = st.mean(sample_data)
    mean_data.append(meanofsam)

sam_mean = st.mean(mean_data)
stdev_sam = st.stdev(mean_data)
lowstdev2 = sam_mean - stdev
highstdev2 = sam_mean + stdev
lowstdev3 = sam_mean - (2*stdev)
highstdev3 = sam_mean + (2*stdev)
lowstdev4 = sam_mean - (3*stdev)
highstdev4 = sam_mean + (3*stdev)

fig = pff.create_distplot([mean_data], ['MEANS OF SAMPLE DATA'])
fig.add_trace(go.Scatter(x =[lowstdev2, lowstdev2], y=[0, 0.62667], mode='lines', name='Lower Stdev 1'))
fig.add_trace(go.Scatter(x =[highstdev2, highstdev2], y=[0, 0.62667], mode='lines', name='Higher Stdev 1'))
fig.add_trace(go.Scatter(x =[lowstdev3, lowstdev3], y=[0, 0.62667], mode='lines', name='Lower Stdev 2'))
fig.add_trace(go.Scatter(x =[highstdev3, highstdev3], y=[0, 0.62667], mode='lines', name='Higher Stdev 2'))
fig.add_trace(go.Scatter(x =[lowstdev4, lowstdev4], y=[0, 0.62667], mode='lines', name='Lower Stdev 3'))
fig.add_trace(go.Scatter(x =[highstdev4, highstdev4], y=[0, 0.62667], mode='lines', name='Lower Stdev 3'))

fig.show()

print('Population Mean: '+str(pop_mean))
print('Sample Mean: '+str(sam_mean))
