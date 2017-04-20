import matplotlib.cbook as cbook
with cbook.get_sample_data('goog.npz') as datafile:
    r = np.load(datafile)['price_data'].view(np.recarray)
# Matplotlib prefers datetime instead of np.datetime64.
date = r.date.astype('O')
plt.figure()
plt.plot(date, r.close)
plt.title('Default date handling can cause overlapping labels')